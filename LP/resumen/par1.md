
## Lenguaje de programacion
Es un conjunto de simbolos y palabras (vob lexico) y conjunto de reglas sintacas y smeantics que permiten escribir un algoritmo. Algoritmo es una secuencia de instrucicon finitas.

## Criterios para evular un LP
- readability: facilidad de leer y mantener el codigo
- abstraction: permitir manjejod e tipo de datos si conocer su implementacion
- comunity: personas que colaboran y proponen mejoras en el LP
- consistency: que no debe dar posibilidad a errores tipos y que siga una estandarizacion
- compatibility: capacidad de integracion con otras tecnologias, framework
- popularity: factor que afeta la oferta y demanda
- portability: que funciona en diferentes plattaformas y dispositivos
- writeability: tiene mucha relacion el aprendizaje, facilidd y simplicidad al codear
- orthogonality: permite la combinacion de conceptos y paradigmas
- expressivity: permite escribir de difenrtes formas
- realability: manejo de excepciones y tipado fuerte
- maintenability: capacidad para facilitar mejoras y correciones

## Paradigmas de Programación
### Imperativo
Consisten enn una secesion de instrucciones o conjunto de sentencias, como si el programador diera ordenes concrets. 
- modular
- estrocturada
- procedeimental
- orientada a objetos

### Declaritivo
No necesita definir algoritmos puesto que describe el problema en lugar de encontrar una solucion al mismo. Este paradigma utilizar el principio del razonamiento logico para responder a las preguntas o cuestiones consultadas. ProLog, Scala, Lisp

	
## Análisis Léxico
Es el proceso de analizar el conjutno de simbolos y palabras para convertirlos a token, que despues se analizaran en el analsiis sintatico. 
Verifica que las cadenas sean validad, que las palabras formen parte del lenguaje.

> charact stream -> token stream

## Expresiones regulares
Es una cadena de texto, que define un patron de coincidencia con una sintaxis muy epecifica para realizar busquedas de texto, ayudan a definir tokens

## Análisis Sintáctico
BFN: Backus-Naur Form, es un metalenguaje usado para expresar gramtias libres de contexto (sintaxis). Tiene simbolso temrinales, no terminales y reglas de produccion (repeticion)
Verifica que el orden de los tokens (gramatica) sea el correcto para el lenguaje de programacion

> token strem -> parse tree (syntax analysis)

### Árbol Sintáctico
El parse tree señala la relacion entre lso diferentes componentes (tokens) a traves de un arbol

### Derivaciones
Secuencia de reemplazos de "nombres" de estructua por seleccion en lso lados derchos de las reglas gramaticales. Es la construccion de la regla gramatical

Permite mostrar grficamente como se puede derivar cualquier cadena de un lenguaje a partir del simbolo distinguido de una gramatica que genera ese lenaugje. Es la representacion de un BFN en un arbol
	
## Análisis Semántico
Utilizar el arbon sintactico, para identifcar los operadores y operandos epxresiones y proporciones. Un compoente del analsisi semnatico es la verificacion de tipos. Esto es verificar que cada operador tenga operandos permitidos
Verifica el sentido o significado de la expresion

> parse tree -> semantic analys and intermeate code generation (anotation tree)

### Árbol de Anotaciones
Nace del analisis semantico, es un arbon sintactico con anotaciones, con el valor, tipo y demas metainfo del token

### Tipado de Datos
Define una coleciond evalores yun conjutno de operaciones predefinidas para esos valores
Los programas dan resultados operando datos, existen dos tipos de datos primitivos y los estructurados (estatico y dinamico)
- tipado debil: no es necesario delcarar el tipo de dato de una variable
- tipado fuerte: si todos los erroes de tipo son detectado y evitdos, tnaot dinamica o estatica
	
## Subprograma o Subrutina

Es una abstriaccion de un proceso que es llamado. El caller pasa argumentos a la subrutina la cual los acpeta como parametros.

Mientras el caller espera, la subrutina se ejecuta, esto puede afectar al stado global del sistema, opcionalmente retorna resultados al caller.

Una function returna uno o vaios valores y es llamadas en una expression. Un procedimiento no retorna valores y es llamadado en un statement, no es una exprecion, pero algunos lenguajes no tiene statements (solo expressiones). Algunos lenguajes tienen el mecanismo de `void context` o employ a special return como nil or `()` para parece funciones como un procedures.

Un metodo es una subrutina definidina en un OBJETO en un contecto de `POO`.

## Modelo sematicos

Los parámetros formales se caracterizan por uno de los tres modelos semánticos distintos: (1) Pueden recibir datos del parámetro real correspondiente; (2) pueden transmitir datos al parámetro real; o (3) pueden hacer ambas cosas. Estos modelos se denominan modo in, modo out y modo inout, respectivamente. Por ejemplo, considere un subprograma que toma dos matrices de valores int como parámetros-lista1 y lista2. El subprograma debe añadir la lista1 a la lista2 y devolver el resultado como una versión revisada de la lista2. Además, el subprograma debe crear una nueva matriz a partir de las dos matrices dadas y devolverla. Para este subprograma, list1 debe estar en modo in, porque no debe ser modificado por el subprograma. list2 debe estar en modo inout, porque el subprograma necesita el valor dado del array y debe devolver su nuevo valor. El tercer array debe estar en modo out, porque no hay valor inicial para este array y su valor calculado debe ser devuelto a la persona que llama.

## Variedad de argumentos

Positional and Named Association

Overloading: With overloaded subroutines the compiler has to figure out which subroutine is being called; this is called overload resolution

Default Parameters

Variadic Subroutines (list con * y dict con ** en python)

Patterns (destructurin, array por posisicon y object por nombre)

## Sintaxis

## Parametros

Common mechanisms
People have identified a bunch of mechanisms over time:

in (const) — callee can't write to the parameter.
out — callee can't read the parameter; it just sends the value out at the end.
in out — Callee can read and write parameter; changes to parameter are reflected in the argument (but we don't know if the argument sees the update during or only after the execution of the callee).
by value — Argument value is copied to the parameter; changes to parameter are not reflected in argument.
by value/result — Argument value copied in; parameter value copied out at end of callee.
aliasing (sharing) — argument and parameter are one. Changes to parameter immediately are seen in the argument, because, as was just mentioned, the argument and parameter are one.
by reference — An implementation of aliasing through passing the address of the argument.
by name — Parameter is more or less a macro, taking on the source code text of the argument.

## Paso por valor

Cuando un parámetro se pasa por valor, el valor del parámetro real se utiliza para inicializar el parámetro formal correspondiente, que entonces actúa como una variable local en el subprograma, implementando así la semántica en modo. El paso por valor se implementa normalmente mediante copia, porque los accesos suelen ser más eficientes con este enfoque. Podría implementarse transmitiendo una ruta de acceso al valor del parámetro real en el llamador, pero eso requeriría que el valor estuviera en una celda protegida contra escritura (una que sólo puede ser leída). Aplicar la protección contra escritura no siempre es una cuestión sencilla. 

Por ejemplo, supongamos que el subprograma al que se ha pasado el parámetro lo pasa a su vez a otro subprograma. Esta es otra razón para utilizar la transferencia de copias. Como veremos en la Sección 9.5.4, C++ proporciona un método conveniente y efectivo para especificar la protección contra escritura en parámetros pass-by-value que se transmiten por ruta de acceso. La ventaja del pass-by-value es que para los escalares es rápido, tanto en coste de enlace como en tiempo de acceso. 

La principal desventaja del método pass-by-value si se utilizan copias es que se requiere un almacenamiento adicional para el parámetro formal, ya sea en el subprograma llamado o en alguna zona fuera del llamador y del subprograma llamado. 

Además, el parámetro real debe copiarse en el área de almacenamiento del parámetro formal correspondiente. El almacenamiento y las operaciones de copia pueden ser costosos si el parámetro es grande, como una matriz con muchos elementos.

### Paso por referencia
El paso por referencia es un segundo modelo de implementación para los parámetros del modo de salida
en modo de salida. Sin embargo, en lugar de copiar valores de datos de ida y vuelta, como en
pass-by-value-resultado, el método pass-by-reference transmite una ruta de acceso,
normalmente sólo una dirección, al subprograma llamado. Esto proporciona la ruta de acceso
a la celda que almacena el parámetro real. De este modo, el subprograma llamado puede
puede acceder al parámetro real en la unidad de programa que llama. En efecto,
el parámetro real se comparte con el subprograma llamado.
La ventaja de la transferencia por referencia es que el proceso de transferencia es eficiente
eficiente, tanto en términos de tiempo como de espacio. No se requiere espacio duplicado y
no es necesario copiar.
Sin embargo, el método de paso por referencia tiene varias desventajas.
En primer lugar, el acceso a los parámetros formales será más lento que el de paso por valor
debido al nivel adicional de direccionamiento indirecto que se requiere.
Segundo, si sólo se requiere una comunicación unidireccional con el subprograma llamado
se requiere, se pueden hacer cambios inadvertidos y erróneos en el parámetro real.
parámetro.

### Paso por resultado

El paso por el resultado es un modelo de implementación para los parámetros del modo de salida. Cuando un
se pasa por resultado, no se transmite ningún valor al subprograma. El
parámetro formal correspondiente actúa como una variable local, pero justo antes de
de que el control se devuelva a la persona que llama, su valor se transmite al
parámetro real del llamador, que obviamente debe ser una variable. (¿Cómo podría
el llamador referenciaría el resultado calculado si fuera un literal o una expresión).
El método pass-by-result tiene las ventajas y desventajas de pass-byvalue, además de algunas desventajas adicionales. Si los valores se devuelven por copia (en lugar de
como en las rutas de acceso), como suele ocurrir, el método pass-by-resultado también requiere
el almacenamiento adicional y las operaciones de copia que requiere el pass-by-value.
Al igual que con el pass-by-value, la dificultad de implementar el pass-by-resultado mediante
transmisión de una ruta de acceso suele hacer que se implemente mediante copia.
En este caso, el problema está en asegurar que el valor inicial del parámetro real
no se utilice en el subprograma llamado.
Un problema adicional con el modelo de paso por resultado es que puede haber una
colisión de parámetros reales, como la que se crea con la llamada


### Paso por nombre
Pass-by-name es un método de transmisión de parámetros en modo inout que no
corresponde a un único modelo de implementación. Cuando los parámetros se pasan
por nombre, el parámetro real es, en efecto, sustituido textualmente por el
parámetro formal correspondiente en todas sus apariciones en el subprograma. Este método
método es bastante diferente de los discutidos hasta ahora; en cuyo caso, los parámetros formales
parámetros formales están ligados a valores o direcciones reales en el momento de la
llamada al subprograma. Un parámetro formal pass-by-name se vincula a un método de acceso
de acceso en el momento de la llamada al subprograma, pero la vinculación real a un valor o
una dirección se retrasa hasta que se asigna o se hace referencia al parámetro formal.
La implementación de un parámetro pass-by-name requiere que se pase un subprograma
al subprograma llamado para evaluar la dirección o el valor del parámetro formal.
del parámetro formal. El entorno de referencia del subprograma pasado también debe
pasar. Este subprograma/entorno de referencia es un cierre (véase el apartado
9.12).7 Los parámetros de paso por nombre son complejos de implementar e ineficientes.
ineficientes. También añaden una complejidad significativa al programa, reduciendo así su legibilidad y fiabilidad.
y, por lo tanto, reducen su legibilidad y fiabilidad.

```
real procedure Sum(k, l, u, ak)
     value l, u;
     integer k, l, u;
     real ak;
     comment k and ak are passed by name;
 begin
     real s;
     s := 0;
     for k := l step 1 until u do
         s := s + ak;
     Sum := s
 end;
```

In the procedure, the index variable k and summation term ak are passed by name. Call by name enables the procedure to change the value of the index variable during execution of the for loop. Call by name also causes the ak argument to be reevaluated during each iteration of the loop. Typically, ak will depend upon the changing (side-effected) k.

For example, code to compute the sum of the first 100 terms of a real array V[] would be:

```
Sum(i, 1, 100, V[i])
```


## Identificar los tipo de subrutinas existentes

Subroutines as Values

Closures: A closure is a subroutine that refers to variables defined in an enclosing scope.
    Deep Binding — if it uses bindings at time of definition
    Shallow Binding — if it uses bindings at time of call

Subroutines as Arguments

## Exercises

### Escribir ER concisas, completas sin redundancia.

```re
^1+(1*01*0)*$ num par ceros

^1+(01*01*)*0 num impar ceros

(?!.*(test|enma))(?=\D*\d)(?=[^A-Z]*[A-Z])^.*$
Requiere mayus, numero y no inclue test y enma

(?=\D*\d)^([^A-Z]*[A-Z][^A-Z]*[A-Z][^A-Z]*)+$
Contiene numero y pares de mayusculas
```

### Comprender un autómata (no graficarán pero deben responder que reconocería el mismo).
	
### Escribir reglas sintácticas usando BNF o EBNF

```html
<sqlstg> ::= <select> <field> <from> <body>
<select> ::= "SELECT "
<from> ::= " FROM "
<where> ::= " WHERE "
<op> ::= " AND " | " OR "
<comp> ::= "=" | "!=" | ">" | "<" | ">=" | "<="
<id> ::= ([A-Z] | [a-z]) ([A-Z] | [a-z] | [0-9])
<field> ::= "* " | <id> | <moreid>
<moreid> ::= <id> | <id> ", " <moreid>
<body> ::= <id> | <id> <where> <wbody>
<wbody> ::= <cond> | <cond> <op> <wbody>
<lp> ::= "("
<rp> ::= ")"
<cond> ::= <id> <comp> <id> | <lp> <wbody> <rp>
```

### Implementar un analizador léxico, sintáctico usando PLY

```python
from typing import Tuple
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

```