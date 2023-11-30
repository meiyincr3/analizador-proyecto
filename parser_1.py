import ply.yacc as sint

from lexer import tokens


# Operaciones aritmeticas

def p_operaciones(p):
   ''' operaciones : operacion
                    | operacion operadorAritmetico operaciones 
                    | IDENTIFICADOR ASIGNAR operaciones'''

def p_operacionAritmentica(p):
   ''' operacion : variable operadorAritmetico variable
   '''

def p_operadorAritmetico(p):
    '''operadorAritmetico : SUMA
						  | RESTA
						  | MULT
						  | DIVISION
              | DIVISIONENTERA
						  | MODULO
						  | POTENCIA
	'''
    
  #INICIO MEIYIN CHANG
# Impresion
def p_print(p):
  '''print : PRINT PARENIZ valores PARENDER PUNTOCOMA
        | PRINT valor PUNTOCOMA'''

def p_print_sinvalor(p):
  "print : PRINT PARENIZ PARENDER PUNTOCOMA"

# Fin Meiyin Chang

#-------------ESTRUCTURAS DE CONTROL-----------------------

def p_estructurasControl(p):
  '''estructurasControl : while
                        | for
                        | if
                        | foreach
                        | switch
  '''


def p_foreach(p):
  ''' foreach : FOREACH PARENIZ IDENTIFICADOR AS IDENTIFICADOR PARENDER LLAVEIZ'''
#foreach ($numeros as $numero) {

def p_switch(p):
  ''' switch : SWITCH PARENIZ valor PARENDER LLAVEIZ casos DEFAULT DOSPUNTOS echo LLAVEDER
  '''
#switch ($color) { case "rojo": echo "El color es rojo."; break;default:echo "El color no es rojo, verde ni azul.";}
#switch ($color) { case "rojo": echo "El color es rojo."; break;case "azul": echo "El color es azul."; break;default:echo "El color no es rojo, verde ni azul.";}
#switch ($color) { case "rojo": echo "El color es rojo."; break;case "azul": echo "El color es azul."; break;case "verde": echo "El color es verde."; break;default:echo "El color no es rojo, verde ni azul.";}


def p_casos(p):
  ''' casos : caso 
             | caso casos
  '''

def p_caso(p):
  ''' caso : CASE valor DOSPUNTOS echo BREAK PUNTOCOMA
  '''

#----------------ESTRUCTURA DE DATOS--------------------

# $queue = new SplQueue(); 
def p_estructurasDeDatos(p):
  '''estructurasDeDatos : queue
                  | stack
                  | array
                  '''

# STACK 
# Incio Meiyin

# $stack->push("Deanna");
def p_stackPush(p):
  ''' stack : IDENTIFICADOR FLECHASIMPLE PUSH PARENIZ valor PARENDER PUNTOCOMA'''

# $stack = new SplStack();
def p_stack(p):
  ''' stack : IDENTIFICADOR ASIGNAR NEW STACK PARENIZ PARENDER PUNTOCOMA'''

#Avanzar
# $stack->next();
def p_stackAvanzar(p):
  " stack : IDENTIFICADOR FLECHASIMPLE NEXT PARENIZ PARENDER PUNTOCOMA"

#Situa el puntero al principio de la pila En este caso, debido a que SplStack es LIFO 
# $stack->rewind();
def p_stackPunteroPrincipio(p):
  " stack : IDENTIFICADOR FLECHASIMPLE REWIND PARENIZ PARENDER PUNTOCOMA"

# Mostrar elemento actual de la cola
# $stack->current();
def p_stackActual(p):
  " stack : IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA"

# Comprobar si en la cola aun hay elementos
# $stack->valid()
def p_stackValido(p):
  " stack : IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER"

# Fin Meiyin

def p_error(p):
    try:
        if p:
            print(f"Error de sintaxis en la línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}'")
        else:
            print("Error de sintaxis: entrada inesperada al final del archivo")
    except Exception as e:
        # Manejar cualquier excepción no esperada y mostrar un mensaje genérico
        print(f"Error inesperado: {str(e)}")


# Build the parser
parser = sint.yacc()

while True:
  try:
    s = input('prueba > ')
    #s = code_meiyin
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)