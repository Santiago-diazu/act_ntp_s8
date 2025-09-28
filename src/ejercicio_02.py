import pandas as pd

def analisis_calificaciones():
    calificaciones = pd.Series([85, 92, 78],
                         index = ["Matemáticas", "Ciencias", "Historia"])
    print("Calificaciones de las estudiantes:\n", calificaciones, "\n")

    info_ciencias = calificaciones["Ciencias"]
    print("La nota de ciencias es:\n", info_ciencias, "\n")

    promedio = calificaciones.mean()
    print("La nota promeido de las materias es:\n", promedio, "\n")

    suma = calificaciones.sum()
    print("La suma de las notas es:\n", suma, "\n")

analisis_calificaciones()