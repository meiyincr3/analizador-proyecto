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
  # Fin Meiyin Chang
  #Inicio Irving Macias
  'default' : 'DEFAULT',
  'break' : 'BREAK',
  'continue' : 'CONTINUE',
  'goto' : 'GOTO',
  'endif' : 'ENDIF',
  #Fin Irving Macias
  #Inicio Diego Martinez
  'do': 'DO',
  'case': 'CASE',
  'die' : 'DIE',
  'exit': 'EXIT',
  'endfor' : 'ENDFOR',
  'enforeach' : 'ENDFOREACH',
  #Fin Diego Martinez


  #Data Structures
  # Inicio Meiyin Chang
  'array':'ARRAY',
  'SplStack':'STACK',
  'SplQueue' : 'QUEUE',
  'push': 'PUSH',
  'pop' : 'POP',
  # Fin Meiyin Chang
  #Inicio Irving Macias
  'SplFixedArray': 'FIXEDARRAY',
  'SplObjectStorage': 'OBJECTSTORAGE',
  'contains' :'CONTAINS',
  'attach' : 'ATTACH',
  #Fin Irving Macias
  #Inicio Diego Martinez
  'current' : 'CURRENT',
  'SplPriorityQueue' : 'PRIORITYQUEUE',
  'SplMaxHeap' : 'MAXHEAP',
  'SplMinHeap' : 'MINHEAP',
  'SplHeap' : 'HEAP',
  #Fin Diego Martinez


  #More Words
  # Inicio Meiyin Chang
  'and':'AND',
  'or':'OR',
  'echo':'ECHO',
  'class':'CLASS',
  'function':'FUNCTION',
  'try':'TRY', 
  'true':'TRUE',
  'false':'FALSE',
  'print' : 'PRINT',
  # Fin Meiyin Chang 
  #Inicio Irving Macias
  'new' : 'NEW',
  'public' : 'PUBLIC',
  'return' : 'RETURN',
  'xor' : 'XOR',
  #Fin Irving Macias  
  #Inicio Diego Martinez
  'catch':'CATCH',
  'switch':'SWITCH',
  'extends' : 'EXTENDS',
  'static' : 'STATIC',
  'declare' : 'DECLARE',
  'namefunction' : 'NAMEFUNCTION',
  #Fin Diego Martinez   
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
  'ANDEQUAL',
  'DOUBLECOLON',
  'RBRACKET',
  'LBRACKET',
  'APOSTROPHE',
  'COMMA',
  'DOT',
  'DOLLARSIGN',
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
  'STRING',
  'CURLYLEFTBRACKET',
  'CURLYRIGHTBRACKET',
  # Fin Meiyin Chang
) + tuple(reserved.values())

# Expresiones Regulares simples para símbolos
#Inicio Irving Macias
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_POWERBY = r'\*\*'
t_ASSINGMENT = r'='
t_IDENTICAL = r'==='
t_NOTIDENTICAL = r'\!=='
#Fin Irving Macias


#Inicio Diego Martinez
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DIVIDE = r'\/'
t_EQUALS = r'=='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_SEMICOLON = r';'
t_ANDEQUAL = r'&='
t_DOUBLECOLON = r'::'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_APOSTROPHE = r'\''
t_COMMA = r','
t_DOT = r'\.'
#Fin Diego Martinez

# Inicio Meiyin Chang
t_DOLLARSIGN = r'\$'
t_GREATERTHAN = r'>'
t_GREATERTHANEQ = r'>='
t_LESSTHAN = r'<'
t_LESSTHANEQ = r'<='
t_COLON = r':'
t_MODULE = r'%'
t_INTDIVIDE = r'//'
t_ARROW = r'=\>'
t_SIMPLEARROW = r'-\>'
t_CURLYLEFTBRACKET = r'{'
t_CURLYRIGHTBRACKET = r'}'
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

def t_STRING(t):
  r'"[^"]*"'
  t.value = str(t.value)
  return t

def t_TRUE(t):
    r'(True)'
    t.type = reserved.get(t.value, 'TRUE')
    t.value = bool(t.value)
    return t

def t_FALSE(t):
    r'(False)'
    t.type = reserved.get(t.value, 'FALSE')
    t.value = bool(t.value)
    return t



def t_IF(t):
    r'if'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_ARRAY(t):
    r'array'
    return t
def t_SORT(t):
    r'sort'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_FOR(t):
    r'for'
    return t
def t_AND(t):
    r'(and|\&\&)'
    return t
def t_OR(t):
    r'(or|\|\|)'
    return t

def t_TRY(t):
    r'try'
    return t
def t_EXCEPTION(t):
    r'exception'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_CATCH(t):
    r'catch'
    return t
#Inicio Diego Martinez
def t_FUNCTION(t):
    r'function'
    return t

def t_NAMEFUNCTION(t):
    r'([a-zA-Z_]\w*)(?=\()'
    return t

def t_ECHO(t):
    r'echo'
    return t


#Fin Diego Martinez

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

code_meiyin = '''
#esto es un comentario
$mensaje = "Hola, mundo";
function saludar($nombre) {
	echo "Hola, " . $nombre;
}
saludar("Juan");
echo $mensaje;
    '''

codigoDiego = '''
// Definir dos números
$numero1 = 10;
$numero2 = 20;

// Comprobar cuál número es mayor
if ($numero1 > $numero2) {
    echo "El número $numero1 es mayor que el número $numero2";
} elseif ($numero2 > $numero1) {
    echo "El número $numero2 es mayor que el número $numero1";
} else {
    echo "Ambos números son iguales";
}

'''

# Enviando el código
#ingresa = input("Ingrese: ")
#print(ingresa)
#lexer.input(ingresa)
lexer.input(algoritmoIrving)


# Tokenizar
for token in lexer:
  print(token)
