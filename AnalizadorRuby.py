import ply.lex as lex
from ply.lex import TOKEN
# List of token names.   This is always required
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'while' : 'WHILE',
    #empieza BETANCOURT-----------------------------
    'alias' : 'ALIAS',
    'and' : 'AND',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
    'print' : 'PRINT',
    #'defined?' : 'DEFINED?', #error
    'do' : 'DO',
    'elsif' : 'ELSIF',
    'end' : 'END',
    'ensure' : 'ENSURE',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'for' : 'FOR',
    'in' : 'IN',
    'module' : 'MODULE',
    'next' : 'NEXT',
    'nil' : 'NIL',
    'not' : 'NOT',
    'or' : 'OR',
    'redo' : 'REDO',
    'rescue' : 'RESCUE',
    'retry' : 'RETRY',
    'return' : 'RETURN',
    'self' : 'SELF',
    'super' : 'SUPER',
    'undef' : 'UNDEF',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'yield' : 'YIELD',
    '_FILE_' : '_FILE_',
    '_LINE_' : '_LINE_',
    'puts' :'PUTS'
    #termina BETANCOURT -----------------------------
}
tokens = (
    'NUMBER',
#    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'ID',
#BETANCOURT----------------------------- Caracteres de escape
    'SALTOLINEA',
    'CONCATSTR',
    'CADENATEXTO',
    'CONTROLX',
    'ESCAPES',
    'SALTOPAGINA',
    'METACONTROLX',
    'NOTACIONOCTAL',
    'RETORNO',
    'ESPACIOBLANCO',
    'FICHAS',
    'PESTANAVERTICAL',
    'CARACTERX',
    'NOTACIONHEXA',
    'STRING',
    'STRINGCC',
    'DOBLEPUNTO',
    'EQUALS',
    #TERMINA---------------------------------------------------
    #VIVANCO---------------------------------------------------

    'IGUALQUE',
    'DIFERENTEQUE',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUALQUE',
    'MENORIGUALQUE',
    'SPACESHIP',
    'IGUALDADESTRICTA',
    'ANDLOGICO',
    'ORLOGICO',
    'NEGACION',
    'ASIGNACION',
    'ASIGNACIONSUMA',
    'ASIGNACIONRESTA',
    'ASIGNACIONPRODUCTO',
    'ASIGNACIONDIVISION',
    'ASIGNACIONMODULO',
    'ASIGNACIONEXPONENCIAL'

    #TERMINA----------------------------------------------------



) + tuple(reserved.values())
# Regular expression rules for simple tokens
#t_FLOAT = r'\d+\.\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'

#EMPIEZA REGLAS CARACTERES ESPECIALES BETANCOURT---------------
t_SALTOLINEA = r'\\n'
t_CONCATSTR = r'\\a'
t_CADENATEXTO = r'\\b'
t_CONTROLX = r'\\cx'
t_ESCAPES = r'\\e'
t_SALTOPAGINA = r'\\f'
t_METACONTROLX = r'\\m-\\cx'
t_NOTACIONOCTAL = r'\\nnn'
t_RETORNO = r'\\r'
t_ESPACIOBLANCO = r'\\s'
t_FICHAS = r'\\t'
t_PESTANAVERTICAL = r'\\v'
t_CARACTERX = r'\\x'
t_NOTACIONHEXA = r'\\xnn'
t_STRING = '\'.*\''
t_STRINGCC = '".*"'
t_DOBLEPUNTO = '\.\.'
t_EQUALS = "\="
#termina caracteres especiales---------------------------
#VIVANCO REGLAS SIMBOLOS --------------------------------
t_IGUALQUE = r'=='
t_DIFERENTEQUE = r'!='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_MAYORIGUALQUE = r'\>='
t_MENORIGUALQUE = r'\<='
t_SPACESHIP = r'\<=>'
t_IGUALDADESTRICTA = r'==='
t_ANDLOGICO = r'&&'
t_ORLOGICO = r'\|\|'
t_NEGACION = r'!'
t_ASIGNACION = r'='
t_ASIGNACIONSUMA = r'\+='
t_ASIGNACIONRESTA = r'-='
t_ASIGNACIONPRODUCTO = r'\*='
t_ASIGNACIONDIVISION = r'\='
t_ASIGNACIONMODULO = r'%='
t_ASIGNACIONEXPONENCIAL = r'\*\*='



#EMPIEZA Betancourt-----------------------------------------------------------------------------
#variables en ruby
empiezaVarRuby = r'(@|\$|@@)?'
nondigit = r'([_A-Za-z])'
variableRuby = empiezaVarRuby+nondigit+r'[\w]*'
@TOKEN(variableRuby)#Reconoce variables ruby ãlgo @@algo @algo
#TERMINA Betancourt-----------------------------------------------------------------------------

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define a rule so we can track line numbers

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
def t_COMMENT(t):
    r'\#.*'
    pass
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
# linea=" "
# while linea!="":
#     linea=input(">>")
#     lexer.input(linea)
#     getTokens(lexer)
# # Tokenize
# print("Succesfull")