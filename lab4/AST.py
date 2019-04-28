class Node(object):
    def __init__(self, node_type, children=None, leaf=None, line=None):
        self.line = line
        self.children = children
        if children is None:
            self.children = []
        self.node_type = node_type
        self.leaf = leaf


class Function(Node):
    def __init__(self, name, args, line):
        super().__init__(self.__class__, [args], name, line)
        self.name = name
        self.args = args

    def __repr__(self):
        return f'{self.name}({self.args})'


class Variable(Node):
    def __init__(self, name, line):
        super().__init__(self.__class__, leaf=name, line=line)
        self.name = name

    def __repr__(self):
        return self.name


class If(Node):
    def __init__(self, cond, if_block, else_block=None):
        super().__init__(self.__class__, [cond, if_block, else_block], ['if', ':', 'else'])
        self.cond = cond
        self.if_block = if_block
        self.else_block = else_block
        if else_block is None:
            self.children = self.children[:2]
            self.leaf = self.leaf[:2]

    def __repr__(self):
        return f'if {self.cond}: {self.if_block}' if self.else_block is Node else f'if {self.cond}: {self.if_block} else {self.else_block} '


class While(Node):
    def __init__(self, cond, while_block):
        super().__init__(self.__class__, [cond, while_block], 'while')
        self.cond = cond
        self.while_block = while_block

    def __repr__(self):
        return f'while {self.cond}: {self.while_block}'


class Range(Node):
    def __init__(self, start, end):
        super().__init__(self.__class__, [start, end], 'range')
        self.start = start
        self.end = end

    def __repr__(self):
        return f'{self.start}:{self.end}'


class For(Node):
    def __init__(self, id, range, for_block):
        super().__init__(self.__class__, [id, range, for_block], 'for')
        self.id = id
        self.range = range
        self.for_block = for_block

    def __repr__(self):
        return f'for {self.id} {self.range} {self.for_block}'


class Break(Node):
    def __init__(self, line):
        super().__init__(self.__class__, leaf='break', line=line)

    def __repr__(self):
        return 'break'


class Continue(Node):
    def __init__(self, line):
        super().__init__(self.__class__, leaf='continue', line=line)

    def __repr__(self):
        return 'continue'


class Return(Node):
    def __init__(self, result, line):
        super().__init__(self.__class__, [result], 'break', line=line)
        self.result = result

    def __repr__(self):
        return f'return {self.result}'


class Print(Node):
    def __init__(self, expression, line):
        super().__init__(self.__class__, [expression], 'print', line=line)
        self.expression = expression

    def __repr__(self):
        return f'print {self.expression}'


class TensorID(Node):
    def __init__(self, variable, key, line):
        super().__init__(self.__class__, [variable, key], 'ref', line)
        self.variable = variable
        self.key = key

    def __repr__(self):
        return f'{self.variable}[{self.key}]'


class Block(Node):
    def __init__(self, instruction):
        super().__init__(self.__class__, [instruction])
        self.instruction = self.children

    def __repr__(self):
        return "{\n" + "\n".join(map(str, self.instruction)) + "\n}"


class Program(Node):
    def __init__(self, program):
        super().__init__(self.__class__, [program])
        self.program = program

    def __repr__(self):
        return str(self.program)


class Instruction(Node):
    def __init__(self, line):
        super().__init__(self.__class__, [line])
        self.line = line

    def __repr__(self):
        return str(self.line)


class Tensor(Node):
    def __init__(self, rows,line):
        super().__init__(self.__class__, [rows], "tensor",line=line)
        self.rows = rows

    def __repr__(self):
        return str(self.rows)


class Result(Node):
    def __init__(self, result):
        super().__init__(self.__class__, [result])
        self.result = result

    def __repr__(self):
        return str(self.result)


class Rows(Node):
    def __init__(self, sequence):
        super().__init__(self.__class__, [sequence])
        self.row_list = self.children

    def __repr__(self):
        return "[" + ", ".join(map(str, self.row_list)) + "]"

    def __len__(self):
        return len(self.row_list)

    def __getitem__(self, item):
        return self.row_list[item]


class Seq(Node):
    def __init__(self, expression):
        super().__init__(self.__class__, [expression])
        self.expression = self.children

    def __repr__(self):
        return "{}".format(self.expression)

    def __len__(self):
        return len(self.expression)

    def __getitem__(self, item):
        return self.expression[item]


class BinaryExpression(Node):
    def __init__(self, left, op, right,line):
        super().__init__(self.__class__, [left, right], op,line=line)
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.left} {self.op} {self.right}'


class Assignment(BinaryExpression):
    pass


class UnaryExpression(Node):
    def __init__(self, operator, operand, left=True):
        super().__init__(self.__class__, [operand], operator)
        self.operator = operator
        self.operand = operand
        self.left = left

    def __repr__(self):
        order = [self.operator, self.operand] if self.left else [self.operand, self.operator]
        return '{}{}'.format(*order)


class Negation(UnaryExpression):
    def __init__(self, operand):
        super().__init__('-', operand)


class Transpose(UnaryExpression):
    def __init__(self, operand):
        super().__init__('\'', operand)


class Error(Node):
    pass
