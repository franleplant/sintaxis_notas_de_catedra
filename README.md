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

- variables dinamicas con numeros

- booleans

- comparaciones

- strings
  - crear strings
  - concatenacion
  - multiplicacion
  - indexacion
  - slices
  - inmutabilidad

- listas
  - crear listas
  - concat
  - indexacion
  - slices
  - mutabilidad
  - append / pop
  - assignacion
  - range fn

- tuplas
  - como armarlas
  - como usarlas

# Hasta aca llego la 2da clase

- control de flujo
  - if
  - for (for i in range(10))
  - while?

- funciones:
  - como crearlas
  - modelo de computacion de funciones puras, in -> out
  - hablar bastante sobre esto
  - fibonachi
  - scopes

- FSA
  - Tratar de llegar a una solucion entre todos
  - establecer un modelo de caja negra primero
  - usar el ejemplo primero del material de estudio
  - evaluar un poco los caminos posibles
  - hablar un poco de la expresion de ideas concretas en un lenguaje de programacion

