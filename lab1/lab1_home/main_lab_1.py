import MLexer as scanner

if __name__ == '__main__':
    file = open("example.file", "r")
    text = file.read()
    lexer = scanner.lexer
    lexer.input(text)
    for token in lexer:
        index_in_line = scanner.find_index_in_line(lexer.lexdata, token)
        print("(%d, %d): %s(%s)" % (token.lineno, index_in_line, token.type, token.value))
