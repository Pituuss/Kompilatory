import ply.lex as lex

newLines = [-1]

literals = [
    '+',
    '-',
    '*',
    '/',
    '(',
    ')',
    '=',
    '<',
    '>',
    '\'',
    ',',
    '',
    ':',
    ';',
    '{',
    '}',
    '[',
    ']'
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT',
}

t_DOTSUM = r"\.\+"
t_DOTSUB = r"\.-"
t_DOTMUL = r"\.\*"
t_DOTDIV = r"\./"
t_SUMASSIGN = r"\+="
t_SUBASSIGN = r"-="
t_MULASSIGN = r"\*="
t_DIVASSIGN = r"/="
t_LEQ = r"<="
t_GEQ = r">="
t_NEQ = r"!="
t_EQ = r"=="

tokens = list(reserved.values())
tokens += ["FLOAT", "INTEGER", "STRING", "DOTSUM", "DOTSUB", "DOTMUL", "DOTDIV",
           "SUMASSIGN", "SUBASSIGN",
           "MULASSIGN", "DIVASSIGN", "LEQ", "GEQ", "NEQ", "EQ", "COMMENT", "ID"]

t_ignore = ' \t'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    for i in range(len(t.value)):
        newLines.append(t.lexpos + i)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_FLOAT(t):
    r'([0-9]+\.[0-9]*|\.[0-9]+) ([eE][-+]?[0-9]+)?'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[a-zA-Z0-9\_\-\+={\[\]}\';:/?>\.,<!@\#$%^&\*()|\~` ]*"'
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


def find_tok_column(token):
    return token.lexpos - newLines[token.lineno - 1]


lexer = lex.lex()
