import ply.lex as lex
from ply.lex import TOKEN
# List of token names.   This is always required
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    #empieza BETANCOURT-----------------------------
    'alias' : 'ALIAS',
    'and' : 'AND',
    'break' : 'BREAK',
    'case' : 'CASE',
    'class' : 'CLASS',
    'def' : 'DEF',
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
    '_LINE_' : '_LINE_'
    #termina BETANCOURT -----------------------------
}
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'ID',

) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'

#t_EQUALS = r'\='#token asignacion
#EMPIEZA Betancourt-----------------------------------------------------------------------------
#variables en ruby
empiezaVarRuby = r'(@|\$|@@)?'
nondigit = r'([_A-Za-z])'
variableRuby = empiezaVarRuby+nondigit+r'[\w]*'
@TOKEN(variableRuby)#aun valida @@@algo
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
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")