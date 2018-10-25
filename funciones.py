import math


PI = 3.14 # Constante PI


def sumaResta(arg1: str, arg2: str, arg3: str, esperado: str) -> int:
    """ Realiza el cálculo de la función arg1 + arg2 - arg3.

    Args:
        arg1 (str): Argumento 1
        arg2 (str): Argumento 2
        arg3 (str): Argumento 3
        esperado (str): Valor esperado

    Returns:
        int: resultado de la operación matemática arg1 + arg2 - arg3
        str: mensaje de salida.
    """
    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))
    resultado = a_entero(arg1 + arg2 - arg3)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def multiPot(arg1: str, arg2: str, arg3: str, esperado: str) -> int:
    """ Realiza el cálculo de la función arg1 * arg2 ** arg3

    Args:
        arg1 (str): Argumento 1
        arg2 (str): Argumento 2
        arg3 (str): Argumento 3
        esperado (str): Valor esperado

    Returns:
        int: resultado de la operación matemática arg1 * arg2 ** arg3
        str: mensaje de salida.
    """
    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))
    resultado = a_entero(arg1 * arg2 ** arg3)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def triangulos(arg1, arg2, arg3, esperado):
    """ Calcula el area de N triángulos en donde:

    Args:
        arg1 (str): Argumento 1, base
        arg2 (str): Argumento 2, altura
        arg3 (str): Argumento 3, cantidad de triángulos
        esperado (str): Valor esperado

    Returns:
        int: resultado de la operación matemática arg1 * arg2 / 2 * arg3
        str: mensaje de salida.
    """
    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))
    resultado = a_entero(arg1 * arg2 / 2 * arg3)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def sectores(arg1: str, arg2: str, arg3: str, esperado: str) -> int:
    """ Calcula el área de varios sectores circulares iguales truncando a 2
        decimales

    Args:
        arg1 (str): Argumento 1, radio
        arg2 (str): Argumento 2, número de sectores iguales
        arg3 (str): Argumento 3, número de sectores a sumar
        esperado (str): Valor esperado

    Returns:
        int: resultado de la función (PI * arg1 ** 2 / arg2) * arg3
        str: mensaje de salida.
    """

    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))
    resultado = a_entero((PI * arg1 ** 2 / arg2) * arg3)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def fibo(arg1: str, arg2: str, arg3: str, esperado: str) -> int:
    """ Calcula una personalización de la secuencia fibo

    Args:
        arg1 (str): Argumento 1, valor inicial, 0 o positivo
        arg2 (str): Argumento 2, siguiente valor, este debe ser mayor a arg1
        arg3 (str): Argumento 3, cantidad de secuencias que deben ser halladas
        esperado (str): Valor esperado

    Returns:
        int: resultado de la función fibo
        str: mensaje de salida.
    """

    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))

    if arg1 < 0 or arg2 < arg1 or arg3 <= 0:
        raise ValueError('El argumento no cumple los requerimientos básicos')

    if arg3 > 2:
        arg3 =- 2

    resultado = arg1 + arg2
    for indice in range(arg3):
        resultado = arg1 + arg2
        arg1 = arg2
        arg2 = resultado

    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def ecuaciones2(arg1: str, arg2: str, arg3: str, esperado: str) -> int:
    """ Función que resuelve ecuación de segundo grado, se captura error
        cuando se ejecuta la raiz cuadrada de un número negativo

    Args:
        arg1 (str): Argumento 1, coeficiente de grado 2
        arg2 (str): Argumento 2, coeficiente de grado 1
        arg3 (str): Argumento 3, coeficiente de grado 0
        esperado (str): Valor esperado

    Returns:
        int: resultado de la función
        str: mensaje de salida.
    """

    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))

    try:
        resultado = a_entero((-arg2 + math.sqrt(arg2 ** 2 - 4 * arg1 * arg3))
            / 2 * arg1)
    except ValueError:
        raise ValueError('Valor negativo para la raiz cuadrada')
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def distancia(argumento1: tuple, argumento2: tuple) -> float:
    xa, ya = argumento1
    xb, yb = argumento2

    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


def distancias(arg1: str, arg2: str, arg3: str, esperado: str) -> float:
    """ Retorna la distancia cartesiana entre el punto del primer operador y
        el segundo y sumarle la distancia entre el punto del segundo operador y
        del tercero

    Args:
        arg1 (str): Argumento 1, coeficiente de grado 2
        arg2 (str): Argumento 2, coeficiente de grado 1
        arg3 (str): Argumento 3, coeficiente de grado 0
        esperado (str): Valor esperado

    Returns:
        int: resultado de la función
        str: mensaje de salida.
    """
    arg1, arg2, arg3 = list(map(a_tupla, [arg1, arg2, arg3]))
    esperado = a_entero(esperado)

    try:
        resultado = a_entero(distancia(arg1, arg2) + distancia(arg2, arg3))
    except ValueError:
        raise ValueError('Valor negativo para la raiz cuadrada')

    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def semiperimetro(lado_a, lado_b, lado_c):
    return (lado_a + lado_b + lado_c) / 2


def areaHeron(sp, distancia_ab, distancia_bc, distancia_ca):
    return math.sqrt(sp * (sp - distancia_ab) * (sp - distancia_bc) * (sp - distancia_ca))


def areaCartesiana(arg1: str, arg2: str, arg3: str, esperado: str) -> float:
    arg1, arg2, arg3 = list(map(a_tupla, [arg1, arg2, arg3]))
    esperado = a_entero(esperado)

    lado_a = distancia(arg1, arg2)
    lado_b = distancia(arg2, arg3)
    lado_c = distancia(arg3, arg1)

    sp = semiperimetro(lado_a, lado_b, lado_c)
    resultado = areaHeron(sp, lado_a, lado_b, lado_c)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def comparar(valor1, valor2):
    mensaje = 'INCORRECTO'
    if valor1 == valor2:
        mensaje = 'CORRECTO'

    return mensaje


def imprimir(numero_fila, nombre_funcion, arg1, arg2, arg3, resultado, mensaje):
    return 'Operación {} - {}({}, {}, {}) - resultado: {} - {}'.format(
        numero_fila, nombre_funcion, arg1, arg2, arg3, resultado, mensaje)


def a_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return '\"{}\"'.format(valor)


def a_tupla(valor):
    tupla = eval(valor)
    if isinstance(tupla, tuple):
        return tupla
