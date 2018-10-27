MANUAL DE USUARIO
=================

El siguiente proyecto intenta dar solución a los requerimientos solicitados en el archivo "Enunciado de Actividad 1. Aplicación python.pdf" y consta de dos archivos **trabajo_python.py** y **funciones.py** ambos programados en Python v3.7 compilado para un sistema operativo Debian GNU/Linux testing (buster)

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
