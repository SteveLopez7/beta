#Traer datos excel a PY
import pandas as pd

#Read file
file = pd.read_excel("Ventas_2025.xlsx")

#Excel to dictionay
ventas = file.to_dict(orient="records")

#Show data
print(ventas)

for venta in ventas:
    print(venta)