import pandas as pd

# Lista de edades de estudiantes
edades_estudiantes = [34, 25, 19, 36, 36, 34, 32, 36, 34, 29,
                      21, 36, 24, 35, 29, 24, 30, 34, 24, 25,
                      31, 19, 24, 26, 26, 30, 35, 21, 31, 1]

def analisis_estadistico(data: list[float | int]) -> pd.DataFrame:
    """
    Toma una lista de valores numéricos y calcula estadísticas descriptivas.
    
    Args:
        data (list[float | int]): Lista de valores numéricos.

    Returns:
        pd.DataFrame: DataFrame con las estadísticas calculadas.
            - x: Valores únicos de la lista.
            - fi: Frecuencia absoluta de cada valor.
            - Fi: Frecuencia acumulada.
            - ri: Frecuencia relativa.
            - Ri: Frecuencia relativa acumulada.
            - pi: Frecuencia porcentual.
            - Pi: Frecuencia porcentual acumulada.
    """
    # Se valida que los datos sean una lista no vacía
    if not data or not isinstance(data, list):
        raise ValueError("Los datos deben estar dispuestos en una lista.")

    # Se convierte la lista de datos en un DataFrame de pandas
    df = pd.DataFrame(data, columns=["edad"])

    # Se calcula la frecuencia absoluta (fi) de cada valor único
    data_frame = df["edad"].value_counts().sort_index().reset_index()
    data_frame.columns = ["x", "fi"]

    # Se calculan las frecuencias acumuladas (Fi), relativas (ri, Ri) y porcentuales (pi, Pi)
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / len(data) 
    data_frame["Ri"] = data_frame["ri"].cumsum()
    data_frame["pi"] = data_frame["ri"] * 100
    data_frame["Pi"] = data_frame["Ri"] * 100

    return data_frame

def main():
    # Se realizael análisis estadístico de las edades (edades_estudiantes)
    resultado_analisis = analisis_estadistico(edades_estudiantes)

    # Se imprime el resultado del análisis estadístico
    print("Análisis Estadístico de Edades:")
    print(resultado_analisis)

    # El resultado se copia al portapapeles
    resultado_analisis.to_clipboard(index=False)

if __name__ == "__main__":
    main()
