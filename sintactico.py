import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from AnalizadorRUBY.AnalizadorRuby import tokens

def p_sentencias(p):
    """sentencias : impresion
                    | argumento
                    | puts
                    | asignacion"""

#BETANCOURT COMIENZA____________________________________________________________________________________________
def p_sentencias_if(p):
    '''sentencias : IF LPAREN condicional RPAREN sentencias END
                  | IF LPAREN condicional RPAREN THEN sentencias END
                  | IF LPAREN condicional RPAREN  sentencias elseifanidado ELSE sentencias END'''
def p_sentencias_unless(p):
    '''sentencias : UNLESS LPAREN condicional RPAREN sentencias END
                  | UNLESS LPAREN condicional RPAREN THEN sentencias END
                  | UNLESS LPAREN condicional RPAREN sentencias elseifanidado  ELSE sentencias END'''
def p_asignacion(p):
    '''asignacion : ID EQUALS variable
                  | ID LCORCHETE NUMBER RCORCHETE EQUALS iterable'''
def p_empty(p):
    'empty :'
    pass

def p_elseifanidado(p):
    '''elseifanidado : ELSEIF sentencias
                    | ELSEIF sentencias elseifanidado
                    | empty'''

def p_sentencias_until(p):
    '''sentencias : UNTIL LPAREN condicional RPAREN DO sentencias END
                      | UNTIL  condicional  DO sentencias END
                      | UNTIL LPAREN condicional RPAREN  sentencias END
                      | UNTIL  condicional   sentencias END'''
def p_sentencias_case(p):
    '''sentencias : CASE expression whenMuchos END
                  | CASE expression whenMuchos ELSE sentencias END'''
def p_whenMuchos(p):
    '''whenMuchos : WHEN rangeYespression sentencias
                  | WHEN rangeYespression sentencias whenMuchos
                  | empty'''
def p_rangeYexpression(p):
    '''rangeYespression : range
                        | expression'''
def p_sentencias_while(p):
    '''sentencias : WHILE LPAREN condicional RPAREN DO sentencias END
                      | WHILE  condicional  DO sentencias END
                      | WHILE LPAREN condicional RPAREN  sentencias END
                      | WHILE  condicional   sentencias END'''
def p_sentencias_for(p):
    '''sentencias : FOR ID IN iterable sentencias END
                  | FOR ID IN iterable DO sentencias END'''
def p_impresion(p):
    '''impresion : PRINT LPAREN argumento RPAREN
                  | PRINT argumento
                  | PRINT LPAREN RPAREN
                  | PRINT '''

def p_puts(p):
    '''puts : PUTS LPAREN argumento RPAREN END
                  | PUTS argumento
                  | PUTS LPAREN RPAREN
                  | PUTS '''
def p_variable(p):
    '''variable : condicional
                | cadena
                | expression
                | iterable'''
def p_dato(p):
    '''dato : NUMBER
            | cadena
            | boolean'''
def p_argumento(p):
    '''argumento : variable'''
def p_iterable(p):
    '''iterable : range
                | array
                | hash'''
def p_array(p):
    'array : LCORCHETE valorArray RCORCHETE'

def p_valorArray(p):
    '''valorArray : dato COMA valorArray
                  | dato '''
def p_hash(p):
    'hash : LLLAVE claveValor RLLAVE'
def p_claveValor(p):
    '''claveValor : cadena DOSPUNTOS variable COMA claveValor
                  | cadena DOSPUNTOS variable
                  | NUMBER DOSPUNTOS variable COMA claveValor
                  | NUMBER DOSPUNTOS variable '''
def p_range(p):
    '''range : expression DOBLEPUNTO expression'''
#REGLAS PARA DEFINIR BOOLEANOS----------------------------------------------
def p_condicional(p):
    '''condicional : logicalOperation'''
def p_logicalOperation(p):
    'logicalOperation : logicalOperation logicalOp logicalOperation'
def p_logicalOp(p):
    '''logicalOp : AND
                | OR'''
def p_logicalOperation_logicalValue(p):
    '''logicalOperation : boolean
                        | ID'''
def p_boolean(p):
    '''boolean : TRUE
               | FALSE
               | exprBool
               | NEGACION boolean'''
#REGLAS QUE DEVUELVEN BOOLEANOS
def p_exprBool_boolOperation(p):
    'exprBool : exprBool boolOperator exprBool'

def p_boolOperator(p):
    '''boolOperator :  MAYORQUE
                   |  MENORQUE
                   |  MAYORIGUALQUE
                   |  MENORIGUALQUE
                   |  IGUALQUE
                   |  DIFERENTEQUE
                   |  ANDLOGICO
                   |  ORLOGICO '''
def p_exprBool_notBool(p):
    'exprBool : factor'
# BETANCOURT TERMINA_________________________________________________________________________________
def p_cadena(p):
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
def p_factor_float(p):
    'factor : FLOAT'
    p[0] = p[1]
def p_factor_var(p):
    'factor : ID'
    p[0] = p[1]
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
strErr=""
def p_error(p):
    print("Syntax error in input!")
    global strErr
    strErr="Error"
# Build the parser
def buildLSemantico(s):
    global strErr
    strErr = ""
    parser = yacc.yacc()
    result = parser.parse(s)

    return result,strErr

