import numpy as np
import pandas as pd

data = {
    "ciudades":["New York", "Madrid", "Tokyo", "Quito", "toledo"],
    "poblacion":[v*100000 for v in range(1,6)],
    "casos":np.random.randint(100,1000, size=5)
}

print(data)

# Crear dataframe con los datos
df = pd.DataFrame(data=data)
print(df)  # crea indice automatico, y coloca las keys del dict como los nombres de columna


# columns nos permite acceder a las columnas, nos devuelve un objeto de la clase index con el nombre de las columnas

print(df.columns)

# indexando con el nombre de la columna nos devolveria una serie con el contenido de esa columna

print(df["ciudades"])
# o tambien
df.ciudades

# dtypes, nos dice los tipos de datos de cada una de las columnas

print(df.dtypes)
