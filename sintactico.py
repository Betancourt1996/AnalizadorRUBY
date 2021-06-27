import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from AnalizadorRUBY.AnalizadorRuby import tokens

def p_sentencias(p):
    """sentencias : impresion
                    | argumento
                    | puts"""
def p_sentencias_if(p):
    '''sentencias : IF LPAREN condicional RPAREN sentencias END
                  | IF LPAREN condicional RPAREN THEN sentencias END'''
#BETANCOURT COMIENZA____________________________________________________________________________________________
def p_impresion(p):
    '''impresion : PRINT LPAREN argumento RPAREN
                  | PRINT argumento
                  | PRINT LPAREN RPAREN
                  | PRINT '''

def p_puts(p):
    '''puts : PUTS LPAREN argumento RPAREN
                  | PUTS argumento
                  | PUTS LPAREN RPAREN
                  | PUTS '''
def p_condicional(p):
    '''condicional : factor MAYORQUE factor
                   | factor MENORQUE factor
                   | factor MAYORIGUALQUE factor
                   | factor MENORIGUALQUE factor
                   | factor IGUALQUE factor
                   | factor DIFERENTEQUE factor
                   | factor ANDLOGICO factor
                   | factor ORLOGICO factor'''
#BETANCOURT TERMINA_________________________________________________________________________________
def p_argumento(p):
    '''argumento : expression
                  | cadena
                  | condicional'''
def p_argumento_cadena(p):
    '''cadena : STRING
               | STRINGCC'''
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_var(p):
    'factor : ID'
    p[0] = p[1]
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)