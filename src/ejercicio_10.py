import requests
import pandas as pd

def consumir_api_users():
    url = "https://playground.mockoon.com/users"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("Conexión exitosa a la API\n")

            data = response.json()
            df = pd.DataFrame(data)

            print("Primeras 5 filas de la base de datos:")
            print(df.head(), "\n")

            print("Información de la base de datos:")
            print(df.info())

            return df
        else:
            print(f"Error en lo solicitado. Código de estado: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error al conectar con la API:", e)

consumir_api_users()
