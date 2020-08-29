Sintaxis
=========

> Notas de Cátedra



# 1

Objetivo: Familiarizarse con los conceptos básicos de programación

Preguntas Sondas

- Quienes programaron en otra cosa que no sea Pascal?
- Quien trabaja de programador?
- Quienes saben lo que es un OS?
- Quienes saben lo que es Linux/Unix?
- Quienes tienen maquinas con linux?

Preguntas para la clase, aproximar respuestas juntos, muy alto nivel todo

- que es un programa/software? ejemplos?

- Que es programar? (como se construyen esos programas?)
```
- Decirle a la computadora que hacer
- Expresar ideas complejas en partes mas simples y componerlas con el fin de instruir a la computadora que hacer
```
- Que es un lenguaje de programación?
```
Un lenguaje formal que nos permite darle instrucciones a una computadora
```
- Que elementos conforman un lenguaje de programación?

```
- Sintaxis y Semántica
- STD, Runtime, etc
- Compilador (en genérico, ya que esto puede ser un Compilador AoT, JIT, etc)
```


- Que es un compilador?
```
             --------------
hello.c ---> | Compilador | ---> Codigo de Maquina
             --------------
```


- Que es código de maquina?
```
Son las instrucciones que el hardware puede entender,
ejemplos:
sumas, restas, multiplicaciones, leer dir de memoria, escribir a memoria, entre otras
```

https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=790acd3f11948272341bd34e571432fd

- Que es un source file o un archivo fuente?
```
- Archivo de texto, plano, no word, solo texto
- Con una extensión estándar dependiente del lenguaje, pero no cambia el formato interno del archivo que es solo texto, ASCII o UTF-X
```

- Como se edita un source file?
```
Usando un editor de texto como
- notepad (no tiene sintax highligting)
- notepad++
- sublime
- atom

O IDEs
- Eclipse
- Netbeans
- Turbo Pascal IDE
```

- Types?
```
- Herramienta para analizar correctitud de los programas ESTATICAMENTE
- Requieren un esfuerzo extra del programador
- Existen varias disiplinas de tipado en distintos ldp y suelen ser grandes diferenciadores de ldp
  - Estaticos: toda _variable_ tiene un tipo que el compilador debe saber estaticamente, las variables no pueden cambiar de tipo
  - Dinamicos: el compilador no debe saber los tipos de toda variable estaticamente, y las variables pueden cambiar de tipos
```

- Pascal que disciplina de Tipado tiene?
```
Fuerte, Estatica y Seguro
```


DONE
- Que es Pascal?
```
En su encarnacion tipica, Pascal es
- Un lenguage con tipado Fuerte, Estatico y Seguro
- Es Compilado (AoT)
```

- Que es Python?
```
- Un lenguage con tipado debil y dinmaico
- Es Interpretado
- REPL
```

- Por que python?
```
- Es un lenguaje mas moderno que Pascal
- Es dinámico y tiene una curva de aprendizaje mas simple
- Tiene muy buen manejo de colecciones de valores
- Es un lenguaje muy usado por lo que están aprendiendo algo de mucho valor y ademas hay mucha documentación en internet
```

- Dudas? Y preguntas
```
Mostrar como buscar en internet
Las dudas traerlas a clase y las hablamos entre todos
```

# 2

Objetivo: Introducir conceptos básicos de Python


- Como usamos python?

```
- Bajarlo e instalarlo en su OS
- Bajarse notepad++ windows o sublime en Linux/Mac
- Probar un hello world:

  - ir a una carpeta de projectos
  - crear un archivo de texto
  - cambiarle la extension a `.py`
  - Editar el archivo con el editor de texto
  - Escribir `print("Hola!!!")`
```

- TAREA: que lean el tutorial oficial en español https://tutorial.python.org.ar/en/latest/real-index.html

- Python REPL


En lugar de repasar que es una variable, un loop, un string etc etc tomamos el approach "hands on"
y lo que hacemos es construir 2 automatas finitos deterministicos muy simples con una
estructura muy austera (pero correcta) que dsp van a usar en el tp del lexer.

- Ejemplo 1 automata "a+b"
- Ejemplo 2 https://github.com/franleplant/sintaxis2019-automata-time/blob/master/main.py



# Lexing

TODO formalizar el algoritmo que les vengo dando desde hace tiempo en un pseudo codigo parecido 
al que se les da en clase (ver el de mini reg exp engine)

```
- input: source, del tipo string
- output: una lista de Tokens
- Token: (TokenKind, Lexeme)
- VALID_TOKENS: es la lista de todos los tokens validos y los automatas que los detectan, de la forma: [(TokenKind, AFD)]
- los afd devuelven 3 posibles valores: RESULTADO_ACEPTADO, RESULTADO_TRAMPA, RESULTADO_NO_ACEPTADO
```


```
type TokenKind = string
type Lexeme = string
type Token = (TokenKind, Lexeme)

fn lex(source: string): List[Token]

  # agregamos un espacio al final para facilitar la condicion de corte
  source = source + " "
  index = 0
  tokens = [] 

  while index < len(source) {
    if source[index] es espacio en blanco
      index += 1
      continue

    candidates: List[TokenKind> = []
    start = index
  
    while True {
      next = calcCandidates(source[start:index + 1])
      if next.allTrapped
        break

   
      candidates = next.candidates;
      index += 1;
    }
    

    if len(candidates) == 0
      error "Token desconocido"
    
    token_kind = candidates[0]
    lexeme = source[start : index]
    token = (token_kind, lexeme)
    tokens.append(token)
 }
  
return tokens
```

```
type TokenConfig = List[(TokenKind, Automata)]
let TOKEN_CONFIG: TokenConfig = [
  ("ParOpen", parOpenAutomata),
  ...
]

def calcCandidates(str: string): {allTrapped: bool, candidates: List[TokenKind]}

  allTrapped = true
  candidates = []
  for (token_kind, automata) in TOKEN_CONFIG {
    res = automata(str)
    if res == RESULT_ACCEPTED
      allTrapped = false
      candidates.append(token_kind)
    if res == RESULT_NOT_ACCEPTED
      allTrapped = false
      
  }
  
  return {allTrapped, candidates}
           
```


Example: https://github.com/franleplant/simple-dfa-lexer.py/blob/master/main.py



## Parsing

Simple model recursive-descent-parser-py

High level struture. 

Esto esta modelado en base a la teoria / diapositivas mas algunas estructuras basicas programaticas

```python

# main data structure
producciones = {
    'S': [
        ['a', 'S', 'a'],
        ['a', 'a'],
    ]
}

no_terminales = ['S']

def Parser(inputString):
    # internal state
    self = {
        'tokens': lex(inputString),
        'index': 0,
        'error': False,
    }

    # Llamado "algoritmo" en el material
    def parse():
        pni('S')
        token_actual = self['tokens'][self['index']]
        if token_actual != 'eof' or self['error']:
            print('Unexpected input termination')
            return False

        return True

    def procesar(parteDerecha):
       # TODO


    # Llamado "Pni" (ACA pasa el backtracking)
    def pni(noTerminal):
       # TODO


    # la funcion Parser devuelve est
    return parse()
```
