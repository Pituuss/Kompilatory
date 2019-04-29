#!/usr/bin/python

import ply.yacc as yacc

import scanner

tokens = scanner.tokens
line = ""

vector_buff = []
vector_flag = False

precedence = (
    ("right", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", '<', '>', 'EQ', 'NEQ', 'GEQ', 'LEQ'),
    ("left", '+', '-'),
    ("left", 'DOTSUM', 'DOTSUB'),
    ("left", '*', '/'),
    ("left", 'DOTMUL', 'DOTDIV'),
    ('right', '\''),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')"
              .format(p.lineno, scanner.find_tok_column(line, p), p.type, p.value))
    else:
        print("Unexpected end of input")


def p_mul_expressions(_p):
    """mul_expressions : expression
                       | expression mul_expressions"""


def p_expression(_p):
    """expression : code_block
                  | base_expr
                  | base_expr ';'
                  | if_statement
                  | loop"""


def p_base_expr(_p):
    """base_expr : assignment
                 | return
                 | print"""


def p_operation(_p):
    """operation : num
                 | unary_operation
                 | function"""


def p_code_block(_p):
    """code_block : '{' mul_expressions '}'"""


def p_PRINT(_p):
    """print : PRINT print_body"""


def p_print_body(_p):
    """print_body : STRING
                  | cond
                  | print_body ',' cond"""


def p_RETURN(_p):
    """return : RETURN cond
              | RETURN"""


def p_vector(_p):
    """vector : '[' vector_body ']'"""


def p_vector_body(_p):
    """vector_body : num
                   | vector_body ',' num
                   | empty"""


def p_matrix(_p):
    """matrix : '[' matrix_body ']'"""


def p_matrix_body(_p):
    """matrix_body : vector
                   | matrix_body ',' vector
                   | empty"""


def p_num(_p):
    """num : NUMBER
           | REAL_NUMBER
           | VAR"""


def p_range(_p):
    """range : VAR '[' int_num_VAR ',' int_num_VAR ']'"""


def p_function(_p):
    """function : function_name '(' num ')'"""


def p_function_name(_p):
    """function_name : ONES
                | EYE
                | ZEROS"""


def p_cond(_p):
    """cond : cmp"""


def p_loop(_p):
    """loop : while
            | for"""


def p_while(_p):
    """while : WHILE '(' cond ')' loop_body"""


def p_for(_p):
    """for : FOR VAR '=' int_num_VAR ':' int_num_VAR loop_body"""


def p_loop_body(_p):
    """loop_body : loop_expr
                 | loop_expr ';'
                 | '{' mul_loop_expr '}'"""


def p_loop_expr(_p):
    """loop_expr : base_expr
                 | loop
                 | if_loop_statement
                 | BREAK
                 | CONTINUE"""


def p_mul_loop_expr(_p):
    """mul_loop_expr : mul_loop_expr loop_body
                     | loop_body"""


def p_if_statement(_p):
    """if_statement : IF '(' cond ')' expression else_statement"""


def p_else_statement(_p):
    """else_statement : ELSE expression
                      | empty"""


def p_if_loop_statement(_p):
    """if_loop_statement : IF '(' cond ')' loop_body else_loop_statement"""


def p_else_loop_statement(_p):
    """else_loop_statement : ELSE loop_body
                      | empty"""


def p_empty(_p):
    """empty : """


def p_assignee(_p):
    """assignee : VAR
                | range"""


def p_ASSIGN(_p):
    # TODO zamienić na expression pojedyncza produkcja
    """assignment : assignee '=' matrix
                  | assignee '=' STRING
                  | assignee '=' operation"""


def p_ADDASSIGN(_p):
    """assignment : assignee ADDASSIGN operation"""


def p_SUBASSIGNt(_p):
    """assignment : assignee SUBASSIGN operation"""


def p_MULASSIGN(_p):
    """assignment : assignee MULASSIGN operation"""


def p_DIVASSIGN(_p):
    """assignment : assignee DIVASSIGN operation"""


def p_int_num_VAR(_p):
    """int_num_VAR : NUMBER
                   | VAR"""


def p_unary_operation(_p):
    """unary_operation : neg_num
                | transpose"""


def p_neg(_p):
    """neg_num : '-' num"""


def p_transpose(_p):
    """transpose : VAR '\\'' """


def p_operation_sum(_p):
    """operation : operation '+' operation
                 | operation '-' operation"""


def p_operation_DOTSUM_DOTSUB(_p):
    """operation : operation DOTSUM operation
                 | operation DOTSUB operation"""


def p_operation_MUL_DIV(_p):
    """operation : operation '*' operation
                 | operation '/' operation"""


def p_operation_DOTMUL_DOTDIV(_p):
    """operation : operation DOTMUL operation
                 | operation DOTDIV operation"""


def p_operation_CMP(_p):
    """cmp : operation '<' operation
           | operation '>' operation"""


def p_operation_cmp_eq(_p):
    """cmp : operation EQ operation
           | operation NEQ operation"""


def p_operation_cmp_geq(_p):
    """cmp : operation GEQ operation
           | operation LEQ operation"""


def p_operation_group(_p):
    """operation : '(' operation ')'"""


parser = yacc.yacc()
