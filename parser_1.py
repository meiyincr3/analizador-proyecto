import ply.yacc as sint
from lexer import tokens

def p_sentence(p):
  '''sentence : print
              | assignment'''

# Inicio Meiyin Chang
def p_assignment(p):
  "assignment : IDENTIFIER ASSINGMENT value SEMICOLON"


def p_print(p):
  '''print : PRINT LBRACKET values RBRACKET SEMICOLON
        | PRINT values SEMICOLON'''


def p_print_sinvalor(p):
  "print : PRINT LBRACKET RBRACKET"


def p_values(p):
  '''values : value
          | value COMMA values'''


def p_value(p):
  '''value : INTEGER
          | FLOAT
          | IDENTIFIER'''
# Fin  Meiyin Chang

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
