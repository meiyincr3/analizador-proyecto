#Grupo 2

import ply.lex as lex

reserved = {
    # Inicio Meiyin Chang 
    #Control Structures
    'if': 'IF', 
    'else': 'ELSE', 
    'elseif':'ELSEIF',
    'while': 'WHILE', 
    'for': 'FOR',
    'foreach':'FOREACH',
    'switch':'SWITCH',
    'do': 'DO',
    'case': 'CASE',
     # Fin Meiyin Chang
     #Inicio Irving Macias
     'default' : 'DEFAULT',
     'break' : 'BREAK',
     'continue' : 'CONTINUE',
     'goto' : 'GOTO',
     'endif' : 'ENDIF',
     'endfor' : 'ENDFOR',
     'enforeach' : 'ENDFOREACH',
     #Fin Irving Macias
    #Data Structures
    # Inicio Meiyin Chang
    'array':'ARRAY',
    'SplStack':'STACK',
    'SplQueue' : 'QUEUE',
    'push': 'PUSH',
    'pop' : 'POP',
    'current' : 'CURRENT',
    # Fin Meiyin Chang
    #Inicio Irving Macias
    'SplFixedArray': 'FIXEDARRAY',
    'SplObjectStorage': 'OBJECTSTORAGE',
    'contains' :'CONTAINS',
    'attach' : 'attach',
    #Fin Irving Macias
    #More Words
    # Inicio Meiyin Chang
    'and':'AND',
    'or':'OR',
    'echo':'ECHO',
    'class':'CLASS',
    'function':'FUNCTION',
    'try':'TRY',
    'catch':'CATCH',
    'switch':'SWITCH', 
     # Fin Meiyin Chang 
     #Inicio Irving Macias
     'new' : 'NEW',
     'public' : 'PUBLIC',
     'return' : 'RETURN',
     'xor' : 'XOR',
     #Fin Irving Macias     
    }


# Secuencia de tokens
tokens = (
  #Inicio Irving Macias
    'IDENTIFIER',
    'INTEGER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'POWERBY',
    'ASSIGMENT',
    'STRICT',
    'NSTRICT'
  #Fin Irving Macias
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
  # Inicio Meiyin Chang
    'GREATERTHAN',
    'EGREATERTHAN',
    'LESSTHAN',
    'ELESSTHAN',
    'COLON',
    'MODULE',
    'DIVIDE',
  # Fin Meiyin Chang
)+tuple(reserved.values())

# Expresiones Regulares simples para símbolos
#Inicio Irving Macias
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWERBY = r'\*\*'
t_ASSIGMENT = r'='
t_STRICT = r'==='
t_NSTRICT = r'!=='
#Fin Irving Macias
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'=='
# Inicio Meiyin Chang
t_GREATERTHAN = r'>'
t_EGREATERTHAN = r'>='
t_LESSTHAN = r'<'
t_ELESSTHAN = r'<='
t_COLON = r':'
t_MODULE = r'%'
t_DIVIDE = r'//'
# Fin Meiyin Chang


#t_FLOTANTE = r'\d+\.\d+'

#Si se repiten caracteres es mejor utilizar una funcion
# Expresión regular para números, incluye cast
def t_IDENTIFIER(t):
  r'\$[a-z_]\w*'
  t.type = reserved.get(t.value,'IDENTIFIER')
  return t


def t_FLOAT(t):
  r'\d+\.\d+'
  return t


def t_INTEGER(t):
  r'\d+'
  t.value = int(t.value)
  return t



# Expresión regular para reconocer saltos de línea
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# Ignorar espacios, tabulaciones
t_ignore = ' \t'


# Manejo de errores
def t_error(t):
  print(
      f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}"
  )
  t.lexer.skip(1)


# Construye el lexer
lexer = lex.lex()

# Código para analizar
code = '''if 4 > var:
if 4 % 2:
if 4 // 2:
mivar = 3 + 4 * 10.8 + hola
  + -20 * 7
  
'''

# Enviando el código
ingresa = input("Ingrese: ")
print(ingresa)
lexer.input(ingresa)



# Tokenizar
for token in lexer:
  print(token)
