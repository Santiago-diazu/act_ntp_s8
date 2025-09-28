import pandas as pd

def analisis_ventas():
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165], 
                       index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    print("Serie de ventas diarias:\n", ventas, "\n")
    
    indice_3 = ventas[3]
    print("Venta del Jueves):", indice_3, "\n")

    promedio = ventas.mean()
    print("Promedio de ventas:", promedio, "\n")

    ordenadas = ventas.sort_values()
    print("Ventas ordenadas:\n", ordenadas, "\n")

analisis_ventas()