import ply.lex as lex

sym_tab = {}

literals = ['+', '-', '*', '/', '(', ')', '=', '<', '>', '\'', ',', '', ':', ';', '{', '}', '[', ']']

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

precedence = (
    ("right", '='),
    ("left", '+', '-'),
    ("left", '*', '/'),
)

t_DOTSUM = r"\.\+"
t_DOTDIFF = r"\.-"
t_DOTMUL = r"\.\*"
t_DOTDIV = r"\./"
t_ADDASSIGN = r"\+="
t_DIFFASSIGN = r"-="
t_MULASSIGN = r"\*="
t_DIVASSIGN = r"/="
t_LEQ = r"<="
t_GEQ = r">="
t_NEQ = r"!="
t_EQ = r"=="

tokens = list(reserved.values())
tokens += ["REAL_NUMBER", "NUMBER", "STRING", "DOTSUM", "DOTDIFF", "DOTMUL", "DOTDIV",
           "ADDASSIGN", "DIFFASSIGN",
           "MULASSIGN", "DIVASSIGN", "LEQ", "GEQ", "NEQ", "EQ", "COMMENT", "ID"]

t_ignore = ' \t'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_REAL_NUMBER(t):
    r"((\+|-|\.)?([0-9]+)(\.[0-9]+)?(\.)?)"
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"\"[a-zA-Z ]*\""
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


def find_index_in_line(line, token):
    line_start = line.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()
