import AST
from SymbolTable import SymbolTable


class Tensor(object):
    def __init__(self, dimension):
        self.dimension = dimension


op_type_map = dict()
for op in ['+', '-', '/', '*']:
    op_type_map[(op, 'int', 'int')] = 'int'
    op_type_map[(op, 'float', 'float')] = 'float'
    op_type_map[(op, 'int', 'float')] = 'float'
    op_type_map[(op, 'float', 'int')] = 'float'

for op in ['>', '<', '==', '!=', '>=', '<=']:
    op_type_map[(op, 'int', 'int')] = 'int'
    op_type_map[(op, 'float', 'float')] = 'int'
    op_type_map[(op, 'int', 'float')] = 'int'
    op_type_map[(op, 'float', 'int')] = 'int'

for op in ['.+', '.-', './', '.*']:
    op_type_map[(op, Tensor.__name__, Tensor.__name__)] = Tensor.__name__

for op in ['+=', '-=', '*=', '/=']:
    op_type_map[(op, 'int', 'int')] = 'int'
    op_type_map[(op, 'float', 'float')] = 'float'
    op_type_map[(op, 'int', 'float')] = 'float'
    op_type_map[(op, 'float', 'int')] = 'float'


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.scope = SymbolTable(None, 'Root')
        self.success = True

    def visit_Program(self, node):
        # print(node.program)
        if node.program:
            self.visit(node.program)

    def visit_Block(self, node):
        self.scope = self.scope.push_scope('Block')
        self.visit(node.instruction)

    def visit_Instruction(self, node):
        self.visit(node.line)

    def visit_Negation(self, node):
        return node.operand

    def visit_Transpose(self, node):
        operand = self.visit(node.operand)
        if operand.get('type') is not 'Tensor':
            print(f'Transpose is possible only on Tensors Line: {node.operand.line}')
            self.success = False
            return operand
        else:
            result = {}
            size = operand.get('size')
            result['size'] = [size[1], size[0]]
            result['type'] = operand.get('type')
            return operand

    def visit_BinaryExpression(self, node):
        result = {}
        left = (self.visit(node.left))
        right = (self.visit(node.right))
        type1 = right.get('type')
        type2 = left.get('type')
        op = node.op
        key = (op, type1, type2)
        if key not in op_type_map.keys():
            print(f'Unsupported operation {type1} {op} {type2} Line: {node.line}')
            self.success = False
        elif type1 is 'Tensor' and type2 is 'Tensor':
            dim1 = right.get('size')
            dim2 = left.get('size')
            if dim1 and dim2:
                if len(dim1) is not len(dim2):
                    print(f'Incompatible dims {dim1} {op} {dim2} Line: {node.line}')
                    self.success = False
                elif op is './' or op is '.*':
                    if dim1[1] is not dim2[0]:
                        print(f'incompatible dims {dim1} {op} {dim2} Line: {node.line}')
                        self.success = False
                    else:
                        result['size'] = [dim1[0], dim2[1]]
                else:
                    if not dim1 == dim2:
                        print(f'Incompatible dims {dim1} {op} {dim2} Line: {node.line}')
                        self.success = False
            else:
                print('Incompatible types Line: {node.op.line}')
                self.success = False
        else:
            result['type'] = op_type_map[(op, type1, type2)]
        return result

    def visit_Assignment(self, node):
        if isinstance(node.left, AST.TensorID):
            v_name = node.left.variable
        else:
            v_name = node.left.name
        v_symbol = self.visit(node.right)
        if isinstance(node.left, AST.TensorID) and self.scope.get(v_name) is None:
            print(f'Tensor {v_name} out of scope')
            self.success = False
        if v_symbol:
            self.scope.put(v_name, v_symbol)

    def visit_Function(self, node):
        self.scope = self.scope.push_scope('Function')
        arg_type = self.visit(node.args).get('type')
        dim = node.args
        if arg_type == 'int':
            return {'type': 'Tensor', 'size': [dim] * 2}
        else:
            print(f'Unexpected parameter type \'{arg_type}\' In function {node.name} Line: {node.line}')
            self.success = False
        self.scope = self.scope.pop_scope()

    def visit_Result(self, node):
        result = {}
        if type(node.result).__name__ not in ['int', 'float', 'string']:
            result['size'] = self.visit(node.result)
        else:
            result['size'] = []
        result['type'] = type(node.result).__name__
        result['value'] = node.result
        return result

    def visit_Tensor(self, node):
        sizes = []
        if type(node.rows[0][0].result).__name__ is not 'Tensor':
            sizes.append(self.visit(node.rows))
            return sizes
        else:
            for res in node.rows[0]:
                sizes.append(self.visit(res.result))
            sizes = [x[0] for x in sizes]
            for s in sizes:
                if s is not sizes[0]:
                    print(f'Invalid matrix size Line: {node.line}')
                    self.success = False
                    return False
            return [len(node.rows[0]), sizes[0]]

    def visit_Rows(self, node):
        size = len(node.row_list[0])
        return size

    def visit_Variable(self, node):
        if node.name not in self.scope.entries.keys():
            print('Variable {node.name} not in scope Line: {node.line}')
            self.success = False
        return self.scope.get(node.name)

    def visit_While(self, node):
        c_type = self.visit(node.cond).get('type')
        if c_type is not 'int':
            print(f'Invalid condition Line: {node.line}')
            self.success = False
        self.scope = self.scope.push_scope('While')
        self.visit(node.while_block)
        self.scope = self.scope.pop_scope()

    def visit_For(self, node):
        range = self.visit(node.range)
        self.scope = self.scope.push_scope('For')
        self.scope.put(node.id, range)
        self.visit(node.for_block)
        self.scope = self.scope.pop_scope()

    def visit_Continue(self, node):
        scopes = self.get_scopes()
        if 'While' not in scopes and 'For' not in scopes:
            print(f'Continue not in Loop scope Line: {node.line}')
            self.success = False

    def visit_Return(self, node):
        scopes = self.get_scopes()
        if 'Function' not in scopes and 'For' not in scopes:
            print(f'Return not in Function scope Line: {node.line}')
            self.success = False
        self.visit(node.result)

    def visit_Break(self, node):
        scopes = self.get_scopes()
        if 'While' not in scopes and 'For' not in scopes:
            print(f'Break not in Loop scope Line: {node.line}')
            self.success = False

    def visit_If(self, node):
        c_type = self.visit(node.cond).get('type')
        if c_type is not 'int':
            print(f'Invalid condition Line: {node.line}')
            self.success = False

        self.scope = self.scope.push_scope('If')
        self.visit(node.if_block)
        self.scope = self.scope.pop_scope()
        if node.else_block:
            self.scope = self.scope.push_scope('Else')
            self.visit(node.else_block)
            self.scope = self.scope.pop_scope()

    def visit_TensorID(self, node):
        variable = self.scope.get(node.variable)
        if variable.get('type') is not 'Tensor':
            print(f'Variable {node.variable} is not a Tensor')
            self.success = False
        key = self.visit(node.key)
        if len(key) > len(variable.get('size')):
            print(f'Access out of dim Line: {node.line}')
            self.success = False
        else:
            size = variable.get('size')
            for i in range(len(key)):
                if self.visit(key[i]).get('value') >= self.visit(size[i]).get('value'):
                    print(f'Access out of range Line: {node.line}')
                    self.success = False
                    break

    def visit_Seq(self, node):
        return node.expression

    def get_scopes(self):
        scopes = []
        parent = self.scope
        while parent:
            scopes.append(parent.name)
            parent = parent.parent
        return scopes

    def visit_Range(self, node):
        start = self.visit(node.start)
        end = self.visit(node.end)
        if end.get('value') < start.get('value'):
            print(f'Invalid Range parameters Line: {node.line}')
            self.success = False

        return start

    def visit_Print(self, node):
        self.visit(node.expression)
