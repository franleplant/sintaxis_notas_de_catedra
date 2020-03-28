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

- Que es programar?
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

DONE
- Que es Python?
```
- Un lenguage con tipado debil y dinmaico
- Es Interpretado
- REPL
```

PSEUDO DONE
- Por que python?
```
- Es un lenguaje mas moderno que Pascal
- Es dinámico y tiene una curva de aprendizaje mas simple
- Tiene muy buen manejo de colecciones de valores
- Es un lenguaje muy usado por lo que están aprendiendo algo de mucho valor y ademas hay mucha documentación en internet
```

DONE
- Dudas? Y preguntas
```
Mostrar como buscar en internet
Las dudas traerlas a clase y las hablamos entre todos
```

# 2

Objetivo: Introducir conceptos básicos de Python



NEXT
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


- Python REPL


En lugar de repasar que es una variable, un loop, un string etc etc tomamos el approach "hands on"
y lo que hacemos es construir 2 automatas finitos deterministicos muy simples con una
estructura muy austera (pero correcta) que dsp van a usar en el tp del lexer.

- Ejemplo 1 TODO, es el primer automata del tp creo que es a^n b o algo asi
- Ejemplo 2 https://github.com/franleplant/sintaxis2019-automata-time/blob/master/main.py



# Lexing

TODO formalizar el algoritmo que les vengo dando desde hace tiempo en un pseudo codigo parecido 
al que se les da en clase 

```
- input: source, del tipo string
- output: una lista de Tokens
- Token: (TokenKind, Lexeme)
- VALID_TOKENS: es la lista de todos los tokens validos y los automatas que los detectan, de la forma: [(TokenKind, AFD)]
- los afd devuelven 3 posibles valores: RESULTADO_ACEPTADO, RESULTADO_TRAMPA, RESULTADO_NO_ACEPTADO


fn lex

index = 0
tokens = [] 

while index < len(source)
  while source[index] sea espacio en blanco
    index += 1

  start = index
  candidates = []
  next_candidates = []
  all_trapped = false
  

  while not all_trapped
    all_trapped = True
    lexeme = src[start:index + 1]
    candidates = next_candidates
    next_candidates = []

    for (tokenKind, afd) in VALID_TOKENS      
      res = afd(lexeme)
      if res == ACCEPTED:
          next_candidates.append(token_type)
          all_trapped = False
      elif res == NOT_ACCEPTED:
          all_trapped = False
      
      index += 1

      if no hay candidatos entonces:
         error token desconocido

  # usamos el primer candidato de los posibles  
  token_kind = candidates[0]
  # construimos el token
  token = (tokenKind, lexeme)
  tokens.append(token)

return tokens
```


Example: https://github.com/franleplant/simple-dfa-lexer.py/blob/master/main.py
