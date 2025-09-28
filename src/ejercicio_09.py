import numpy as np
import pandas as pd

def bd_numpy():
    ventas = np.array([
        [1500, 2000, 2500],
        [1800, 2200, 2600],
        [1700, 2100, 2400]
    ])

    df = pd.DataFrame(ventas, columns=['Q1', 'Q2', 'Q3'])

    print("Base de datos de ventas trimestrales:\n", df, "\n")
    print("Tipos de datos en la base de datos:\n", df.dtypes)

    return df

bd_numpy()
