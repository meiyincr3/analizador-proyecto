import ply.yacc as sint
from lexer import tokens

def p_sentence(p):
  '''sentence : print
              | assignment'''

# Inicio Meiyin Chang
def p_assignment(p):
  "assignment : IDENTIFIER ASSINGMENT values SEMICOLON"

def p_print(p):
  '''print : PRINT LBRACKET values RBRACKET SEMICOLON
        | PRINT string_ele SEMICOLON'''

def p_print_sinvalor(p):
  "print : PRINT LBRACKET RBRACKET SEMICOLON"

def p_input(p):
  '''input : FGETS LBRACKET RBRACKET SEMICOLON'''

def p_string_ele(p):
  '''string_ele : STRING'''

def p_values(p):
  '''values : value
          | value COMMA values'''

def p_value(p):
  '''value : INTEGER
          | FLOAT
          | IDENTIFIER
          | TRUE
          | FALSE'''
# Fin  Meiyin Chang

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

# push:añade, pop:elimina, count:cuenta, current:muestra el valor
def p_operad_stack(p):
  ''' operad_stack : PUSH LPAREN values PAREN_DER SEMICOLON 
                  | POP LPAREN RPAREN SEMICOLON
                  | COUNT LPAREN RPAREN SEMICOLON
                  | CURRENT LPAREN RPAREN SEMICOLON
  '''
#Fin Irving Macias

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
