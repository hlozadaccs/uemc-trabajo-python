MANUAL DE USUARIO
=================

El siguiente proyecto intenta dar solución a los requerimientos solicitados en el archivo "Enunciado de Actividad 1. Aplicación python.pdf" y consta de dos archivos **trabajo_python.py** y **funciones.py** ambos programados en Python v3.7 compilado para un sistema operativo Debian GNU/Linux testing (buster).

Puede visitar mi repo desde el siguiente [enlace](https://github.com/imatsu/uemc-trabajo-python)

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
Operación ID - nombre_operador(operando1, operando2, operando3) - resultado: 0 - VALOR INVÁLIDO
Operación 1 - sumaResta(5, 3, 2) - resultado: 6 - CORRECTO
Operación 2 - sumaResta(12, 25, 42) - resultado: -5 - CORRECTO
Operación 3 - sumaResta(13, 13, 13) - resultado: 13 - INCORRECTO
Operación 4 - sumaResta(9, 8, 7) - resultado: 10 - CORRECTO
Operación 5 - sumaResta(1, 2, 3) - resultado: 0 - CORRECTO
Operación 6 - multiPot(1, 3, 2) - resultado: 9 - CORRECTO
Operación 7 - multiPot(5, 2, 3) - resultado: 1000 - CORRECTO
Operación 8 - multiPot(3, 2, 4) - resultado: 1296 - CORRECTO
Operación 9 - multiPot(1, 7, 2) - resultado: 49 - INCORRECTO
Operación 10 - multiPot(2, 3, 3) - resultado: 216 - CORRECTO
Operación 11 - triangulos(2, 3, 5) - resultado: 15.0 - CORRECTO
Operación 12 - triangulos(2.3, 1.6, 2) - resultado: 0 - VALOR INVÁLIDO
Operación 13 - triangulos(3, 2, 2) - resultado: 6.0 - CORRECTO
Operación 14 - triangulos(1.1, 2.2, 3) - resultado: 0 - VALOR INVÁLIDO
Operación 15 - triangulos(10, 5, 2) - resultado: 50.0 - CORRECTO
Operación 16 - sectores(2, 3, 5) - resultado: 20.94 - CORRECTO
Operación 17 - sectores(3.5, 6, 3) - resultado: 0 - VALOR INVÁLIDO
Operación 18 - sectores(5.55, 5, 1) - resultado: 0 - VALOR INVÁLIDO
Operación 19 - sectores(2.12, 4, 3) - resultado: 0 - VALOR INVÁLIDO
Operación 20 - sectores(10, 7, 2) - resultado: 89.72 - CORRECTO
Operación 21 - fibo(2, 3, 5) - resultado: 13 - CORRECTO
Operación 22 - fibo(1, 5, 7) - resultado: 45 - CORRECTO
Operación 23 - fibo(2, 7, 10) - resultado: 280 - CORRECTO
Operación 24 - fibo(11, 13, 6) - resultado: 98 - INCORRECTO
Operación 25 - fibo(5, 6, 12) - resultado: 809 - CORRECTO
Operación 26 - ecuaciones2(1, 3, 2) - resultado: -1.0 - CORRECTO
Operación 27 - ecuaciones2(1, 5, 3) - resultado: -0.7 - CORRECTO
Operación 28 - ecuaciones2(2, 7, 2) - resultado: -1.26 - INCORRECTO
Operación 29 - ecuaciones2(1, 4, 3) - resultado: -1.0 - INCORRECTO
Operación 30 - ecuaciones2(2, 9, 1) - resultado: -0.46 - INCORRECTO
Operación 31 - distancias((1,2), (-2,3), (3,-1)) - resultado: 9.57 - CORRECTO
Operación 32 - distancias((2,3), (1,5), (-2,-2)) - resultado: 9.86 - CORRECTO
Operación 33 - distancias((0,0), (-1,-1), (3,3)) - resultado: 7.08 - INCORRECTO
Operación 34 - distancias((9,-9), (2,3), (1,5)) - resultado: 16.13 - CORRECTO
Operación 35 - distancias((0,1), (0,3), (0,8)) - resultado: 7.0 - CORRECTO
Operación 36 - areaCartesiana((2,0), (-3,5), (3,2)) - resultado: 7.51 - INCORRECTO
Operación 37 - areaCartesiana((2,3), (1,5), (-2,-2)) - resultado: 6.5 - CORRECTO
Operación 38 - areaCartesiana((0,0), (-1,-1), (3,3)) - resultado: 0 - VALOR INVÁLIDO
Operación 39 - areaCartesiana((9,-9), (2,3), (1,5)) - resultado: 1.01 - INCORRECTO
Operación 40 - areaCartesiana((0,1), (3,3), (0,8)) - resultado: 10.51 - INCORRECTO
Operación 41 - acortar(Esto es una frase, 5, 6) - resultado: es una - CORRECTO
Operación 42 - acortar(Esto es una frase, 0, 6) - resultado: Esto e - INCORRECTO
Operación 43 - acortar(Esto es una frase, 5, 0) - resultado:  - INCORRECTO
Operación 44 - acortar(Esto es una frase, 2, 2) - resultado: to - INCORRECTO
Operación 45 - acortar(Esto es una frase, 0, 0) - resultado:  - INCORRECTO
Operación 46 - insertar(Esto es una frase, gran , 12) - resultado: Esto es una gran frase - CORRECTO
Operación 47 - insertar(Esto es una frase, no , 5) - resultado: Esto no es una frase - CORRECTO
Operación 48 - insertar(Esto es una frase, gran, 12) - resultado: Esto es una granfrase - INCORRECTO
Operación 49 - insertar(Esto es una frase,  bastante larga, 17) - resultado: Esto es una frase bastante larga - CORRECTO
Operación 50 - insertar(Esto es una frase, , que no media, 11) - resultado: Esto es una, que no media frase - CORRECTO
Operación 51 - barajar(Esto es una frase, gran, 2) - resultado: Esgtor eas nuna frase - CORRECTO
Operación 52 - barajar(gran, Esto es una frase, 1) - resultado: gErsatno es una frase - CORRECTO
Operación 53 - barajar(ABCDE, 12345, 1) - resultado: A1B2C3D4E5 - CORRECTO
Operación 54 - barajar(camarero, AAAA, 2) - resultado: caAmaAreAroA - CORRECTO
Operación 55 - barajar(espaciado,        , 1) - resultado: e s p a c i a do - INCORRECTO
Operación 56 - invertir(Esto es una frase, completo, 2) - resultado: to es una fraseEsto es una fra - INCORRECTO
Operación 57 - invertir(Esto es una frase, palabra, 1) - resultado: toEs  au asefra - INCORRECTO
Operación 58 - invertir(1234 5678 9012, palabra, 2) - resultado: 3412 7856 1290 - CORRECTO
Operación 59 - invertir(1234 5678 9012, completo, 3) - resultado: 4 5678 90121234 5678 9 - INCORRECTO
Operación 60 - invertir(Esto es una frase, palabra, 2) - resultado: toEs  au asefra - INCORRECTO
```

# ARCHIVO CSV

Se usa la versión 2 del archivo CSV proporcionado por el profesor en el tablón

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
