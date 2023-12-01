import ply.yacc as sint

from lexer import tokens

resultado_sintactico = []

def p_sentencias(p):
    '''sentencias : bloques
                  | operadorAritmetico
                  '''

def p_bloques(p):
    '''bloques : bloque
               | bloque bloques
               '''

def p_bloque(p):
    '''bloque : impresion
                | asignacion
                | funciones
                | while
                | switch
                | reglasSemanticas
                | operaciones 
                | COMENTARIO
                | longitud
                | LLAVEDER
                | incrementoDecremento
                '''
    
    #operacionesSemantico
    #indexacionSemantica
    
def p_impresion(p):
    '''impresion : print
                | echo
                | input
                '''



def p_funciones(p):
    '''funciones : funcion
                | return
               '''

def p_indexacion(p):
   '''indexacion : IDENTIFICADOR CORCHETEIZ valor CORCHETEDER
                  | IDENTIFICADOR CORCHETEIZ valor CORCHETEDER PUNTOCOMA'''


def p_valores(p):
  '''valores : valor
            | valor COMA valores'''

def p_numero(p):
  '''NUMERO : ENTERO
            | RESTA ENTERO
            | FLOTANTE
  '''
def p_valor(p):
    '''valor : NUMERO
	         | CADENA
	         | BOOLEAN
             | IDENTIFICADOR
             | indexacionSemantica
	'''
#-------------------------Reglas semanticas de comparadores----------------   
def p_comparadorNum(p):
	''' comparadorNum : MAYORQUE
					| MAYORIGUALQUE
					| MENORQUE
					| MENORIGUALQUE
	'''
def p_comparador(p):
	''' comparador : IDENTICO
					| NOIDENTICO
					| IGUAL
	'''
    
def p_variableOperacion(p):
    ''' variable : NUMERO
                  | IDENTIFICADOR
    '''

def p_comparaciones(p):
	''' comparaciones : comparacion  
					 | comparacion operadores comparaciones
	'''

def p_comparacion(p):
	''' comparacion :  variable comparadorNum variable 
            | valor comparador valor 
	'''
#-----------------------Fin de reglas semanticas de comparadores---------------


def p_incrementoDecremento(p):
  '''incrementoDecremento : variable INCREMENTO 
                          | variable DECREMENTO
                          | variable INCREMENTO PUNTOCOMA
                          | variable DECREMENTO PUNTOCOMA
  '''

def p_operadores(p):
   '''operadores : OPERADOR
	         | AND
	         | OR
	'''

def p_longitud(p):
   '''longitud : IDENTIFICADOR ASIGNAR STRLEN PARENIZ valor PARENDER PUNTOCOMA'''

# Operaciones aritmeticas

def p_operaciones(p): # $variable1 + $variable2 - $variable3
   ''' operaciones : operacion
                    | operacion PUNTOCOMA
                    | operacion operadorAritmetico operaciones 
                    | IDENTIFICADOR ASIGNAR operaciones'''

def p_operacion(p): # $variable1 + $variable2
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

# Asignacion
def p_asignacion(p):
    '''asignacion : IDENTIFICADOR ASIGNAR valor PUNTOCOMA
                  | IDENTIFICADOR PUNTOCOMA
                  | IDENTIFICADOR ASIGNAR pop
                  | IDENTIFICADOR ASIGNAR push'''

# Inicio Meiyin
# Impresion
def p_print(p):
  '''print : PRINT PARENIZ valores PARENDER PUNTOCOMA
        | PRINT valor PUNTOCOMA'''

def p_print_sinvalor(p):
  "print : PRINT PARENIZ PARENDER PUNTOCOMA"

def p_input(p):
  "input : IDENTIFICADOR ASIGNAR FGETS PARENIZ FLUJOS PARENDER PUNTOCOMA"


# Fin Meiyin Chang

#Inicio de Irving
def p_echo(p):
  '''echo : ECHO valores PUNTOCOMA
  '''
#Fin de Irving



#INICIO DE DIEGO
#FUNCIONES
#declaracion de una funcion
def p_declaracion_funcion(p):
    "funcion : FUNCTION NAMEFUNCTION PARENIZ parametro PARENDER LLAVEIZ"
# function sumar($numero1, $numero2) {


#Declaracion de un parametro
def p_parametro(p):
   '''parametro : IDENTIFICADOR
                | IDENTIFICADOR COMA parametro
'''

#llamada a una funcion
def p_llamada_funcion(p):
    ''' funcion : NAMEFUNCTION PARENIZ valores PARENDER PUNTOCOMA
                | IDENTIFICADOR ASIGNAR NAMEFUNCTION PARENIZ valores PARENDER PUNTOCOMA
'''

# sumar($valor1, $valor2);
# $suma = sumar($valor1, $valor2);


# return 
def p_return(p):
  " return : RETURN IDENTIFICADOR PUNTOCOMA"
#return $resultado;

#FIN DE DIEGO



#-------------ESTRUCTURAS DE CONTROL-----------------------
def p_estructurasControl(p):
  '''estructurasControl : while
                        | for
                        | if
                        | elseif
                        | else
                        | foreach
                        | switch
                        | caso
                        | default
                        | break
  '''
  #forSemantico
  #whileSemantico
    
    
#Inicio de Irving

# while (9 > 9.75) {
def p_while(p):
	''' while : WHILE PARENIZ comparacionSemantico PARENDER LLAVEIZ 
	'''
   
#for ($i = 2; $i <= 10; $i + 2) {
def p_for(p):
  ''' for : FOR PARENIZ IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA comparacion PUNTOCOMA incrementoDecremento PARENDER LLAVEIZ
  '''
#Fin de Irving


#Inicio Meiyin

def p_foreach(p):
  ''' foreach : FOREACH PARENIZ IDENTIFICADOR AS IDENTIFICADOR PARENDER LLAVEIZ'''
#foreach ($numeros as $numero) {

#def p_switch(p):
  #''' switch : SWITCH PARENIZ valor PARENDER LLAVEIZ casos DEFAULT DOSPUNTOS echo LLAVEDER
  #'''
#switch ($color) { case "rojo": echo "El color es rojo."; break;default:echo "El color no es rojo, verde ni azul.";}
#switch ($color) { case "rojo": echo "El color es rojo."; break;case "azul": echo "El color es azul."; break;default:echo "El color no es rojo, verde ni azul.";}
#switch ($color) { case "rojo": echo "El color es rojo."; break;case "azul": echo "El color es azul."; break;case "verde": echo "El color es verde."; break;default:echo "El color no es rojo, verde ni azul.";}

def p_switch(p):
  ''' switch : SWITCH PARENIZ valor PARENDER LLAVEIZ 
            | casoSemantico
            | break
            | default
  '''

#def p_casos(p):
  #''' casos : caso 
  #           | caso casos
  #'''

def p_caso(p):
  ''' caso : CASE valor DOSPUNTOS 
  '''

def p_break(p):
  ''' break : BREAK PUNTOCOMA
  '''
def p_default(p):
  ''' default : DEFAULT DOSPUNTOS
  '''

#PRUEBAS PARA SWITCH CASE
def p_bloqueSPruebas(p):
    '''bloqueSPruebas : bloquePrueba
                      | bloquePrueba bloqueSPruebas
               '''

def p_bloquePrueba(p):
    '''bloquePrueba : switch 
                    | caso 
                    | echo
                    | break
                    | default
                    | LLAVEDER
               '''


#Fin Meiyin


#INICIO DE DIEGO
def p_if(p):
  ''' if : IF PARENIZ comparaciones PARENDER LLAVEIZ
          | IF PARENIZ IDENTIFICADOR PARENDER LLAVEIZ 
  '''
#if ($edad >= 18) {
#if ($esAdmin) { 

def p_elseif(p):
  ''' elseif : LLAVEDER ELSEIF PARENIZ comparaciones PARENDER LLAVEIZ
          | LLAVEDER ELSEIF PARENIZ IDENTIFICADOR PARENDER LLAVEIZ 
          | ELSEIF PARENIZ comparaciones PARENDER LLAVEIZ
          | ELSEIF PARENIZ IDENTIFICADOR PARENDER LLAVEIZ 
  '''
#} elseif ($numero2 > $numero1) {

def p_else(p):
  ''' else : LLAVEDER ELSE LLAVEIZ
          | ELSE LLAVEIZ
          '''
#} else {
# else {

#FIN DE DIEGO


#------------------------------------------------------






#----------------ESTRUCTURA DE DATOS--------------------
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

# $stack->pop();
def p_stackPop(p):
  ''' stack : IDENTIFICADOR FLECHASIMPLE POP PARENIZ PARENDER PUNTOCOMA'''

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





#INICIO DIEGO MARTINEZ
#QUEUE

# $queue = new SplQueue();
def p_queue(p):
  " queue : IDENTIFICADOR ASIGNAR NEW QUEUE PARENIZ PARENDER PUNTOCOMA"  

#Añadir elementos a la cola
# $queue->enqueue('1');
def p_colaAnadir(p):
  " queue : IDENTIFICADOR FLECHASIMPLE ENQUEUE PARENIZ valor PARENDER PUNTOCOMA"

#Muestra el número de elementos de la cola(3)
# $queue->count();
def p_colaContar(p):
  ''' queue : IDENTIFICADOR FLECHASIMPLE COUNT PARENIZ PARENDER PUNTOCOMA
            | IDENTIFICADOR ASIGNAR IDENTIFICADOR FLECHASIMPLE COUNT PARENIZ PARENDER PUNTOCOMA
  '''

#Saca de la cola el primer elemento y lo muestra
# $queue->dequeue();
# $primerElementoCola = $queue->dequeue();
def p_colaExpulsar(p):
  ''' queue : IDENTIFICADOR FLECHASIMPLE DEQUEUE PARENIZ PARENDER PUNTOCOMA
            | IDENTIFICADOR ASIGNAR IDENTIFICADOR FLECHASIMPLE DEQUEUE PARENIZ PARENDER PUNTOCOMA'''

#Avanzar
# $queue->next();
def p_colaSiguiente(p):
  " queue : IDENTIFICADOR FLECHASIMPLE NEXT PARENIZ PARENDER PUNTOCOMA"

#Situa el puntero al principio de la cola
# $queue->rewind();
def p_colaPunteroPrincipio(p):
  " queue : IDENTIFICADOR FLECHASIMPLE REWIND PARENIZ PARENDER PUNTOCOMA"

# Mostrar elemento actual de la cola
# $queue->current();
# $actual = $cola->current();
def p_colaActual(p):
  ''' queue : IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA
            | IDENTIFICADOR ASIGNAR IDENTIFICADOR FLECHASIMPLE CURRENT PARENIZ PARENDER PUNTOCOMA'''

# Comprobar si en la cola aun hay elementos
# $queue->valid()
# $condicion = $cola->valid();
def p_colaValido(p):
  ''' queue : IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER
            | IDENTIFICADOR ASIGNAR IDENTIFICADOR FLECHASIMPLE VALID PARENIZ PARENDER PUNTOCOMA'''

#FIN DIEGO



#Inicio Irving
#ARRAY
def p_array(p):
  ''' array : IDENTIFICADOR ASIGNAR ARRAY PARENIZ PARENDER PUNTOCOMA
            | IDENTIFICADOR ASIGNAR ARRAY PARENIZ valores PARENDER PUNTOCOMA
            | IDENTIFICADOR ASIGNAR CORCHETEIZ valores CORCHETEDER PUNTOCOMA
  '''
#$arrayNumerico = array(1, 2, 3, 4, 5);
#$arrayNumerico = [1, 2, 3, 4, 5];
#$fibonacci = array();


def p_arrayShift(p):
  ''' array : IDENTIFICADOR ASIGNAR ARRAY_SHIFT PARENIZ IDENTIFICADOR PARENDER PUNTOCOMA
  '''
#$primerElemento = array_shift($miArray);


def p_arrayPush(p):
  ''' array : ARRAY_PUSH PARENIZ IDENTIFICADOR valores PARENDER PUNTOCOMA
            | ARRAY_PUSH PARENIZ IDENTIFICADOR COMA valores PARENDER PUNTOCOMA
  '''
#array_push($miArray, 6, 7);


def p_arrayIn(p):
  ''' array : IDENTIFICADOR ASIGNAR IN_ARRAY PARENIZ valor COMA IDENTIFICADOR PARENDER PUNTOCOMA
  '''
#$existe = in_array(3, $miArray);
#Fin Irving

#----------------------------Reglas Semanticas----------------

def p_reglasSemanticas(p):
  '''reglasSemanticas : whileSemantico
                  | ifSemantico
                  | forSemantico
                  | pop
                  | push
                  | indexacionSemantica
                  | comparacionSemantico
                  '''

#Irving
def p_operacionesSemantico(p): # entero + entero / negativo - negativo + float * float
    '''operacionesSemantico : operacionSemantico
                            | operacionSemantico operadorAritmetico operacionesSemantico'''

def p_operacionSemantico(p):# entero + entero, negativo - negativo, float * float
    '''operacionSemantico : NUMERO operadorAritmetico NUMERO'''


def p_incrementoDecrementoSemantico(p):# $numero++  $numero--
  '''incrementoDecrementoSemantico : IDENTIFICADOR INCREMENTO
                                    | IDENTIFICADOR DECREMENTO
  '''

def p_ifSemantico(p): # if (True or False) {
  ''' ifSemantico : IF PARENIZ booleanosSemantico PARENDER LLAVEIZ
  '''
def p_booleanosSemantico(p):#   True  or False and True
  '''booleanosSemantico : BOOLEAN
                        | BOOLEAN operadores booleanosSemantico
  '''

#Meiyin

def p_push(p):# $var->push($ident)  |   $var->push($ident);
  '''push : IDENTIFICADOR FLECHASIMPLE PUSH PARENIZ IDENTIFICADOR PARENDER
          |  IDENTIFICADOR FLECHASIMPLE POP PARENIZ IDENTIFICADOR PARENDER PUNTOCOMA
  '''

def p_pop(p): # $var->pop()  |   $var->pop();
  '''pop : IDENTIFICADOR FLECHASIMPLE POP PARENIZ PARENDER
          | IDENTIFICADOR FLECHASIMPLE POP PARENIZ PARENDER PUNTOCOMA'''

def p_casoSemantico(p):# case "rojo": | case 1:
  ''' casoSemantico : CASE ENTERO DOSPUNTOS 
                    | CASE CADENA DOSPUNTOS 
  '''

def p_indexacionSemantica(p): # $variable[5]  | $var=$variable[5];
   'indexacionSemantica : IDENTIFICADOR CORCHETEIZ ENTERO CORCHETEDER'


#Diego   

def p_whileSemantico(p): # while(True or False) {
  'whileSemantico : WHILE PARENIZ booleanosSemantico PARENDER LLAVEIZ '

def p_comparacionSemantico(p): # entero > entero, negativo < negativo, flotante >= flotante
	''' comparacionSemantico :  NUMERO comparadorNum NUMERO 
	'''
   
 # for ($i = 0; $i < 5; 5++) //Esto no deberia pasar "5++" pero actualmente esta permitido en el for
def p_forSemantico(p):# for ($i = 0; $i < 5; $i++) {
  '''forSemantico : FOR PARENIZ IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA comparacion PUNTOCOMA incrementoDecrementoSemantico PARENDER LLAVEIZ
  '''

#-----------------------------------------------------


#----------ERRORES PERSONALIZADOS------------
symbol_table = {}  # Inicializar la tabla de símbolos vacía

"""
def p_asignacion(p):
    '''asignacion : IDENTIFICADOR ASIGNAR valor PUNTOCOMA
                  | IDENTIFICADOR ASIGNAR valor
    '''
    variable_name = p[1]
    value = p[3]

    if len(p) < 5:
        error_message = f"Error de sintaxis: Falta el punto y coma en la asignación de '{variable_name}'"
        print(error_message)  # Este mensaje aparece en la consola
        # Agregar el mensaje de error a la lista resultado_sintactico
        resultado_sintactico.append("Error: " + error_message)
    else:
        symbol_table[variable_name] = value
"""



#----------ERRORES PERSONALIZADOS------------
# Imprime errores según las reglas
def p_error(p):
    global bandera
    bandera = True
    print("-----WARNING: ENTRADA AL ERROR Y BANDERA SE HACE TRUE")
    global resultado_sintactico
    #resultado_sintactico.clear()
    if p:
        resultado = "Error sintactico de tipo: {}. Token inesperado: {}. ".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico: {}".format(p)
        print(resultado)
    resultado_sintactico.append(resultado)



code = '''
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
  }
'''

# Build the parser
parser = sint.yacc()

'''
while True:
  try:
    s = input('prueba > ')
    #s = code
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)
'''

def analisis_sintactico2(data):
    linea = 0
    global resultado_sintactico
    resultado_sintactico.clear()
    global bandera

    for item in data.splitlines():
        print("-------------INICIO FOR-------------------")
        bandera = False
        linea += 1
        # print("item: ", item)
        if item:
            print(f"Analizando línea {linea}: {item}")
            gram = parser.parse(item)
            print("ESTADO BANDERA DESPUES DE ANALISIS", bandera)
            # print("gram: ", gram)
            if bandera == False:
                resultado_sintactico.append("Linea: " + str(linea) + "  Info: No hay errores!")
            else:
                resultado_sintactico.append("Error en la linea: " + str(linea))
        else:
            print("data vacia")

    print("result: ", resultado_sintactico)
    return resultado_sintactico


print("Analisis sintactico terminado... :)")