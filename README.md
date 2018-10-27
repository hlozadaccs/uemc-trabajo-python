MANUAL DE USUARIO
=================

El siguiente proyecto intenta dar solución a los requerimientos solicitados en el archivo "Enunciado de Actividad 1. Aplicación python.pdf" y consta de dos archivos **trabajo_python.py** y **funciones.py** ambos programados en Python v3.7 compilado para un sistema operativo Debian GNU/Linux testing (buster).

# CONTENIDO DEL PROYECTO

El proyecto conteniene los siguientes archivos:

1. **diagrama_trabajo_python.png**: Archivo que contiene un pequeño diagrama de flujo del funcionamiento de la aplicación
1. **Enunciado de Actividad 1. Aplicación python.pdf**: Requerimientos del proyecto.
1. **funciones.py**: Contiene todas las funciones necesarias para poder ejecutar el proyecto.
1. **LICENSE**: Licencia Pública General v3
1. **operaciones_calculadora_personalizada.csv**: Contiene la información de origen necesaria para la ejecución del proyecto.
1. **Pipfile**: Dependencias del proyecto
1. **resultados.txt**: Salida producto de la ejecución del proyecto
1. **trabajo_python.py**: Programa inicial

# EJECUCIÓN

```bash
$ python3.7 trabajo_python.py
```

# SALIDA ESPERADA

```
Operación 1 - sumaResta(5, 3, 2) - resultado: 6 - CORRECTO
Operación 2 - sumaResta(3, 4, 8) - resultado: -1 - INCORRECTO
Argumento inválido para la función: sumaResta
Operación 3 - sumaResta(a, 3, 2) - resultado: 0 - VALOR INVÁLIDO
Operación 4 - multiPot(1, 3, 2) - resultado: 9 - CORRECTO
Operación 5 - multiPot(1, 3, 2) - resultado: 9 - INCORRECTO
Operación 6 - triangulos(2, 3, 5) - resultado: 15.0 - CORRECTO
Operación 7 - triangulos(2, 3, 5) - resultado: 15.0 - INCORRECTO
No existe la función: calculaMe
Operación 8 - calculaMe(1, 1, 1) - resultado: 0 - VALOR INVÁLIDO
Operación 9 - sectores(2, 3, 5) - resultado: 20.93 - CORRECTO
Operación 10 - sectores(2, 3, 5) - resultado: 20.93 - INCORRECTO
Argumento inválido para la función: sectores
Operación 11 - sectores(a, b, c) - resultado: 0 - VALOR INVÁLIDO
Operación 12 - fibo(2, 3, 5) - resultado: 5 - INCORRECTO
Argumento inválido para la función: fibo
Operación 13 - fibo(3, 3, a) - resultado: 0 - VALOR INVÁLIDO
Operación 14 - ecuaciones2(1, 3, 2) - resultado: -1.0 - CORRECTO
Valor negativo para la raiz cuadrada
Operación 15 - ecuaciones2(5, 3, 2) - resultado: 0 - VALOR INVÁLIDO
Operación 16 - distancias((1,2), (-2,3), (3,-1)) - resultado: 9.57 - CORRECTO
Operación 16 - distancias((-5,2), (-2,3), (3,-1)) - resultado: 9.57 - INCORRECTO
Operación 16 - distancias((1,9), (2,9), (3,9)) - resultado: 2.0 - INCORRECTO
Operación 17 - areaCartesiana((2,0), (-3,5), (3,2)) - resultado: 7.5 - CORRECTO
Operación 18 - acortar(Esto es una frase, 5, 6) - resultado: es una - CORRECTO
Operación 19 - acortar(Esto es una frase, 5, 2) - resultado: es - INCORRECTO
Operación 20 - insertar(Esto es una frase, gran , 12) - resultado: Esto es una gran frase - CORRECTO
Operación 21 - barajar(Esto es una frase, gran, 2) - resultado: Esgtor eas nuna frase - CORRECTO
Operación 22 - barajar(gran, Esto es una frase, 1) - resultado: gErsatno es una frase - CORRECTO
Argumento inválido para la función: sumaResta
Operación 23 - sumaResta(5, , ) - resultado: 0 - VALOR INVÁLIDO
```

# ARCHIVO CSV

De acuerdo al enunciado el archivo de origen debe tener los siguientes requerimientos:

1. El nombre del archivo debe ser **operaciones_calculadora_personalizada.csv**
1. El separador de columna debe ser el símbolo punto y coma (**;**)
1. El delimitador de cadena debe ser el símbolo comilla doble (**"**)

# PSEUDOCÓDIGO

## Pseudocódigo función principal:

```
INICIO
    VAR archivo_csv <- 'operaciones_calculadora_personalizada.csv'
    VAR archivo_txt <- 'resultados.txt'

    PARA indice, fila <- archivo_csv:
        VAR numero_fila        <- fila[0]
        VAR nombre_funcion     <- fila[1]
        VAR operando1          <- fila[2]
        VAR operando2          <- fila[3]
        VAR operando3          <- fila[4]
        VAR resultado_esperado <- fila[5]

        VAR resultado, mensaje <- nombre_funcion(operando1, operando2, operando3, esperado)
        VAR salida <- imprimir(numero_fila, nombre_funcion, operando1, operando2, operando3, resultado, mensaje)

        Escribir(salida)
        Escribir(archivo_txt, salida)
    FIN-PARA
FIN
```

## Pseudocódigo para las funciones:

### Función comparar

```
Función comparar(valor1, valor2):cadena de caracteres
Inicio
    VAR mensaje <- 'INCORRECTO'
    SI valor1 = valor2 ENTONCES
        mensaje <- 'CORRECTO'
    FIN-SI
   devolver mensaje
Fin-Función
```

### Función sumaResta

```
Función sumaResta(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado <- arg1 + arg2 - arg3
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función triangulo

```
Función multiPot(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado <- arg1 * arg2 ** arg3
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función triangulos

```
Función triangulos(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado <- arg1 * arg2 / 2 * arg3
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función sectores

```
Función sectores(arg1, arg2, arg3, esperado):tupla
Inicio
    CONSTANTE PI = 3.14
    VAR resultado <- (PI * arg1 ** 2 / arg2) * arg3
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función fibo

```
Función fibo(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado = 0
    PARA indice <- arg3:
        resultado = arg1 + arg2
        arg1 = arg2
        arg2 = resultado
    FIN-PARA

    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función ecuaciones2

```
Función fibo(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado = ((-1 * arg2) + raiz_cuadrada(arg2 ** 2 - 4 * arg1 * arg3)) / 2 * arg1
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función distancia

```
Función distancia(argumento1, argumento2):numérico
Inicio
    VAR xa <- argumento1[0]
    VAR xb <- argumento2[0]
    VAR ya <- argumento1[1]
    VAR yb <- argumento2[1]

    VAR resultado = raiz_cuadrada((xb - xa) ** 2 + (yb - ya) ** 2)
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función distancias

```
Función distancias(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado = distancia(arg1, arg2) + distancia(arg2, arg3)
    VAR mensaje <- comparar(resultado, esperado)
    devolver resultado, mensaje
Fin-Función
```

### Función semiperimetro

```
Función semiperimetro(lado_a, lado_b, lado_c):numérico
Inicio
    devolver (lado_a + lado_b + lado_c) / 2
Fin-Función
```

### Función areaHeron

```
Función semiperimetro(sp, distancia_ab, distancia_bc, distancia_ca):numérico
Inicio
    devolver raiz_cuadrada(sp * (sp - distancia_ab) * (sp - distancia_bc) * (sp - distancia_ca))
Fin-Función
```

### Función areaCartesiana

```
Función areaCartesiana(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR lado_a <- distancia(arg1, arg2)
    VAR lado_b <- distancia(arg2, arg3)
    VAR lado_c <- distancia(arg3, arg1)

    VAR sp <- semiperimetro(lado_a, lado_b, lado_c)
    VAR resultado <- a_decimal(areaHeron(sp, lado_a, lado_b, lado_c))
    VAR mensaje <- comparar(a_decimal(esperado), resultado)
    devolver resultado, mensaje
Fin-Función
```

### Función acortar

```
Función acortar(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR resultado <- arg1[arg2:arg2+arg3]
    VAR mensaje <- comparar(esperado, resultado)
    devolver resultado, mensaje
Fin-Función
```

### Función insertar

```
Función insertar(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR izquierda <- arg1[:arg3]
    VAR derecha   <- arg1[arg3:]
    VAR resultado <- izquierda + arg2 + derecha
    VAR mensaje <- comparar(esperado, resultado)
    devolver resultado, mensaje
Fin-Función
```

### Función barajar

```
Función barajar(arg1, arg2, arg3, esperado):tupla
Inicio
    VAR limite <- len(arg1)
    SI len(arg1) <- len(arg2) ENTONCES
        limite <- len(arg2)
    FIN-SI

    VAR resultado = []
    PARA indice <- limite:
        resultado[indice] <- arg1[indice]

        SI (indice + 1) % arg3 == 0 ENTONCES
            resultado[indice] <- arg2.pop(0)
        FIN-SI
    FIN-PARA
    
    VAR mensaje <- comparar(esperado, resultado)
    devolver resultado, mensaje
Fin-Función
```
