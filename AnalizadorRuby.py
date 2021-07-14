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
    'and' : 'AND',
    'case' : 'CASE',
    'print' : 'PRINT',
    'do' : 'DO',
    'elsif' : 'ELSIF',
    'end' : 'END',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'for' : 'FOR',
    'in' : 'IN',
    'or' : 'OR',
    'unless' : 'UNLESS',
    'until' : 'UNTIL',
    'when' : 'WHEN',
    'puts' :'PUTS'
    #termina BETANCOURT -----------------------------
}
tokens = (
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LCORCHETE',
    'RCORCHETE',
    'LLLAVE',
    'RLLAVE',
    'DOSPUNTOS',
    'COMA',
    'ID',
#BETANCOURT----------------------------- Caracteres de escape
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
    'ANDLOGICO',
    'ORLOGICO',
    'NEGACION',
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
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_COMA = r','
t_DOSPUNTOS = r':'
t_LLLAVE = r'{'
t_RLLAVE = r'}'
t_FLOAT = r'\d+\.\d+'
t_NUMBER = r'\d+'
#EMPIEZA REGLAS CARACTERES ESPECIALES BETANCOURT---------------

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
t_ANDLOGICO = r'&&'
t_ORLOGICO = r'\|\|'
t_NEGACION = r'!'



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
    lista=[]
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        lista.append(tok)
    return lista
# Build the lexer
lexer = lex.lex()

def leer(linea):
    lexer.input(linea)
    lista=getTokens(lexer)
    # Tokenize
    print("Succesfull")
    return lista
