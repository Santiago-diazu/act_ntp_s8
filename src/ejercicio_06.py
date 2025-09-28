import pandas as pd

def biblioteca():
    libros = [
        ["Bajo la misma estrella", "Jenn Muriel", 2000],
        ["Harry Potter", "Víctor Ramos", 2002],
        ["Pequeñas mentirosas", "Maria Fernanda", 2006]
        ]
    nombre_columna = ["Título", "Autor", "Año"]

    df = pd.DataFrame(libros, columns=nombre_columna)

    print("Base de datos de la biblioteca:\n", df, "\n")
    print("Dimensiones de la base de datos: \n", df.shape)

    return df

biblioteca()