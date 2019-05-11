import operator
import sys

import numpy as np

import AST
from Exceptions import *
from Memory import *
from visit import *

sys.setrecursionlimit(10000)


class Interpreter(object):
    def __init__(self):
        self.memory_stack = MemoryStack()
        self.binary_ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            ".+": operator.add,
            ".-": operator.sub,
            ".*": np.multiply,
            "./": np.divide,
            "<": operator.lt,
            ">": operator.gt,
            "<=": operator.le,
            ">=": operator.ge,
            "==": operator.eq,
            "!=": operator.ne,
        }
        self.unary_ops = {
            "-": operator.neg,
            "'": np.transpose
        }
        self.functions_names = {
            'EYE': np.eye,
            'ZEROS': np.zeros,
            'ONES': np.ones
        }

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Node)
    def visit(self, node):
        pass

    @when(AST.Program)
    def visit(self, node):
        return self.visit(node.program)

    @when(AST.Block)
    def visit(self, node):
        for instruction in node.instruction:
            self.visit(instruction)

    @when(AST.Instruction)
    def visit(self, node):
        return self.visit(node.line)

    @when(AST.BinaryExpression)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)

        return self.binary_ops.get(node.op)(r1, r2)

    @when(AST.UnaryExpression)
    def visit(self, node):
        r1 = node.operand.accept()
        return self.unary_ops.get(node.operator)(r1)

    @when(AST.Function)
    def visit(self, node):
        return self.functions_names.get(node.name)(node.args.result)

    @when(AST.Variable)
    def visit(self, node):
        return self.memory_stack.get(node.name)

    @when(AST.If)
    def visit(self, node):
        if node.cond.accept(self):
            return node.if_block.accept(self)
        else:
            if node.else_block:
                return node.else_block.accept(self)

    @when(AST.While)
    def visit(self, node):
        result = None
        while node.cond.accept(self):
            result = node.while_block.accept(self)
        return result

    @when(AST.Range)
    def visit(self, node):
        start = node.start.accept(self)
        end = node.end.accept(self)

        if type(start) == str:
            start = self.memory_stack.get(start)
        if type(end) == str:
            end = self.memory_stack.get(end)

        return range(start, end)

    @when(AST.For)
    def visit(self, node):
        result = None
        for i in node.range.accept(self):
            self.memory_stack.insert(node.id, i)
            result = node.for_block.accept(self)
        return result

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(node.result.accpet(self))

    @when(AST.Print)
    def visit(self, node):
        for i in node.expression:
            print(i.accept(self))

    @when(AST.TensorID)
    def visit(self, node):

        tensor = self.memory_stack.get(node.variable)

        for x in node.key:
            tensor = tensor[x.accept(self)]
        return tensor.accept(self)

    @when(AST.Error)
    def visit(self, node):
        pass

    # +++++++++++++++

    @when(AST.Tensor)
    def visit(self, node):

        return np.asarray(node.rows.accept(self))

    @when(AST.Rows)
    def visit(self, node):
        v = []
        for r in node.row_list:
            v.append(r.accept(self))
        return v[0]

    @when(AST.Seq)
    def visit(self, node):
        val = []
        for x in node.expression:
            val.append(x.accept(self))
        return np.asarray(val)

    @when(AST.Result)
    def visit(self, node):
        if type(node.result) == int or type(node.result) == str:
            return node.result
        else:
            return node.result.accept(self)

    @when(AST.Assignment)
    def visit(self, node):
        right = None
        left = node.left if isinstance(node.left, AST.TensorID) else node.left.name
        if node.op == "=":
            right = node.right.accept(self)
        elif node.op == "+=":
            right = node.right.accept(self)
            right = operator.add(right, node.left.accept(self))
        elif node.op == "*=":
            right = node.right.accept(self)
            right = operator.mul(right, node.left.accept(self))
        elif node.op == "/=":
            right = node.right.accept(self)
            right = operator.truediv(right, node.left.accept(self))
        elif node.op == "-=":
            right = node.right.accept(self)
            right = operator.sub(right, node.left.accept(self))

        if isinstance(node.left, AST.TensorID):
            tensor = self.memory_stack.get(left.variable)
            where = left.key.accept(self)
            access = tensor
            for k in where[:-1]:
                access = access[k]
            access[-1] = right
            self.memory_stack.insert(left.variable, tensor)
        else:
            self.memory_stack.insert(left, right)

    @when(AST.Transpose)
    def visit(self, node):
        r1 = node.operand.accept(self)
        return np.transpose(r1)

    @when(AST.Negation)
    def visit(self, node):
        r1 = node.operand.accept(self)
        return operator.neg(r1)
