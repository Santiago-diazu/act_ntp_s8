import json
import pandas as pd

def bd_vehiculos_json():
    nombre_archivo = "../data/vehiculos.json"

    vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Focus", "año": 2018},
        {"marca": "Honda", "modelo": "Civic", "año": 2021}
    ]

    with open(nombre_archivo, mode="w", encoding="utf-8") as archivo:
        json.dump(vehiculos, archivo, ensure_ascii=False, indent=4)

    df = pd.read_json(nombre_archivo)

    print("Base de datos de vehículos:\n", df, "\n")
    print("Tipos de datos en la base de datos:\n", df.dtypes)

    return df

bd_vehiculos_json()
