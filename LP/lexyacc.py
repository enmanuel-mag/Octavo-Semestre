
import ply.yacc as yacc
import ply.lex as lex

reserved = {
  'select': 'SELECT',
  'from': 'FROM',
  'where': 'WHERE',
  'and': 'AND',
  'or': 'OR'
}

tokens = (
  'ID',
  'EQ',
  'NE',
  'GT',
  'LT',
  'AT',
  'CM',
  'LP',
  'RP'
) + tuple(reserved.values())

t_EQ=R'\='
t_NE=R'\!='
t_GT=R'\>'
t_LT=R'\<'
t_AT=R'\*'
t_CM=R'\,'
t_LP=R'\('
t_RP=R'\)'

def t_ID(t):
  R'\w+'
  t.type = reserved.get(t.value, 'ID')
  return t

t_ignore = ' \t'

def t_error(t):
  print("Illegal character ", t)
  t.lexer.skip(1)

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

lexer = lex.lex()

data = '''
SELECT vP FROM fo WHERE (cP>rE OR BB=Vn AND (CR!=f9) AND K1!=qZ) AND (R7>=Ve)
'''
lexer.input(data)

while True:
  tok = lexer.token()
  if not tok:
    break
  #print(tok)

def p_sqlstg(p):
  '''sqlstg : SELECT field FROM body
  '''

def p_field(p):
  '''field : AT
           | ID
           | morefield 
  '''

def p_morefield(p):
  '''morefield : ID 
               | ID CM morefield
  '''

def p_body(p):
  '''body : ID
          | ID WHERE wbody
  '''

def p_wbody(p):
  '''wbody : cond
           | cond op wbody
  '''

def p_cond(p):
  '''cond : ID comp ID
          | LP wbody RP
  '''

def p_op(p):
  '''op : AND
        | OR
  '''

def p_comp(p):
  '''comp : EQ
          | NE
          | GT
          | LT
  '''

parser = yacc.yacc()

while True:
  try:
    data = input('SQL>>> ')
  except EOFError as e:
    print(e)
    break
  if not data: continue
  result = parser.parse(data)
  print(result)
