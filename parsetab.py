
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDEQUAL APOSTROPHE ARRAY ARROW ASSINGMENT ATTACH BREAK CASE CATCH CLASS COLON COMMA COMMENTS CONTAINS CONTINUE COUNT CURLYLEFTBRACKET CURLYRIGHTBRACKET CURRENT DECLARE DECREMENT DEFAULT DIE DIVIDE DO DOLLARSIGN DOT DOUBLECOLON ECHO ELSE ELSEIF ENDFOR ENDFOREACH ENDIF EQUALS EXIT EXTENDS FALSE FGETS FIXEDARRAY FLOAT FOR FOREACH FUNCTION GOTO GREATERTHAN GREATERTHANEQ HEAP IDENTICAL IDENTIFIER IF INCREMENT INTDIVIDE INTEGER LBRACKET LESSTHAN LESSTHANEQ LPAREN MAXHEAP MINHEAP MINUS MODULE NAMEFUNCTION NEW NOTIDENTICAL OBJECTSTORAGE OR PLUS POP POWERBY PRINT PRIORITYQUEUE PUBLIC PUSH QUEUE RBRACKET RETURN RPAREN SEMICOLON SIMPLEARROW STACK STATIC STRING SWITCH TIMES TRUE TRY WHILE XORsentence : print\n              | assignment\n              | input\n              | function\n              | returnassignment : IDENTIFIER ASSINGMENT values SEMICOLONprint : PRINT LPAREN values RPAREN SEMICOLON\n        | PRINT value SEMICOLONprint : PRINT LPAREN RPAREN SEMICOLONinput : FGETS LPAREN RPAREN SEMICOLONvalues : value\n          | value COMMA valuesvalue : INTEGER\n          | FLOAT\n          | IDENTIFIER\n          | TRUE\n          | FALSE\n          | STRINGfunction : FUNCTION NAMEFUNCTION LPAREN parameter RPAREN CURLYLEFTBRACKETparameter : IDENTIFIER\n                | IDENTIFIER COMMA parameter\nfunction : NAMEFUNCTION LPAREN parameter RPAREN return : RETURN IDENTIFIER SEMICOLON'
    
_lr_action_items = {'PRINT':([0,],[7,]),'IDENTIFIER':([0,7,12,13,21,24,32,38,43,],[8,17,25,17,17,34,34,17,34,]),'FGETS':([0,],[9,]),'FUNCTION':([0,],[10,]),'NAMEFUNCTION':([0,10,],[11,23,]),'RETURN':([0,],[12,]),'$end':([1,2,3,4,5,6,29,35,37,39,40,42,44,48,],[0,-1,-2,-3,-4,-5,-8,-23,-9,-6,-10,-22,-7,-19,]),'LPAREN':([7,9,11,23,],[13,22,24,32,]),'INTEGER':([7,13,21,38,],[15,15,15,15,]),'FLOAT':([7,13,21,38,],[16,16,16,16,]),'TRUE':([7,13,21,38,],[18,18,18,18,]),'FALSE':([7,13,21,38,],[19,19,19,19,]),'STRING':([7,13,21,38,],[20,20,20,20,]),'ASSINGMENT':([8,],[21,]),'RPAREN':([13,15,16,17,18,19,20,22,26,28,33,34,41,45,47,],[27,-13,-14,-15,-16,-17,-18,31,36,-11,42,-20,46,-12,-21,]),'SEMICOLON':([14,15,16,17,18,19,20,25,27,28,30,31,36,45,],[29,-13,-14,-15,-16,-17,-18,35,37,-11,39,40,44,-12,]),'COMMA':([15,16,17,18,19,20,28,34,],[-13,-14,-15,-16,-17,-18,38,43,]),'CURLYLEFTBRACKET':([46,],[48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentence':([0,],[1,]),'print':([0,],[2,]),'assignment':([0,],[3,]),'input':([0,],[4,]),'function':([0,],[5,]),'return':([0,],[6,]),'value':([7,13,21,38,],[14,28,28,28,]),'values':([13,21,38,],[26,30,45,]),'parameter':([24,32,43,],[33,41,47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentence","S'",1,None,None,None),
  ('sentence -> print','sentence',1,'p_sentence','parser_1.py',5),
  ('sentence -> assignment','sentence',1,'p_sentence','parser_1.py',6),
  ('sentence -> input','sentence',1,'p_sentence','parser_1.py',7),
  ('sentence -> function','sentence',1,'p_sentence','parser_1.py',8),
  ('sentence -> return','sentence',1,'p_sentence','parser_1.py',9),
  ('assignment -> IDENTIFIER ASSINGMENT values SEMICOLON','assignment',4,'p_assignment','parser_1.py',13),
  ('print -> PRINT LPAREN values RPAREN SEMICOLON','print',5,'p_print','parser_1.py',16),
  ('print -> PRINT value SEMICOLON','print',3,'p_print','parser_1.py',17),
  ('print -> PRINT LPAREN RPAREN SEMICOLON','print',4,'p_print_sinvalor','parser_1.py',20),
  ('input -> FGETS LPAREN RPAREN SEMICOLON','input',4,'p_input','parser_1.py',23),
  ('values -> value','values',1,'p_values','parser_1.py',26),
  ('values -> value COMMA values','values',3,'p_values','parser_1.py',27),
  ('value -> INTEGER','value',1,'p_value','parser_1.py',30),
  ('value -> FLOAT','value',1,'p_value','parser_1.py',31),
  ('value -> IDENTIFIER','value',1,'p_value','parser_1.py',32),
  ('value -> TRUE','value',1,'p_value','parser_1.py',33),
  ('value -> FALSE','value',1,'p_value','parser_1.py',34),
  ('value -> STRING','value',1,'p_value','parser_1.py',35),
  ('function -> FUNCTION NAMEFUNCTION LPAREN parameter RPAREN CURLYLEFTBRACKET','function',6,'p_function_declaration','parser_1.py',68),
  ('parameter -> IDENTIFIER','parameter',1,'p_parameter','parser_1.py',72),
  ('parameter -> IDENTIFIER COMMA parameter','parameter',3,'p_parameter','parser_1.py',73),
  ('function -> NAMEFUNCTION LPAREN parameter RPAREN','function',4,'p_function_call','parser_1.py',78),
  ('return -> RETURN IDENTIFIER SEMICOLON','return',3,'p_return','parser_1.py',82),
]
