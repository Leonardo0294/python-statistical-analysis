import random

def generar_edades(num_alumnos, edad_min=19, edad_max=36):
    """
    Genera una lista de edades aleatorias para un número dado de alumnos,
    dentro de un rango de edades especificado.

    Parámetros:
    num_alumnos (int): Número de edades a generar.
    edad_min (int): Edad mínima permitida (por defecto: 19).
    edad_max (int): Edad máxima permitida (por defecto: 36).

    Retorna:
    list: Lista de edades aleatorias generadas.
    """
    edades = [random.randint(edad_min, edad_max) for _ in range(num_alumnos)]
    return edades


num_alumnos = 30
edades_generadas = generar_edades(num_alumnos, edad_min=19, edad_max=36)
print("Edades generadas:", edades_generadas)
