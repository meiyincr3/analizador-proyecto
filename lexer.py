#Grupo 2

import ply.lex as lex

resultado_lexico = []

reservadas = {
  # Inicio Meiyin Chang
  'print': 'PRINT',
  'switch':'SWITCH',
  'case': 'CASE',
  'SplStack':'STACK',
  'push' : 'PUSH',
  'pop' : 'POP',
  'rewind' : 'REWIND',
  'valid' : 'VALID',
  'current' : 'CURRENT',
  'next' : 'NEXT',
  'foreach' : 'FOREACH',
  'as' : 'AS',
  'fgets': 'FGETS',
  
  # Fin Meiyin Chang 

  # Inicio Diego Martinez
  'function' : 'FUNCTION', 
  'if': 'IF', 
  'else': 'ELSE',
  'SplQueue' : 'QUEUE',
  'new': 'NEW',
  'enqueue': 'ENQUEUE',
  'dequeue': 'DEQUEUE',
  'count': 'COUNT',
  'valid': 'VALID',
  'elseif':'ELSEIF',
  'return' : 'RETURN',
  'namefunction' : 'NAMEFUNCTION',
  # Fin Diego Martinez

  # Inicio Irving Macias
  'echo' :'ECHO',
  'while': 'WHILE', 
  'for': 'FOR',
  'array':'ARRAY',
  'break' : 'BREAK',
  'default': 'DEFAULT',
  'strlen' : 'STRLEN',
  'array_shift' : 'ARRAY_SHIFT', 
  'in_array' : 'IN_ARRAY',
  'array_push' : 'ARRAY_PUSH'
  # Fin Irving Macias

}

# Secuencia de tokens
tokens = (
 #Inicio Irving Macias
  'IDENTIFICADOR',
  'LETRAS',
  'ENTERO',
  'FLOTANTE',
  'SUMA',
  'RESTA',
  'POTENCIA',
  'IDENTICO',
  'NOIDENTICO', 
  'COMA',
  #Fin Irving Macias

  #Inicio Diego Martinez
  'PARENIZ',
  'PARENDER',
  'ASIGNAR',
  'INCREMENTO',
  'DECREMENTO',
  'PUNTOCOMA',
  'OPERADOR',
  'LLAVEIZ',
  'LLAVEDER',
  'MULT',
  'MAYORQUE',
  'MAYORIGUALQUE',
  'FLUJOS',
  #Fin Diego Martinez

  # Inicio Meiyin Chang
  'IGUAL',
  'MENORQUE',
  'MENORIGUALQUE',
  'DOSPUNTOS',
  'COMENTARIO',
  'MODULO',
  'DIVISIONENTERA',
  'BOOLEAN',
  'CADENA',
  'AND',
  'OR',
  'FLECHASIMPLE',
  'CORCHETEIZ',
  'CORCHETEDER',
  'DIVISION', 
  # Fin Meiyin Chang
 ) + tuple(reservadas.values())

# Expresiones Regulares simples para símbolos
#Inicio Irving Macias
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_POTENCIA = r'\*\*'
t_ASIGNAR = r'='
t_IDENTICO = r'==='
t_NOIDENTICO = r'\!=='
t_LLAVEIZ = r'\{'
t_LLAVEDER = r'\}'
#Fin Irving Macias

#Inicio Diego Martinez
t_PARENIZ = r'\('
t_PARENDER = r'\)'
t_DIVISION = r'\/'
t_IGUAL = r'=='
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'
t_PUNTOCOMA = r';'
t_COMA = r','
t_CORCHETEIZ = r'\['
t_CORCHETEDER = r'\]'
#Fin Diego Martinez

# Inicio Meiyin Chang
t_MAYORQUE = r'>'
t_MAYORIGUALQUE = r'>='
t_MENORQUE = r'<'
t_MENORIGUALQUE = r'<='
t_DOSPUNTOS = r':'
t_MODULO = r'%'
t_DIVISIONENTERA = r'//'
t_FLECHASIMPLE = r'\-\>'
t_AND = r'&&'
t_OR = r'\|\|'
# Fin Meiyin Chang

#Si se repiten caracteres es mejor utilizar una funcion
# Expresión regular para números, incluye cast

# Inicio Meiyin Chang


def t_OPERADOR(t):
    r'and|or|AND|OR'
    return t

def t_BOOLEAN(t):
    r'True|False'
    return t

def t_FLUJOS(t):
    r'STDIN'
    return t


def t_FLOTANTE(t):
  r'\d+\.\d+'
  return t

def t_ENTERO(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_CADENA(t):
    r'("[^"]*"|\'[^\']*\')'
    t.type = reservadas.get(t.value, "CADENA")
    return t

def t_COMENTARIO(t):
    r'(\/\/.*)|(\#.*)'
    return t

def t_NAMEFUNCTION(t):
    r'([a-zA-Z_]\w*)(?=\()'
    t.type = reservadas.get(t.value, "NAMEFUNCTION")
    return t

def t_IDENTIFICADOR(t):
  r'\$[a-zA-Z_]\w*'
  t.type = reservadas.get(t.value,'IDENTIFICADOR')
  return t

def t_LETRAS(t):
  r'[a-zA-Z_]\w*'
  t.type = reservadas.get(t.value,'LETRAS')
  return t

# Expresión regular para reconocer saltos de línea
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# Ignorar espacios, tabulaciones
t_ignore = ' \t'


# Manejo de errores
def t_error(t):
    mensaje_error = f"ERROR: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}"
    print(mensaje_error)
    resultado_lexico.append(mensaje_error)
    t.lexer.skip(1)

#---------------------------COMENTAR PERO SE USA, NO BORRAR------------------
"""
# Construye el lexer
lexer = lex.lex()

# Código para analizar
code = '''if 4 > var:
if 4 % 2:
if 4 // 2:
mivar = 3 + 4 * 10.8 + "hola"
  + -20 * 7 
'''

codei = '''
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
function saludar($nombre) {
	echo "Hola, " . $nombre;
}
saludar("Juan");
echo $mensaje;
    '''

codeDiego = '''
// Definir dos números
$numero1 = 10;
$numero2 = 20;

// Ejemplo de uso:
$stack = new SplStack();

$fibonacci = array();

// Comprobar cuál número es mayor
if ($numero1 > $numero2 and  $numero1 > $numero2) {
    echo "El número $numero1 es mayor que el número $numero2";
} elseif ($numero2 > $numero1) {
    echo "El número $numero2 es mayor que el número $numero1";
} else {
    echo "Ambos números son iguales";
} &&
||
or
and
->
HOLA
name()
while ($contador <= 5) {
'''

# Enviando el código
#ingresa = input("Ingrese: ")
#print(ingresa)
#lexer.input(ingresa)
lexer.input(codeDiego)
#lexer.input(codei)

# Tokenizar
for token in lexer:
  print(token)

"""
#-------------------------SE USA PARA PRUEBAS---------------------


# Build the lexer object

def analisis_lexico(data):
    global resultado_lexema
    validador = lex.lex() 
    validador.input(data)

    resultado_lexico.clear()
    # Tokenize
    while True:
        tok = validador.token()
        if not tok:
            break  # No more input
        if not hasattr(tok, 'type'):
            continue  # Si el token no tiene tipo, es un mensaje de error
        estado = "Linea: {:4} Tipo: {:16} Valor: {:16} Posicion: {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexico.append(estado)
    return resultado_lexico

print("Análisis lexico terminado... :)")