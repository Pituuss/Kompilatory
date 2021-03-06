
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "right=left+-left*/NUMBER REAL_NUMBER STRING VARstart : EXPRESSION\n             | start EXPRESSIONEXPRESSION : NUMBEREXPRESSION : VAREXPRESSION : VAR '=' EXPRESSIONEXPRESSION : EXPRESSION '+' EXPRESSION\n                  | EXPRESSION '-' EXPRESSIONEXPRESSION : EXPRESSION '*' EXPRESSION\n                  | EXPRESSION '/' EXPRESSIONEXPRESSION : '(' EXPRESSION ')'"
    
_lr_action_items = {'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,],[3,3,-1,-3,-4,3,-2,3,3,3,3,3,-6,-7,-8,-9,-5,-10,]),'VAR':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,],[4,4,-1,-3,-4,4,-2,4,4,4,4,4,-6,-7,-8,-9,-5,-10,]),'(':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,],[5,5,-1,-3,-4,5,-2,5,5,5,5,5,-6,-7,-8,-9,-5,-10,]),'$end':([1,2,3,4,6,13,14,15,16,17,18,],[0,-1,-3,-4,-2,-6,-7,-8,-9,-5,-10,]),'+':([2,3,4,6,12,13,14,15,16,17,18,],[7,-3,-4,7,7,-6,-7,-8,-9,7,-10,]),'-':([2,3,4,6,12,13,14,15,16,17,18,],[8,-3,-4,8,8,-6,-7,-8,-9,8,-10,]),'*':([2,3,4,6,12,13,14,15,16,17,18,],[9,-3,-4,9,9,9,9,-8,-9,9,-10,]),'/':([2,3,4,6,12,13,14,15,16,17,18,],[10,-3,-4,10,10,10,10,-8,-9,10,-10,]),')':([3,4,12,13,14,15,16,17,18,],[-3,-4,18,-6,-7,-8,-9,-5,-10,]),'=':([4,],[11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'EXPRESSION':([0,1,5,7,8,9,10,11,],[2,6,12,13,14,15,16,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> EXPRESSION','start',1,'p_start','scanner.py',59),
  ('start -> start EXPRESSION','start',2,'p_start','scanner.py',60),
  ('EXPRESSION -> NUMBER','EXPRESSION',1,'p_expression_number','scanner.py',68),
  ('EXPRESSION -> VAR','EXPRESSION',1,'p_expression_var','scanner.py',73),
  ('EXPRESSION -> VAR = EXPRESSION','EXPRESSION',3,'p_expression_assignment','scanner.py',83),
  ('EXPRESSION -> EXPRESSION + EXPRESSION','EXPRESSION',3,'p_expression_sum','scanner.py',89),
  ('EXPRESSION -> EXPRESSION - EXPRESSION','EXPRESSION',3,'p_expression_sum','scanner.py',90),
  ('EXPRESSION -> EXPRESSION * EXPRESSION','EXPRESSION',3,'p_expression_mul','scanner.py',98),
  ('EXPRESSION -> EXPRESSION / EXPRESSION','EXPRESSION',3,'p_expression_mul','scanner.py',99),
  ('EXPRESSION -> ( EXPRESSION )','EXPRESSION',3,'p_expression_group','scanner.py',107),
]
