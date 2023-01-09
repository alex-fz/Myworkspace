import pandas as pd
import numpy as np

serie = pd.Series([1972, 1980, 1981, 1982])
print(serie)

# acceder a los valores y podemos usar metodos de la clase numpy
print(serie.values)  # devuelve un array de los valores
print(serie.values.sum())

# Index podemos definirlo nosotros o dejarlo vacio
print(serie.index)  # Devolvera una clase range index al no haberle definido los indices

### Definir explicitamente un array indice y pasarlo como argumento
serie = pd.Series([1972,1980,1981,1982], index=["Daniela", "Mateo", "Adrian", "Alex"])
print(serie)
print(serie.index)  # devolovera un array con los indices que definimos


### Tambien se pueden  crear Series a partir de diccionario, arrays, etc.
serie_2 = pd.Series(np.random.rand(10))
print(serie_2)


diccionario = {"cuadrado de {}".format(i): i*i for i in range(11)}

serie_dict = pd.Series(diccionario)
print(serie_dict) # las claves se volvieron indices y los valores pues valores