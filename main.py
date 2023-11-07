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
  'BOOLEANT',
  'BOOLEANF',
  'CADENA',
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
#Fin Diego Martinez

# Inicio Meiyin Chang
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

def t_CADENA(t):
    r'\'[\w\W\s]*\'|"[\w\W\s]*\"'
    t.value = str(t.value)
    return t
def t_BOOLEANT(t):
    r'(True)'
    t.type = reserved.get(t.value, 'BOOLEANT')
    t.value = bool(t.value)
    return t
def t_BOOLEANF(t):
    r'(False)'
    t.type = reserved.get(t.value, 'BOOLEANF')
    t.value = bool(t.value)
    return t
def t_NFUNCION(t):
    r'[a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'NFUNCION')  # Check for reserved words
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

def t_ECHO(t):
    r'echo'
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

code_meiyin = '''
$mensaje = "Hola, mundo";
$numeros_ejemplo = [10, 5, 7, 21, 3, 15];
function saludar($nombre) {
	echo "Hola, " . $nombre;
}


saludar("Juan");
echo $mensaje;
    '''

# Enviando el código
#ingresa = input("Ingrese: ")
#print(ingresa)
#lexer.input(ingresa)
lexer.input(code_meiyin)


# Tokenizar
for token in lexer:
  print(token)
