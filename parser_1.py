import ply.yacc as sint
from lexer import tokens

def p_sentencia(p):
  '''sentencia : impresion
              | asignacion
              | mientras'''

def p_asignacion(p):
  "asignacion : IDENTIFICADOR IGUAL valor"

def p_impresion(p):
  "impresion : IMPRESION P_IZQ valores P_DER"


def p_impresion_sinvalor(p):
  "impresion : IMPRESION P_IZQ P_DER"

def p_mientras(p):
  "mientras : MIENTRAS P_IZQ VERDADERO P_DER DOSP sentencia"


def p_valores(p):
  '''valores : valor
          | valor COMA valores'''


def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | IDENTIFICADOR'''


def p_error(p):
  print("Error de sintaxis")


# Build the parser
parser = sint.yacc()

while True:
  try:
    s = input('esp > ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)
