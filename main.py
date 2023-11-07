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
    'ASSINGMENT',
    'IDENTICAL',
    'NOTIDENTICAL', 
    'COMMENTS',
  #Fin Irving Macias

  #Inicio Diego Martinez
    'DIVIDE',   
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'INCREMENT',
    'DECREMENT',
    'SEMICOLON',
    'AND_EQUAL',
    'DOUBLE_COLON',
  #Fin Diego Martinez

  # Inicio Meiyin Chang
    'TIMES',
    'GREATERTHAN',
    'GREATERTHANEQ',
    'LESSTHAN',
    'LESSTHANEQ',
    'COLON',
    'MODULE',
    'INTDIVIDE',
    'ARROW',
    'SIMPLEARROW',

  # Fin Meiyin Chang
)+tuple(reserved.values())

# Expresiones Regulares simples para símbolos
#Inicio Irving Macias
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWERBY = r'\*\*'
t_ASSINGMENT = r'='
t_IDENTICAL = r'==='
t_NOTIDENTICAL = r'!=='
#Fin Irving Macias


#Inicio Diego Martinez
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DIVIDE = r'/'
t_EQUALS = r'=='
t_INCREMENT = r'++'
t_DECREMENT = r'--'
t_SEMICOLON = r';'
t_AND_EQUAL = r'&='
T_DOUBLE_COLON = r'::'
#Fin Diego Martinez

# Inicio Meiyin Chang
t_DIVIDE = r'/'
t_GREATERTHAN = r'>'
t_GREATERTHANEQ = r'>='
t_LESSTHAN = r'<'
t_LESSTHANEQ = r'<='
t_COLON = r':'
t_MODULE = r'%'
t_INTDIVIDE = r'//'
t_ARROW = r'=\>'
t_SIMPLEARROW = r'-\>'
# Fin Meiyin Chang


#t_FLOTANTE = r'\d+\.\d+'

#Si se repiten caracteres es mejor utilizar una funcion
# Expresión regular para números, incluye cast
# Inicio Meiyin Chang
def t_IDENTIFIER(t):
  r'\$[a-zA-Z_]\w*'
  t.type = reserved.get(t.value,'IDENTIFIER')
  return t

def t_FLOAT(t):
  r'\d+\.\d+'
  return t


def t_INTEGER(t):
  r'\d+'
  t.value = int(t.value)
  return t

#Inicio Irving y Meiyin
def t_COMMENTS(t):
  r'(\/\/.*)|(\/\*(.|\s)*\*\/)|(\#.*)'
  return t
#Fin Irving y Meiyin

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

algoritmoIrving = '''
$totalNumeros = 10

$fibonacci = array();
$fibonacci[0] = 0;
$fibonacci[1] = 1;

for ($i = 2; $i < $totalNumeros; $i++) {
    $fibonacci[$i] = $fibonacci[$i - 1] + $fibonacci[$i - 2];
}

// Imprimir la sucesión de Fibonacci
for ($i = 0; $i < $totalNumeros; $i++) {
    echo $fibonacci[$i];
    if ($i < $totalNumeros - 1) {
        echo ', ';
    }
}
'''
# Enviando el código
#ingresa = input("Ingrese: ")
#print(ingresa)
#lexer.input(ingresa)
lexer.input(code)


# Tokenizar
for token in lexer:
  print(token)
