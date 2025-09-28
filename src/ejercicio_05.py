import pandas as pd

def bd_empleados():
    empleados = [
        {"empleado": "Ana", "Salario": 50000, "Departamento": "Ventas"},
        {"empleado": "Víctor", "Salario": 80000, "Departamento": "Marketing"},
        {"empleado": "Santiago", "Salario": 100000, "Departamento": "Contabilidad"}
    ]

    df = pd.DataFrame(empleados)

    print("Base de datos de los empleaods:\n", df, "\n")
    print("Fila con índice 0:\n", df.iloc[0], "\n")
    print("Fila con índice 1:\n", df.iloc[1], "\n")
    print("Fila con índice 2:\n", df.iloc[2], "\n")
    
    return df

bd_empleados()

