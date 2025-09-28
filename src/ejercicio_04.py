import pandas as pd

def datos_productos():
    datos = {
        "Productos": ["Computadores", "Celulares", 'Tablets'],
        "Precio": [1000, 800, 700],
    }

    df = pd.DataFrame(datos)

    print("Datos completos:\n", df, "\n")
    print("Datos específicos: \n", df["Precio"], "\n")
    print("Información básica: \n", df.info())

datos_productos()