import ply.lex as lex

sym_tab = {}

literals = ['+', '-', '*', '/', '(', ')', '=', '<', '>', '\'', ',', '', ':', ';']

tokens = ("ID", "REAL_NUMBER", "NUMBER", "STRING", "DOTSUM", "DOTDIFF", "DOTMUL", "DOTDIV", "ADDASSIGN", "DIFFASSIGN",
          "MULASSIGN", "DIVASSIGN", "LEQ", "GEQ", "NEQ", "EQ", "IF", "ELSE", "FOR", "WHILE", "BREAK",
          "CONTINUE", "EYE", "ZEROS", "ONES", "PRINT", "RETURN", "COMMENT")

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t):
    #    line = t.value.lstrip()
    #    i = line.find("\n")
    #    line = line if i == -1 else line[:i]
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r"[a-zA-Z_]\w*"
    return t


def t_REAL_NUMBER(t):
    # r"\f+"
    r"((\+|-)?([0-9]+)(\.[0-9]+)?)"
    # r"((\+|-)?([0-9]+)(\.[0-9]+)?)|((\+|-)?\.?[0-9]+)"
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"\"([^\\']+|\\'|\\\\)*\""
    t.value = t.value[1:-1]
    return t


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
t_IF = r"if"
t_ELSE = r"else"
t_FOR = r"for"
t_WHILE = r"while"
t_BREAK = r"break"
t_CONTINUE = r"continue"
t_EYE = r"eye"
t_ZEROS = r"zeros"
t_ONES = r"ones"
t_PRINT = r"print"
t_RETURN = r"return"

precedence = (
    ("right", '='),
    ("left", '+', '-'),
    ("left", '*', '/'),
)


def p_error(p):
    print("parsing error\n")


def p_start(p):
    """start : EXPRESSION
             | start EXPRESSION"""
    if len(p) == 2:
        print("p[1]=", p[1])
    else:
        print("p[2]=", p[2])


def p_expression_number(p):
    """EXPRESSION : NUMBER"""
    p[0] = p[1]


def p_expression_var(p):
    """EXPRESSION : ID"""
    val = sym_tab.get(p[1])
    if val:
        p[0] = val
    else:
        p[0] = 0
        print("%s not used\n" % p[1])


def p_expression_assignment(p):
    """EXPRESSION : ID '=' EXPRESSION"""
    p[0] = p[3]
    sym_tab[p[1]] = p[3]


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION"""
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ')'"""
    p[0] = p[2]


def find_index_in_line(line, token):
    line_start = line.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()
