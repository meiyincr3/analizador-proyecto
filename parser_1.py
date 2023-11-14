import ply.yacc as sint
from lexer import tokens

def p_sentence(p):
  '''sentence : print
              | assignment
              | mientras'''

# Inicio Meiyin Chang
def p_assignment(p):
  "assignment : DOLLARSIGN IDENTIFIER ASSINGMENT value"


def p_print(p):
  "print : print LBRACKET values RBRACKET"


def p_print_sinvalor(p):
  "print : print LBRACKET RBRACKET"


def p_while(p):
  "while : WHILE LBRACKET TRUE RBRACKET DOUBLECOLON sentence"


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
