import ply.yacc as yacc

import AST as ast
import MLexer

tokens = MLexer.tokens
line = ""

precedence = (
    ("nonassoc", 'IF'),
    ("nonassoc", 'ELSE'),
    ("right", '=', 'SUMASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", '<', '>', 'EQ', 'NEQ', 'GEQ', 'LEQ'),
    ("left", '+', '-'),
    ("left", 'DOTSUM', 'DOTSUB'),
    ("left", '*', '/'),
    ("left", 'DOTMUL', 'DOTDIV'),
    ("left", 'UNARYMINUS'),
    ('right', '\'')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')"
              .format(p.lineno, MLexer.find_tok_column(p), p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """
    program : block
    """
    p[0] = ast.Program(p[1])


def p_implicit_block(p):
    """
    block : '{' block '}'
          | block '{' block '}'
    """
    if len(p) is 5:
        p[1].children.append(p[3])
        p[0] = p[1]
    else:
        p[0] = ast.Block(p[2])


def p_block(p):
    """
    block : block instruction
          | instruction
    """
    if len(p) is 3:
        p[1].children.append(p[2])
        p[0] = p[1]
    else:
        p[0] = ast.Block(p[1])


def p_instruction(p):
    """
    instruction : base_instruction ';'
                | if_statement
                | loop_statement
    """
    p[0] = p[1]


def p_base_instruction(p):
    """
    base_instruction : assign_expression
                     | keyword
    """
    p[0] = ast.Instruction(p[1])


def p_assign_expression(p):
    """
    assign_expression : variable assign_op expression
    """
    p[0] = ast.Assignment(p[1], p[2], p[3], p.lexer.lineno)


def p_variable(p):
    """
    variable : ID
             | tensor_id
    """
    p[0] = ast.Variable(p[1], p.lexer.lineno)


def p_tensor_id(p):
    """
    tensor_id : ID '[' sequence ']'
    """
    p[0] = ast.TensorID(p[1], p[3], p.lexer.lineno)


def p_sequence(p):
    """
    sequence : sequence ',' expression
            | expression
    """
    if len(p) is 4:
        p[1].expression.append(p[3])
        p[0] = p[1]
    else:
        p[0] = ast.Seq(p[1])


def p_expression_result(p):
    """
    expression : result
    """
    p[0] = p[1]


def p_expression_id(p):
    """
    expression : ID
    """
    p[0] = ast.Variable(p[1], p.lexer.lineno)


def p_result(p):
    """
    result : INTEGER
           | FLOAT
           | STRING
           | tensor
           | tensor_id
    """
    p[0] = ast.Result(p[1])


def p_tensor(p):
    """
    tensor : '[' rows ']'
    """
    p[0] = ast.Tensor(p[2], p.lexer.lineno)


def p_rows(p):
    """
    rows : rows ';' sequence
         | sequence
    """
    if len(p) is 4:
        p[1].row_list.append(p[3])
        p[0] = p[1]
    else:
        p[0] = ast.Rows(p[1])


def p_expression_minus(p):
    """
    expression : '-' expression %prec UNARYMINUS
    """
    p[0] = ast.Negation(p[2])


def p_transpose_variable(p):
    """
    expression : ID '\\''
    """
    p[0] = ast.Transpose(ast.Variable(p[1], p.lexer.lineno))


def p_transpose_expression(p):
    """
    expression : '(' expression ')' '\\''
    """
    p[0] = ast.Transpose(p[2])


def p_expression_in_parens(p):
    """
    expression : '(' expression ')'
    """
    p[0] = p[2]


def p_math_expression(p):
    """
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
               | expression DOTSUM expression
               | expression DOTDIV expression
               | expression DOTMUL expression
               | expression DOTSUB expression
    """
    p[0] = ast.BinaryExpression(p[1], p[2], p[3], p.lexer.lineno)


def p_fun_expression(p):
    """
    expression : function '(' expression ')'
    """
    p[0] = ast.Function(p[1], p[3], p.lexer.lineno)


def p_function(p):
    """
    function : EYE
             | ZEROS
             | ONES
    """
    p[0] = p[1]


def p_print(p):
    """
    keyword : PRINT sequence
    """
    p[0] = ast.Print(p[2], p.lexer.lineno)


def p_break(p):
    """
    keyword : BREAK
    """
    p[0] = ast.Break(p.lexer.lineno)


def p_continue(p):
    """
    keyword : CONTINUE
    """
    p[0] = ast.Continue(p.lexer.lineno)


def p_return(p):
    """
    keyword : RETURN expression
    """
    p[0] = ast.Return(p[2], p.lexer.lineno)


def p_body(p):
    """
    body : instruction
    """
    p[0] = ast.Instruction(p[1])


def p_block_body(p):
    """
    body : '{' block '}'
    """
    p[0] = ast.Instruction(p[2])


def p_relation(p):
    """
    relation : expression comp_operator expression
    """
    p[0] = ast.BinaryExpression(p[1], p[2], p[3], p.lexer.lineno)


def p_comp_operator(p):
    """
    comp_operator : '>'
                  | '<'
                  | EQ
                  | GEQ
                  | LEQ
                  | NEQ
    """
    p[0] = p[1]


def p_if_statement(p):
    """
    if_statement : IF '(' relation ')' body %prec IF
    """
    p[0] = ast.If(p[3], p[5])


def p_if_else_statement(p):
    """
    if_statement : IF '(' relation ')' body ELSE body
    """
    p[0] = ast.If(p[3], p[5], p[7])


def p_loop_statement(p):
    """
    loop_statement : while_statement
                   | for_statement
    """
    p[0] = p[1]


def p_while_statement(p):
    """
    while_statement : WHILE '(' relation ')' body
    """
    p[0] = ast.While(p[3], p[5])


def p_for_statement(p):
    """
    for_statement : FOR ID '=' range body
    """
    p[0] = ast.For(p[2], p[4], p[5])


def p_range(p):
    """
    range : expression ':' expression
    """
    p[0] = ast.Range(p[1], p[3])


def p_assign_op(p):
    """
    assign_op : '='
              | SUMASSIGN
              | DIVASSIGN
              | SUBASSIGN
              | MULASSIGN
    """
    p[0] = p[1]


parser = yacc.yacc()
