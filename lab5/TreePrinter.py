from __future__ import print_function

import AST

def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator

def draw_tree(ind, other):
    return '║  ' * (ind - 1) + '╠══ ' * (1 if ind else 0) + str(other)

class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        if self.leaf is not None:
            return self.withLeaf(indent)
        else:
            return self.withNoLeaf(indent)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        res = list(zip(self.printLeafs(indent), self.printChildren(self.children, indent + 1)))

        return '\n'.join(map(lambda x: '\n'.join(x), res))

    @addToClass(AST.Node)
    def withLeaf(self, indent):
        res = [self.printLeaf(self.leaf, indent)]
        res += self.printChildren(self.children, indent + 1)
        return '\n'.join(res)

    @addToClass(AST.Node)
    def withNoLeaf(self, indent):
        res = []
        res += self.printChildren(self.children, indent)
        return '\n'.join(res)

    @addToClass(AST.Node)
    def printLeafs(self, indent):
        return list(map(lambda leaf: self.printLeaf(leaf, indent), self.leaf))

    @addToClass(AST.Node)
    def printLeaf(self, leaf, indent):
        return leaf.printTree(indent) if hasattr(leaf, 'printTree') else draw_tree(indent,leaf) 

    @addToClass(AST.Node)
    def printChildren(self, children, indent):
        return map(lambda child: (child.printTree(indent) if hasattr(child, 'printTree') else draw_tree(indent, child)), children)
