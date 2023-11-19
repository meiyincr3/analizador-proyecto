import ply.yacc as sint
from lexer import tokens

def p_sentence(p):
  '''sentence : print
              | printf
              | assignment
              | input
              | function
              | return
              | echo
              | array
              | stack
              | op_stack
              | operad_stack
              '''

# Inicio Meiyin Chang
def p_assignment(p):
  "assignment : IDENTIFIER ASSINGMENT values SEMICOLON"

def p_print(p):
  '''print : PRINT LPAREN values RPAREN SEMICOLON
        | PRINT value SEMICOLON'''

def p_print_sinvalor(p):
  "print : PRINT LPAREN RPAREN SEMICOLON"

def p_printf_conformato(p):
  "printf : PRINTF LPAREN values RPAREN SEMICOLON"

def p_input(p):
  '''input : FGETS LPAREN values RPAREN SEMICOLON'''

def p_values(p):
  '''values : value
          | value COMMA values'''

def p_value(p):
  '''value : INTEGER
          | FLOAT
          | IDENTIFIER
          | TRUE
          | FALSE
          | STRING'''
  
def p_echo(p):
  '''echo : ECHO STRING SEMICOLON'''
  
# Fin  Meiyin Chang

#Inicio Irving Macias
def p_array(p):
    "array : IDENTIFIER ASSINGMENT ARRAY LPAREN INTEGER RPAREN SEMICOLON"
  # $array =  new holiboli(232);
  # $array = array(232);


#Stack methods
def p_stack(p):
    "stack : IDENTIFIER ASSINGMENT NEW STACK LPAREN RPAREN SEMICOLON"
  # $stack = new stack();

# métodos de la pila
# Ejemplo: $_pila1 -> push(2);
def p_op_stack(p):
  " op_stack : IDENTIFIER MINUS GREATERTHAN operad_stack"

# push:añade, pop:elimina, count:cuenta, current:muestra el valor
def p_operad_stack(p):
  '''operad_stack : PUSH LPAREN values RPAREN SEMICOLON 
                  | POP LPAREN RPAREN SEMICOLON
                  | COUNT LPAREN RPAREN SEMICOLON
                  | CURRENT LPAREN RPAREN SEMICOLON
  '''
#Fin Irving Macias


#Inicio Diego Martinez

#FUNCIONES
#declaracion de una funcion
def p_function_declaration(p):
    "function : FUNCTION NAMEFUNCTION LPAREN parameter RPAREN CURLYLEFTBRACKET"
# function sumar($numero1, $numero2) {


#Declaracion de un parametro
def p_parameter(p):
   '''parameter : IDENTIFIER
                | IDENTIFIER COMMA parameter
'''
# $numero1, $numero2, ... 

#llamada a una funcion
def p_function_call(p):
    ''' function : NAMEFUNCTION LPAREN parameter RPAREN SEMICOLON
                | IDENTIFIER ASSINGMENT NAMEFUNCTION LPAREN parameter RPAREN SEMICOLON
'''
# sumar($valor1, $valor2);
# $suma = sumar($valor1, $valor2);


# return 
def p_return(p):
  " return : RETURN IDENTIFIER SEMICOLON"
# return $resultado;


code = '''
function sumar($numero1, $numero2) {
    $resultado = $numero1 + $numero2;
    return $resultado;
}

// Uso de la función
$valor1 = 5;
$valor2 = 3;
$suma = sumar($valor1, $valor2);
echo "La suma de $valor1 y $valor2 es: $suma"; // Esto imprimirá "La suma de 5 y 3 es: 8"
    '''

#Fin de Diego Martinez


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
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)
