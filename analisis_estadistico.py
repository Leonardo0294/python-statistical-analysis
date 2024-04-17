import pandas as pd

def analisis_estadistico(valores):
    """
    Realiza un análisis estadístico básico de una lista de valores numéricos.

    Parámetros:
    valores (list): Lista de valores numéricos.

    Retorna:
    pandas.DataFrame: Dataframe que contiene las siguientes columnas como claves:
        - 'fi': Frecuencia absoluta de cada valor en la lista.
        - 'Fi': Frecuencia acumulada.
        - 'ri': Frecuencia relativa.
        - 'Ri': Frecuencia relativa acumulada.
        - 'pi%': Probabilidad (en porcentaje).
        - 'Pi%': Probabilidad acumulada (en porcentaje).
    """
    # Se calcula la frecuencia absoluta (fi) de cada valor
    fi_series = pd.Series(valores).value_counts().sort_index()
    fi = fi_series.to_dict()

    # Se calcula la frecuencia acumulada (Fi)
    Fi = pd.Series(fi).cumsum()

    # Se calcula el tamaño total de la muestra (n)
    n = len(valores)

    # Se calcula la frecuencia relativa (ri)
    ri = {valor: frecuencia / n for valor, frecuencia in fi.items()}

    # Se calcula la frecuencia relativa acumulada (Ri)
    Ri = pd.Series(ri).cumsum()

    # Se calcula la probabilidad (pi) en porcentaje
    pi_percent = {valor: frecuencia / n * 100 for valor, frecuencia in fi.items()}

    # Se calcula la probabilidad acumulada (Pi) en porcentaje
    Pi_percent = pd.Series(pi_percent).cumsum()

    # Se crea el dataframe con las estadísticas calculadas
    df_estadisticas = pd.DataFrame({
        'fi': list(fi.values()),
        'Fi': Fi,
        'ri': list(ri.values()),
        'Ri': Ri,
        'pi%': list(pi_percent.values()),
        'Pi%': Pi_percent
    }, index=list(fi.keys()))

    # Se formatea el dataframe para mostrar dos decimales en los resultados
    pd.options.display.float_format = '{:,.2f}'.format

    # Se copia el dataframe al portapapeles y se muestra por consola
    df_estadisticas.to_clipboard()
    print(df_estadisticas)

    return df_estadisticas

# Valores
valores = [34, 25, 19, 36, 36, 34, 32, 36, 34, 29,
           21, 36, 24, 35, 29, 24, 30, 34, 24, 25,
           31, 19, 24, 26, 26, 30, 35, 21, 31, 19]

# análisis estadístico de los valores
resultado_analisis = analisis_estadistico(valores)
