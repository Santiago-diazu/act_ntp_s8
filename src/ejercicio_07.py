import csv
import pandas as pd

def cursos_csv():
    nombre_archivo = "cursos.csv"

    cursos = [
        ["Curso", "Instructor", "Duración"],
        ["Web II", "Jhon", "18 semanas"],
        ["Nuevas tecnologías", "Jhon", "18 semanas"],
        ["Móviles II", "Alejandro", "18 semanas"]
        ]
    with open (nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(cursos)

    try:
        df = pd.read_csv(nombre_archivo)
        print("Base de datos de cursos:\n", df)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe")

cursos_csv()