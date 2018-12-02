
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionCOMMENT EQUAL NAME VALUE WHITESPACE\n        expression : NAME\n                   | NAME EQUAL\n                   | NAME EQUAL VALUE\n        expression : COMMENT'
    
_lr_action_items = {'NAME':([0,],[2,]),'COMMENT':([0,],[3,]),'$end':([1,2,3,4,5,],[0,-1,-4,-2,-3,]),'EQUAL':([2,],[4,]),'VALUE':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> NAME','expression',1,'p_expression_full','parser.py',141),
  ('expression -> NAME EQUAL','expression',2,'p_expression_full','parser.py',142),
  ('expression -> NAME EQUAL VALUE','expression',3,'p_expression_full','parser.py',143),
  ('expression -> COMMENT','expression',1,'p_expression_comment','parser.py',148),
]
