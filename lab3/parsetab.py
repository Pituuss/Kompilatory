
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFnonassocELSEright=SUMASSIGNSUBASSIGNMULASSIGNDIVASSIGNleft<>EQNEQGEQLEQleft+-leftDOTSUMDOTSUBleft*/leftDOTMULDOTDIVleftUNARYMINUSright'BREAK COMMENT CONTINUE DIVASSIGN DOTDIV DOTMUL DOTSUB DOTSUM ELSE EQ EYE FLOAT FOR GEQ ID IF INTEGER LEQ MULASSIGN NEQ ONES PRINT RETURN STRING SUBASSIGN SUMASSIGN WHILE ZEROS\n    program : block\n    \n    block : '{' block '}'\n          | block '{' block '}'\n    \n    block : block instruction\n          | instruction\n    \n    instruction : base_instruction ';'\n                | if_statement\n                | loop_statement\n    \n    base_instruction : assign_expression\n                     | keyword\n    \n    assign_expression : variable assign_op expression\n    \n    variable : ID\n             | tensor_id\n    \n    tensor_id : ID '[' sequence ']'\n    \n    sequence : sequence ',' expression\n            | expression\n    \n    expression : result\n    \n    expression : ID\n    \n    result : INTEGER\n           | FLOAT\n           | STRING\n           | tensor\n           | tensor_id\n    \n    tensor : '[' rows ']'\n    \n    rows : rows ';' sequence\n         | sequence\n    \n    expression : '-' expression %prec UNARYMINUS\n    \n    expression : ID '\\''\n    \n    expression : '(' expression ')' '\\''\n    \n    expression : '(' expression ')'\n    \n    expression : expression '+' expression\n               | expression '-' expression\n               | expression '*' expression\n               | expression '/' expression\n               | expression DOTSUM expression\n               | expression DOTDIV expression\n               | expression DOTMUL expression\n               | expression DOTSUB expression\n    \n    expression : function '(' expression ')'\n    \n    function : EYE\n             | ZEROS\n             | ONES\n    \n    keyword : PRINT sequence\n    \n    keyword : BREAK\n    \n    keyword : CONTINUE\n    \n    keyword : RETURN expression\n    \n    body : instruction\n    \n    body : '{' block '}'\n    \n    relation : expression comp_operator expression\n    \n    expression : relation\n    \n    comp_operator : '>'\n                  | '<'\n                  | EQ\n                  | GEQ\n                  | LEQ\n                  | NEQ\n    \n    if_statement : IF '(' relation ')' body %prec IF\n    \n    if_statement : IF '(' relation ')' body ELSE body\n    \n    loop_statement : while_statement\n                   | for_statement\n    \n    while_statement : WHILE '(' relation ')' body\n    \n    for_statement : FOR ID '=' range body\n    \n    range : expression ':' expression\n    \n    assign_op : '='\n              | SUMASSIGN\n              | DIVASSIGN\n              | SUBASSIGN\n              | MULASSIGN\n    "
    
_lr_action_items = {'{':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[3,22,3,-5,-7,-8,-59,-60,3,-4,22,-6,-17,-18,-50,-19,-20,-21,-22,-23,22,-2,-28,-27,-3,106,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,106,106,-14,-57,-47,3,-29,-39,-61,-62,106,22,-63,-58,-48,]),'IF':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[10,10,10,-5,-7,-8,-59,-60,10,-4,10,-6,-17,-18,-50,-19,-20,-21,-22,-23,10,-2,-28,-27,-3,10,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,10,10,-14,-57,-47,10,-29,-39,-61,-62,10,10,-63,-58,-48,]),'PRINT':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[14,14,14,-5,-7,-8,-59,-60,14,-4,14,-6,-17,-18,-50,-19,-20,-21,-22,-23,14,-2,-28,-27,-3,14,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,14,14,-14,-57,-47,14,-29,-39,-61,-62,14,14,-63,-58,-48,]),'BREAK':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[15,15,15,-5,-7,-8,-59,-60,15,-4,15,-6,-17,-18,-50,-19,-20,-21,-22,-23,15,-2,-28,-27,-3,15,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,15,15,-14,-57,-47,15,-29,-39,-61,-62,15,15,-63,-58,-48,]),'CONTINUE':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[16,16,16,-5,-7,-8,-59,-60,16,-4,16,-6,-17,-18,-50,-19,-20,-21,-22,-23,16,-2,-28,-27,-3,16,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,16,16,-14,-57,-47,16,-29,-39,-61,-62,16,16,-63,-58,-48,]),'RETURN':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[17,17,17,-5,-7,-8,-59,-60,17,-4,17,-6,-17,-18,-50,-19,-20,-21,-22,-23,17,-2,-28,-27,-3,17,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,17,17,-14,-57,-47,17,-29,-39,-61,-62,17,17,-63,-58,-48,]),'WHILE':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[18,18,18,-5,-7,-8,-59,-60,18,-4,18,-6,-17,-18,-50,-19,-20,-21,-22,-23,18,-2,-28,-27,-3,18,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,18,18,-14,-57,-47,18,-29,-39,-61,-62,18,18,-63,-58,-48,]),'FOR':([0,2,3,4,6,7,11,12,22,23,24,25,35,36,40,41,42,43,44,45,54,55,75,76,84,85,87,88,89,90,91,92,93,94,95,96,98,100,101,103,104,105,106,107,108,110,111,113,114,115,116,117,],[19,19,19,-5,-7,-8,-59,-60,19,-4,19,-6,-17,-18,-50,-19,-20,-21,-22,-23,19,-2,-28,-27,-3,19,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,19,19,-14,-57,-47,19,-29,-39,-61,-62,19,19,-63,-58,-48,]),'ID':([0,2,3,4,6,7,11,12,14,17,19,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,40,41,42,43,44,45,49,51,53,54,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,84,85,87,88,89,90,91,92,93,94,95,96,98,99,100,101,103,104,105,106,107,108,110,111,112,113,114,115,116,117,],[20,20,20,-5,-7,-8,-59,-60,36,36,52,20,-4,20,-6,36,36,-64,-65,-66,-67,-68,-17,-18,36,36,-50,-19,-20,-21,-22,-23,36,36,36,20,-2,36,36,36,36,36,36,36,36,36,36,-51,-52,-53,-54,-55,-56,-28,-27,36,36,-3,20,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,36,20,20,-14,-57,-47,20,-29,-39,-61,-62,36,20,20,-63,-58,-48,]),'$end':([1,2,4,6,7,11,12,23,25,55,84,104,105,110,111,116,117,],[0,-1,-5,-7,-8,-59,-60,-4,-6,-2,-3,-57,-47,-61,-62,-58,-48,]),'}':([4,6,7,11,12,23,24,25,54,55,84,104,105,110,111,114,116,117,],[-5,-7,-8,-59,-60,-4,55,-6,84,-2,-3,-57,-47,-61,-62,117,-58,-48,]),';':([5,8,9,15,16,33,34,35,36,40,41,42,43,44,45,50,58,75,76,79,80,86,87,88,89,90,91,92,93,94,95,96,98,103,107,108,109,],[25,-9,-10,-44,-45,-43,-16,-17,-18,-50,-19,-20,-21,-22,-23,-46,-11,-28,-27,99,-26,-15,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,-14,-29,-39,-25,]),'ELSE':([6,7,11,12,25,104,105,110,111,116,117,],[-7,-8,-59,-60,-6,113,-47,-61,-62,-58,-48,]),'(':([10,14,17,18,26,27,28,29,30,31,32,37,38,39,46,47,48,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[26,38,38,51,38,38,-64,-65,-66,-67,-68,38,38,78,-40,-41,-42,38,38,38,38,38,38,38,38,38,38,38,38,38,-51,-52,-53,-54,-55,-56,38,38,38,38,]),'=':([13,20,21,52,103,],[28,-12,-13,82,-14,]),'SUMASSIGN':([13,20,21,103,],[29,-12,-13,-14,]),'DIVASSIGN':([13,20,21,103,],[30,-12,-13,-14,]),'SUBASSIGN':([13,20,21,103,],[31,-12,-13,-14,]),'MULASSIGN':([13,20,21,103,],[32,-12,-13,-14,]),'-':([14,17,26,27,28,29,30,31,32,34,35,36,37,38,40,41,42,43,44,45,49,50,51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,103,107,108,112,115,],[37,37,37,37,-64,-65,-66,-67,-68,61,-17,-18,37,37,-50,-19,-20,-21,-22,-23,37,61,37,37,-50,61,61,37,37,37,37,37,37,37,37,37,37,-51,-52,-53,-54,-55,-56,-28,-27,61,37,-50,37,61,-31,-32,-33,-34,-35,-36,-37,-38,61,-30,61,-24,37,61,-14,-29,-39,37,61,]),'INTEGER':([14,17,26,27,28,29,30,31,32,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[41,41,41,41,-64,-65,-66,-67,-68,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-51,-52,-53,-54,-55,-56,41,41,41,41,]),'FLOAT':([14,17,26,27,28,29,30,31,32,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[42,42,42,42,-64,-65,-66,-67,-68,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-51,-52,-53,-54,-55,-56,42,42,42,42,]),'STRING':([14,17,26,27,28,29,30,31,32,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[43,43,43,43,-64,-65,-66,-67,-68,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-51,-52,-53,-54,-55,-56,43,43,43,43,]),'EYE':([14,17,26,27,28,29,30,31,32,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[46,46,46,46,-64,-65,-66,-67,-68,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-51,-52,-53,-54,-55,-56,46,46,46,46,]),'ZEROS':([14,17,26,27,28,29,30,31,32,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[47,47,47,47,-64,-65,-66,-67,-68,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-51,-52,-53,-54,-55,-56,47,47,47,47,]),'ONES':([14,17,26,27,28,29,30,31,32,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[48,48,48,48,-64,-65,-66,-67,-68,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-51,-52,-53,-54,-55,-56,48,48,48,48,]),'[':([14,17,20,26,27,28,29,30,31,32,36,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,82,99,112,],[49,49,53,49,49,-64,-65,-66,-67,-68,53,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-51,-52,-53,-54,-55,-56,49,49,49,49,]),',':([33,34,35,36,40,41,42,43,44,45,75,76,80,83,86,87,88,89,90,91,92,93,94,95,96,98,103,107,108,109,],[59,-16,-17,-18,-50,-19,-20,-21,-22,-23,-28,-27,59,59,-15,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,-14,-29,-39,59,]),']':([34,35,36,40,41,42,43,44,45,75,76,79,80,83,86,87,88,89,90,91,92,93,94,95,96,98,103,107,108,109,],[-16,-17,-18,-50,-19,-20,-21,-22,-23,-28,-27,98,-26,103,-15,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,-14,-29,-39,-25,]),'+':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[60,-17,-18,-50,-19,-20,-21,-22,-23,60,-50,60,60,-28,-27,60,-50,60,-31,-32,-33,-34,-35,-36,-37,-38,60,-30,60,-24,60,-14,-29,-39,60,]),'*':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[62,-17,-18,-50,-19,-20,-21,-22,-23,62,-50,62,62,-28,-27,62,-50,62,62,62,-33,-34,62,-36,-37,62,62,-30,62,-24,62,-14,-29,-39,62,]),'/':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[63,-17,-18,-50,-19,-20,-21,-22,-23,63,-50,63,63,-28,-27,63,-50,63,63,63,-33,-34,63,-36,-37,63,63,-30,63,-24,63,-14,-29,-39,63,]),'DOTSUM':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[64,-17,-18,-50,-19,-20,-21,-22,-23,64,-50,64,64,-28,-27,64,-50,64,64,64,-33,-34,-35,-36,-37,-38,64,-30,64,-24,64,-14,-29,-39,64,]),'DOTDIV':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[65,-17,-18,-50,-19,-20,-21,-22,-23,65,-50,65,65,-28,-27,65,-50,65,65,65,65,65,65,-36,-37,65,65,-30,65,-24,65,-14,-29,-39,65,]),'DOTMUL':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[66,-17,-18,-50,-19,-20,-21,-22,-23,66,-50,66,66,-28,-27,66,-50,66,66,66,66,66,66,-36,-37,66,66,-30,66,-24,66,-14,-29,-39,66,]),'DOTSUB':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[67,-17,-18,-50,-19,-20,-21,-22,-23,67,-50,67,67,-28,-27,67,-50,67,67,67,-33,-34,-35,-36,-37,-38,67,-30,67,-24,67,-14,-29,-39,67,]),'>':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[69,-17,-18,-50,-19,-20,-21,-22,-23,69,-50,69,69,-28,-27,69,-50,69,-31,-32,-33,-34,-35,-36,-37,-38,69,-30,69,-24,69,-14,-29,-39,69,]),'<':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[70,-17,-18,-50,-19,-20,-21,-22,-23,70,-50,70,70,-28,-27,70,-50,70,-31,-32,-33,-34,-35,-36,-37,-38,70,-30,70,-24,70,-14,-29,-39,70,]),'EQ':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[71,-17,-18,-50,-19,-20,-21,-22,-23,71,-50,71,71,-28,-27,71,-50,71,-31,-32,-33,-34,-35,-36,-37,-38,71,-30,71,-24,71,-14,-29,-39,71,]),'GEQ':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[72,-17,-18,-50,-19,-20,-21,-22,-23,72,-50,72,72,-28,-27,72,-50,72,-31,-32,-33,-34,-35,-36,-37,-38,72,-30,72,-24,72,-14,-29,-39,72,]),'LEQ':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[73,-17,-18,-50,-19,-20,-21,-22,-23,73,-50,73,73,-28,-27,73,-50,73,-31,-32,-33,-34,-35,-36,-37,-38,73,-30,73,-24,73,-14,-29,-39,73,]),'NEQ':([34,35,36,40,41,42,43,44,45,50,56,57,58,75,76,77,81,86,87,88,89,90,91,92,93,94,95,96,97,98,102,103,107,108,115,],[74,-17,-18,-50,-19,-20,-21,-22,-23,74,-50,74,74,-28,-27,74,-50,74,-31,-32,-33,-34,-35,-36,-37,-38,74,-30,74,-24,74,-14,-29,-39,74,]),')':([35,36,40,41,42,43,44,45,56,75,76,77,81,87,88,89,90,91,92,93,94,95,96,97,98,103,107,108,],[-17,-18,-50,-19,-20,-21,-22,-23,85,-28,-27,96,100,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,108,-24,-14,-29,-39,]),':':([35,36,40,41,42,43,44,45,75,76,87,88,89,90,91,92,93,94,95,96,98,102,103,107,108,],[-17,-18,-50,-19,-20,-21,-22,-23,-28,-27,-31,-32,-33,-34,-35,-36,-37,-38,-49,-30,-24,112,-14,-29,-39,]),"'":([36,96,],[75,107,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,3,22,106,],[2,24,54,114,]),'instruction':([0,2,3,22,24,54,85,100,101,106,113,114,],[4,23,4,4,23,23,105,105,105,4,105,23,]),'base_instruction':([0,2,3,22,24,54,85,100,101,106,113,114,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'if_statement':([0,2,3,22,24,54,85,100,101,106,113,114,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'loop_statement':([0,2,3,22,24,54,85,100,101,106,113,114,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'assign_expression':([0,2,3,22,24,54,85,100,101,106,113,114,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'keyword':([0,2,3,22,24,54,85,100,101,106,113,114,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'while_statement':([0,2,3,22,24,54,85,100,101,106,113,114,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'for_statement':([0,2,3,22,24,54,85,100,101,106,113,114,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'variable':([0,2,3,22,24,54,85,100,101,106,113,114,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'tensor_id':([0,2,3,14,17,22,24,26,27,37,38,49,51,53,54,59,60,61,62,63,64,65,66,67,68,78,82,85,99,100,101,106,112,113,114,],[21,21,21,45,45,21,21,45,45,45,45,45,45,45,21,45,45,45,45,45,45,45,45,45,45,45,45,21,45,21,21,21,45,21,21,]),'assign_op':([13,],[27,]),'sequence':([14,49,53,99,],[33,80,83,109,]),'expression':([14,17,26,27,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,78,82,99,112,],[34,50,57,58,76,77,34,57,34,86,87,88,89,90,91,92,93,94,95,97,102,34,115,]),'result':([14,17,26,27,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,78,82,99,112,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'function':([14,17,26,27,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,78,82,99,112,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'relation':([14,17,26,27,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,78,82,99,112,],[40,40,56,40,40,40,40,81,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'tensor':([14,17,26,27,37,38,49,51,53,59,60,61,62,63,64,65,66,67,68,78,82,99,112,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'comp_operator':([34,50,57,58,76,77,86,87,88,89,90,91,92,93,94,95,97,102,115,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'rows':([49,],[79,]),'range':([82,],[101,]),'body':([85,100,101,113,],[104,110,111,116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','Mparser.py',35),
  ('block -> { block }','block',3,'p_implicit_block','Mparser.py',42),
  ('block -> block { block }','block',4,'p_implicit_block','Mparser.py',43),
  ('block -> block instruction','block',2,'p_block','Mparser.py',54),
  ('block -> instruction','block',1,'p_block','Mparser.py',55),
  ('instruction -> base_instruction ;','instruction',2,'p_instruction','Mparser.py',66),
  ('instruction -> if_statement','instruction',1,'p_instruction','Mparser.py',67),
  ('instruction -> loop_statement','instruction',1,'p_instruction','Mparser.py',68),
  ('base_instruction -> assign_expression','base_instruction',1,'p_base_instruction','Mparser.py',75),
  ('base_instruction -> keyword','base_instruction',1,'p_base_instruction','Mparser.py',76),
  ('assign_expression -> variable assign_op expression','assign_expression',3,'p_assign_expression','Mparser.py',83),
  ('variable -> ID','variable',1,'p_variable','Mparser.py',90),
  ('variable -> tensor_id','variable',1,'p_variable','Mparser.py',91),
  ('tensor_id -> ID [ sequence ]','tensor_id',4,'p_tensor_id','Mparser.py',98),
  ('sequence -> sequence , expression','sequence',3,'p_sequence','Mparser.py',105),
  ('sequence -> expression','sequence',1,'p_sequence','Mparser.py',106),
  ('expression -> result','expression',1,'p_expression_result','Mparser.py',117),
  ('expression -> ID','expression',1,'p_expression_id','Mparser.py',124),
  ('result -> INTEGER','result',1,'p_result','Mparser.py',131),
  ('result -> FLOAT','result',1,'p_result','Mparser.py',132),
  ('result -> STRING','result',1,'p_result','Mparser.py',133),
  ('result -> tensor','result',1,'p_result','Mparser.py',134),
  ('result -> tensor_id','result',1,'p_result','Mparser.py',135),
  ('tensor -> [ rows ]','tensor',3,'p_tensor','Mparser.py',142),
  ('rows -> rows ; sequence','rows',3,'p_rows','Mparser.py',150),
  ('rows -> sequence','rows',1,'p_rows','Mparser.py',151),
  ('expression -> - expression','expression',2,'p_expression_minus','Mparser.py',162),
  ("expression -> ID '",'expression',2,'p_transpose_variable','Mparser.py',169),
  ("expression -> ( expression ) '",'expression',4,'p_transpose_expression','Mparser.py',176),
  ('expression -> ( expression )','expression',3,'p_expression_in_parens','Mparser.py',183),
  ('expression -> expression + expression','expression',3,'p_math_expression','Mparser.py',190),
  ('expression -> expression - expression','expression',3,'p_math_expression','Mparser.py',191),
  ('expression -> expression * expression','expression',3,'p_math_expression','Mparser.py',192),
  ('expression -> expression / expression','expression',3,'p_math_expression','Mparser.py',193),
  ('expression -> expression DOTSUM expression','expression',3,'p_math_expression','Mparser.py',194),
  ('expression -> expression DOTDIV expression','expression',3,'p_math_expression','Mparser.py',195),
  ('expression -> expression DOTMUL expression','expression',3,'p_math_expression','Mparser.py',196),
  ('expression -> expression DOTSUB expression','expression',3,'p_math_expression','Mparser.py',197),
  ('expression -> function ( expression )','expression',4,'p_fun_expression','Mparser.py',204),
  ('function -> EYE','function',1,'p_function','Mparser.py',211),
  ('function -> ZEROS','function',1,'p_function','Mparser.py',212),
  ('function -> ONES','function',1,'p_function','Mparser.py',213),
  ('keyword -> PRINT sequence','keyword',2,'p_print','Mparser.py',220),
  ('keyword -> BREAK','keyword',1,'p_break','Mparser.py',227),
  ('keyword -> CONTINUE','keyword',1,'p_continue','Mparser.py',234),
  ('keyword -> RETURN expression','keyword',2,'p_return','Mparser.py',241),
  ('body -> instruction','body',1,'p_body','Mparser.py',248),
  ('body -> { block }','body',3,'p_block_body','Mparser.py',255),
  ('relation -> expression comp_operator expression','relation',3,'p_relation','Mparser.py',262),
  ('expression -> relation','expression',1,'p_relation_expression','Mparser.py',269),
  ('comp_operator -> >','comp_operator',1,'p_comp_operator','Mparser.py',276),
  ('comp_operator -> <','comp_operator',1,'p_comp_operator','Mparser.py',277),
  ('comp_operator -> EQ','comp_operator',1,'p_comp_operator','Mparser.py',278),
  ('comp_operator -> GEQ','comp_operator',1,'p_comp_operator','Mparser.py',279),
  ('comp_operator -> LEQ','comp_operator',1,'p_comp_operator','Mparser.py',280),
  ('comp_operator -> NEQ','comp_operator',1,'p_comp_operator','Mparser.py',281),
  ('if_statement -> IF ( relation ) body','if_statement',5,'p_if_statement','Mparser.py',288),
  ('if_statement -> IF ( relation ) body ELSE body','if_statement',7,'p_if_else_statement','Mparser.py',295),
  ('loop_statement -> while_statement','loop_statement',1,'p_loop_statement','Mparser.py',302),
  ('loop_statement -> for_statement','loop_statement',1,'p_loop_statement','Mparser.py',303),
  ('while_statement -> WHILE ( relation ) body','while_statement',5,'p_while_statement','Mparser.py',310),
  ('for_statement -> FOR ID = range body','for_statement',5,'p_for_statement','Mparser.py',317),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',324),
  ('assign_op -> =','assign_op',1,'p_assign_op','Mparser.py',331),
  ('assign_op -> SUMASSIGN','assign_op',1,'p_assign_op','Mparser.py',332),
  ('assign_op -> DIVASSIGN','assign_op',1,'p_assign_op','Mparser.py',333),
  ('assign_op -> SUBASSIGN','assign_op',1,'p_assign_op','Mparser.py',334),
  ('assign_op -> MULASSIGN','assign_op',1,'p_assign_op','Mparser.py',335),
]
