import ply.yacc as sint
from lexer import tokens

def p_sentence(p):
  '''sentence : print
              | assignment
              | input
              | function
              | return'''

# Inicio Meiyin Chang
def p_assignment(p):
  "assignment : IDENTIFIER ASSINGMENT values SEMICOLON"

def p_print(p):
  '''print : PRINT LPAREN values RPAREN SEMICOLON
        | PRINT value SEMICOLON'''

def p_print_sinvalor(p):
  "print : PRINT LPAREN RPAREN SEMICOLON"

def p_input(p):
  '''input : FGETS LPAREN RPAREN SEMICOLON'''

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
# Fin  Meiyin Chang

'''
#Inicio Irving Macias
def p_array(p):
    "ARRAY : NEW ARRAY LPAREN INTEGER RPAREN"
  

#Stack methods
def p_stack(p):
  " STACK :  NEW STACK LPAREN RPAREN"

# métodos de la pila
# Ejemplo: $_pila1 -> push(2);
def p_op_stack(p):
  " op_stack : DOLLARSIGN STRING MINUS GREATERTHAN operad_stack"
'''
# push:añade, pop:elimina, count:cuenta, current:muestra el valor
#def p_operad_stack(p):
  #''' operad_stack : PUSH LPAREN values PAREN_DER SEMICOLON 
        #          | POP LPAREN RPAREN SEMICOLON
         #         | COUNT LPAREN RPAREN SEMICOLON
          #        | CURRENT LPAREN RPAREN SEMICOLON
  #'''
#Fin Irving Macias


#Inicio Diego Martinez

#FUNCIONES
#declaracion de una funcion
def p_function_declaration(p):
    "function : FUNCTION NAMEFUNCTION LPAREN parameter RPAREN CURLYLEFTBRACKET"

#Declaracion de un parametro
def p_parameter(p):
   '''parameter : IDENTIFIER
                | IDENTIFIER COMMA parameter
'''

#llamada a una funcion
def p_function_call(p):
    "function : NAMEFUNCTION LPAREN parameter RPAREN"

# return 
def p_return(p):
  " return : RETURN IDENTIFIER SEMICOLON"


#Fin de Diego Martinez


def p_error(p):
  print("Error de sintaxis")

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
