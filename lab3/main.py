import sys

import MLexer
import Mparser
import AST
import TreePrinter

if __name__ == '__main__':

    filename = sys.argv[1] if len(sys.argv) > 1 else "example2.m"
    try:
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=MLexer.lexer)
    if parser.errorok:
        print(ast.printTree())
    else:
        print("error while parsing")
