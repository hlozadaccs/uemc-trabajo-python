import math


def sumaResta(arg1, arg2, arg3, esperado):
    """ Realiza el cálculo de la función arg1 + arg2 - arg3.

    Args:
        arg1 (str): Operando 1
        arg2 (str): Operando 2
        arg3 (str): Operando 3
        esperado (str): Valor esperado

    Returns:
        tuple (int, str):
            int: resultado de la operación matemática arg1 + arg2 - arg3
            str: mensaje de salida.
    """

    # Transformación de tipos de datos str a int
    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))
    resultado = a_entero(arg1 + arg2 - arg3)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def multiPot(arg1, arg2, arg3, esperado):
    """ Realiza el cálculo de la función arg1 * arg2 ** arg3

    Args:
        arg1 (str): Operando 1
        arg2 (str): Operando 2
        arg3 (str): Operando 3
        esperado (str): Valor esperado

    Returns:
        tuple (int, str):
            int: resultado de la operación matemática arg1 * arg2 ** arg3
            str: mensaje de salida.
    """
    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))
    resultado = a_entero((arg1 * arg2) ** arg3)
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def triangulos(arg1, arg2, arg3, esperado):
    """ Calcula el area de N triángulos en donde:

    Args:
        arg1 (str): Operando 1, base
        arg2 (str): Operando 2, altura
        arg3 (str): Operando 3, cantidad de triángulos
        esperado (str): Valor esperado

    Returns:
        tuple (float, str):
            float: resultado de la operación matemática arg1 * arg2 / 2 * arg3
            str: mensaje de salida.
    """
    arg1, arg2, arg3 = list(map(a_entero, [arg1, arg2, arg3]))
    resultado = a_decimal(arg1 * arg2 / 2 * arg3)
    mensaje = comparar(a_decimal(esperado), resultado)
    return resultado, mensaje


def sectores(arg1, arg2, arg3, esperado):
    """ Calcula el área de varios sectores circulares iguales truncando a 2
        decimales

    Args:
        arg1 (str): Operando 1, radio
        arg2 (str): Operando 2, número de sectores iguales
        arg3 (str): Operando 3, número de sectores a sumar
        esperado (str): Valor esperado

    Returns:
        tuple (float, str):
            float: resultado de la operación matemática
                   (PI * arg1 ** 2 / arg2) * arg3
            str: mensaje de salida.
    """

    PI = 3.14
    arg1, arg2, arg3 = list(map(a_entero, [arg1, arg2, arg3]))
    resultado = a_decimal((PI * arg1 ** 2 / arg2) * arg3)
    mensaje = comparar(a_decimal(esperado), resultado)
    return resultado, mensaje


def fibo(arg1, arg2, arg3, esperado):
    """ Calcula una personalización de la secuencia fibo

    Args:
        arg1 (str): Operando 1, valor inicial, 0 o positivo
        arg2 (str): Operando 2, siguiente valor, este debe ser mayor a arg1
        arg3 (str): Operando 3, cantidad de secuencias que deben ser halladas
        esperado (str): Valor esperado

    Returns:
        tuple (int, str):
            int: resultado de la suma sucesiva entre Operando 1 y Operando 2
            str: mensaje de salida.
    """

    arg1, arg2, arg3, esperado = list(map(a_entero, [arg1, arg2, arg3,
                                                     esperado]))

    if arg1 < 0 or arg2 < arg1 or arg3 <= 0:
        raise ValueError('El argumento no cumple los requerimientos básicos')

    if arg3 > 2:
        arg3 = arg3 - 2

    resultado = arg1 + arg2
    for indice in range(arg3):
        resultado = arg1 + arg2
        arg1 = arg2
        arg2 = resultado

    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def ecuaciones2(arg1, arg2, arg3, esperado):
    """ Función que retorna la solución positiva de la ecuación de segundo
        grado, se captura error cuando se ejecuta la raiz cuadrada de un número
        negativo

    Args:
        arg1 (str): Operando 1, coeficiente de grado 2
        arg2 (str): Operando 2, coeficiente de grado 1
        arg3 (str): Operando 3, coeficiente de grado 0
        esperado (str): Valor esperado

    Returns:
        tuple (float, str):
            float: resultado de la solución positiva de la ecuación de segundo
                   grado
            str: mensaje de salida.
    """

    # Transformación de variables a entero
    arg1, arg2, arg3 = list(map(a_entero, [arg1, arg2, arg3]))

    try:
        resultado = a_decimal((-arg2 + math.sqrt(arg2 ** 2 - 4 * arg1 * arg3))
            / 2 * arg1)
    except ValueError:
        raise ValueError('Valor negativo para la raiz cuadrada')

    mensaje = comparar(a_decimal(esperado), resultado)
    return resultado, mensaje


def distancia(argumento1, argumento2):
    """ Calcula la distancia entre dos puntos de un plano cartesiano

    Args:
        argumento1 tuple: Argumento 1, (xa, xb)
        argumento2 tuple: Argumento 2, (ya, yb)

    Returns:
        float: distancia, entre el argumento1 y argumento2
    """
    xa, ya = argumento1
    xb, yb = argumento2

    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


def distancias(arg1, arg2, arg3, esperado):
    """ Retorna la distancia cartesiana entre el punto del primer operador y
        el segundo y sumarle la distancia entre el punto del segundo operador y
        del tercero

    Args:
        arg1 (str): Argumento 1, coeficiente de grado 2
        arg2 (str): Argumento 2, coeficiente de grado 1
        arg3 (str): Argumento 3, coeficiente de grado 0
        esperado (str): Valor esperado

    Returns:
        tuple (float, str):
            float: distancia cartesiana
            str: mensaje de salida.
    """
    arg1, arg2, arg3 = list(map(a_tupla, [arg1, arg2, arg3]))

    try:
        resultado = a_decimal(distancia(arg1, arg2) + distancia(arg2, arg3))
    except ValueError:
        raise ValueError('Valor negativo para la raiz cuadrada')

    mensaje = comparar(a_decimal(esperado), resultado)
    return resultado, mensaje


def semiperimetro(lado_a, lado_b, lado_c):
    """ Retorna el semiperimetro de un triángulo.

    Args:
        lado_a (float): Argumento 1, distancia del lado a
        lado_b (float): Argumento 2, distancia del lado b
        lado_c (float): Argumento 3, distancia del lado c

    Returns:
        float: resultado de la sumatoria de los lados dividido entre 2
    """
    return (lado_a + lado_b + lado_c) / 2


def areaHeron(sp, distancia_ab, distancia_bc, distancia_ca):
    """ Retorna el area Heron de acuerdo a los parámetros.

    Args:
        sp (float): semiperímetro
        distancia_ab (float): distancia del lado a
        distancia_bc (float): distancia del lado b
        distancia_ca (float): distancia del lado c

    Returns:
        float: resultado de la areaHeron
    """
    return math.sqrt(sp * (sp - distancia_ab) * (sp - distancia_bc) *
        (sp - distancia_ca))


def areaCartesiana(arg1, arg2, arg3, esperado):
    """ Retorna el área de un triángulo en coordenadas cartesianas, aplicando
        la fórmula de Heron:

        1.- Se calcula la distancia de los puntos arg1, arg2, arg3
        2.- Se calcula el semiperimetro, el cual es la sumatoria de la distancia
            de los puntos dividido entre 2. (ver función semiperimetro)
        3.- Se calcula el area de Heron, con los resultados obtenidos.
            (ver función areaHeron)

    Args:
        arg1 (str): Argumento 1
        arg2 (str): Argumento 2
        arg3 (str): Argumento 3
        esperado (str): Valor esperado

    Returns:
        tuple (float, str):
            float: Invocación de la función areaHeron
            str: mensaje de salida.
    """

    # aquí se transforman a tuplas los puntos arg1, arg2, arg3
    arg1, arg2, arg3 = list(map(a_tupla, [arg1, arg2, arg3]))
    lado_a = distancia(arg1, arg2)
    lado_b = distancia(arg2, arg3)
    lado_c = distancia(arg3, arg1)

    sp = semiperimetro(lado_a, lado_b, lado_c)
    resultado = a_decimal(areaHeron(sp, lado_a, lado_b, lado_c))
    mensaje = comparar(a_decimal(esperado), resultado)
    return resultado, mensaje


def acortar(arg1, arg2, arg3, esperado):
    """ Retorna una cadena de caracteres cortada desde el punto la posición del
        arg1 hasta la posición del arg2, y compara con el valor esperado

    Args:
        arg1 (str): Operando 1, cadena de caracteres
        arg2 (str): Operando 2, valor inicial de corte
        arg3 (str): Operando 3, valor final de corte
        esperado (str): Valor esperado

    Returns:
        tuple (str, str):
            str: cadena de caracteres
            str: mensaje de salida.
    """

    # Se transforman a entero los argumentos 2 y 3
    arg2, arg3 = list(map(a_entero, [arg2, arg3]))
    if arg2 < 0 or arg3 < 0:
        raise ValueError('Las posiciones son negativas')

    resultado = arg1[arg2:arg2+arg3]
    mensaje = comparar(esperado, resultado)
    return resultado, mensaje


def insertar(arg1, arg2, arg3, esperado):
    """ Retorna una cadena de caracteres en donde arg2 es insertado en arg1 en
        la posición arg3

    Args:
        arg1 (str): Operando 1, cadena de caracteres
        arg2 (str): Operando 2, cadena de caracteres
        arg3 (str): Operando 3, posición
        esperado (str): Valor esperado

    Returns:
        tuple (str, str):
            str: cadena de caracteres
            str: mensaje de salida.
    """
    arg3 = a_entero(arg3)

    if len(arg1) < arg3:
        raise ValueError('La posición excede el tamaño del argumento 1')

    izquierda, derecha = arg1[:arg3], arg1[arg3:]
    resultado = '{0}{1}{2}'.format(izquierda, arg2, derecha)
    mensaje = comparar(resultado, esperado)
    return resultado, mensaje


def barajar(arg1, arg2, arg3, esperado):
    """ Retorna una cadena de caracteres producto de la mezcla del arg1 y el
        arg2 cada tantos (arg3) caracteres

    Args:
        arg1 (str): Operando 1, cadena de caracteres
        arg2 (str): Operando 2, cadena de caracteres
        arg3 (str): Operando 3, posición
        esperado (str): Valor esperado

    Returns:
        tuple (str, str):
            str: cadena de caracteres
            str: mensaje de salida.
    """

    # convierto a lista las cadenas de caracteres (aunque ya lo son)
    arg1, arg2 = list(map(list, [arg1, arg2]))

    # transformo a entero el argumento3
    arg3 = a_entero(arg3)

    # calculo la cadena de caracteres mas grande.
    limite = len(arg1) if len(arg1) > len(arg2) else len(arg2)

    resultado = []
    for indice in range(limite):
        try:
            resultado.append(arg1[indice])
        except IndexError:
            pass

        if (indice + 1) % arg3 == 0:
            try:
                resultado.append(arg2.pop(0))
            except IndexError:
                pass

    resultado = ''.join(resultado)
    mensaje = comparar(resultado, esperado)
    return resultado, mensaje


def invertir_palabra(cadena, cantidad):
    cadena = str(cadena)
    cantidad = int(cantidad)
    return '{}{}'.format(cadena[cantidad:], cadena[0:-cantidad])


def invertir(arg1, arg2, arg3, esperado):
    """
    Args:
        arg1 (str): Operando 1, cadena de caracteres
        arg2 (str): Operando 2, cadena de caracteres
        arg3 (str): Operando 3, cada cuanto se realizará la inversión
        esperado (str): Valor esperado

    Returns:
        tuple (str, str):
            str: cadena de caracteres
            str: mensaje de salida.
    """

    # transformo a entero el argumento3
    arg3 = a_entero(arg3)
    if arg2 == 'completo':
        resultado = invertir_palabra(arg1, arg3)
    elif arg2 == 'palabra':
        resultado = ' '.join([invertir_palabra(x, 2) for x in arg1.split(' ')])
    else:
        raise ValueError('El modo no está permitido')

    mensaje = comparar(resultado, esperado)
    return resultado, mensaje


def comparar(valor1, valor2):
    """ Compara dos valores desconocidos, y retorna un mensaje si el valor1 es
        igual o diferente del valor2, el tipo de datos es controlado por la
        función origen que la invoca

    Args:
        valor1 (Desconocido): Valor 1, el tipo de datos es desconocido
        valor2 (Desconocido): Valor 2, el tipo de datos es desconocido

    Returns:
        str: cadena de caracteres
    """
    mensaje = 'INCORRECTO'
    if valor1 == valor2:
        mensaje = 'CORRECTO'

    return mensaje


def imprimir(numero_fila, nombre_funcion, arg1, arg2, arg3, resultado, mensaje):
    """ Retorna una cadena de caracteres formateada por los argumentos y
        resultado de las funciones, en donde:

        args[:5] = Argumentos producto de la lectura del archivo csv
        args[6:] = Resultado de las funciones

    Args:
        numero_fila (int): Número de fila
        nombre_función (int): Nombre de la función
        arg1 (str): Operando 1
        arg2 (str): Operando 2
        arg3 (str): Operando 3
        resultado (desconocido): Resultado de la función invocada
        mensaje (str): Mensaje de la función invocada

    Returns:
        str: cadena de caracteres
    """
    return 'Operación {} - {}({}, {}, {}) - resultado: {} - {}'.format(
        numero_fila, nombre_funcion, arg1, arg2, arg3, resultado, mensaje)


def a_entero(valor):
    """ Retorna un valor transformado en cadena de caracteres

    Args:
        valor (str): Valor

    Returns:
        int: Valor
    """
    try:
        return int(valor)
    except ValueError:
        return '\"{}\"'.format(valor)


def a_decimal(valor):
    """ Función que transforma una cadena de caracteres en un valor decimal,
        truncado a 2 decimales

    Args:
        valor (str): Cadena de caracteres

    Returns:
        float: Cadena de caracteres transformado a decimal truncado a 2
        decimales
    """
    try:
        return math.ceil(float(valor) * 100) / 100
    except ValueError:
        return '\"{}\"'.format(valor)


def a_tupla(valor):
    """ Retorna un valor transformado a tupla (x,y)

    Args:
        valor (str): Valor

    Returns:
        tupla: Valor
    """
    tupla = eval(valor)
    if isinstance(tupla, tuple):
        return tupla
