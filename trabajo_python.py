import csv
import funciones


archivo_csv = 'operaciones_calculadora_personalizada.csv'

def leer_archivo_csv(archivo_csv: str) -> str:
    """ Función que tiene por objeto abrir un archivo csv e iterar cada fila,
        en cada fila es posible encontrar 5 o 6 cadenas de caracteres separadas
        por coma (,) en donde:

            1.- numero_fila = indica la fila que está siendo procesada,
                "Siendo un parámetro de la fila puede ser calculado iterando
                enumerate(contenido)"
            2.- nombre_funcion = es el nombre de la función que será importada
                desde la librería funciones y serán pasados los 3 o 4 argumentos
                subsiguientes de la fila para su procesamiento.
            3.- arg1, arg2, arg3, esperado = dependiendo del tipo de función,
                los argumentos pueden ser de diferente tipo y pasados a la
                función respectiva para su prosesamiento

    Args:
        param1 (str): Nombre del archivo csv.

    Returns:
        str: Mensaje del procesamiento de cada fila del archivo csv
    """
    with open(archivo_csv, newline='') as archivo:
        contenido = csv.reader(archivo, delimiter=';', quotechar='"')

        for indice, fila in enumerate(contenido):
            try:
                numero_fila, nombre_funcion = fila[:2]
                arg1, arg2, arg3 = fila[2:5]
            except ValueError:
                print('Imposible procesar fila #{}, argumentos incompletos'
                      .format(indice))
                continue

            try:
                """
                Captura de error, el 6to parámetro puede o no ser pasado si
                algunos de los tres argumentos previos es de un tipo distinto
                """

                esperado = fila[5]
            except IndexError:
                esperado = 0

            resultado = 0
            mensaje = 'VALOR INVÁLIDO'

            try:
                resultado, mensaje = getattr(funciones, nombre_funcion) \
                    (arg1, arg2, arg3, esperado)
            except TypeError:
                """
                Captura de error TypeError, ocurre cuando se invoca la función y
                alguno de los argumentos está mal.
                """
                error = 'Argumento inválido para la función: {}' \
                    .format(nombre_funcion)
                print(error)
            except AttributeError:
                """
                Captura de error AttributeError, ocurre cuando el segundo
                parámetro de la fila nombre_funcion no es el nombre de una
                función válida
                """
                error = 'No existe la función: {}'.format(nombre_funcion)
                print(error)
            except ValueError as error:
                """
                Captura de error ValueError, ocurre cuando se invoca la función
                y los argumentos no pasan la validación.
                """
                print(str(error))
            finally:
                """
                Salida o retorno standard
                """
                salida = funciones.imprimir(
                    numero_fila, nombre_funcion, arg1, arg2, arg3, resultado,
                    mensaje)
                print(salida)


leer_archivo_csv(archivo_csv)
