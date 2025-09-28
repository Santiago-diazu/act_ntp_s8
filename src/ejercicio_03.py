import pandas as pd

def operaciones_precios():
    precios = pd.Series([100, 150, 200],
                        index=["A", "B", "C"])
    
    descuento=pd.Series([0.10, 0.20, 0.15],
                        index=["A", "B", "C"])
    
    valor_descuento = precios * descuento
    con_descuento = precios - valor_descuento
    con_iva = con_descuento * 1.16

    print("El precio inciial de los productos es de:\n", precios)
    print("El valor del descuento es de:\n", valor_descuento, "\n")
    print("El precio del producto con el descuento aplicado es de:\n", con_descuento, "\n")
    print("El precio final con descuento y el IVA, es de:\n", con_iva)
    print("Operación elemento por elemento antes de IVA: \nProducto A: ", precios["A"], "-", valor_descuento["A"], "=", con_descuento["A"],"\nProducto B: ", precios["B"], "-", valor_descuento["B"], "=", con_descuento["B"],"\nProducto C: ", precios["C"], "-", valor_descuento["C"], "=", con_descuento["C"])
operaciones_precios()