###FUNCIONES UNIVERSALES UNARIAS
# Son funciones que realizan operaciones elemento a elemento sobre datos de un  ndarray
# Las funciones unarias comprenden todas las operaciones que reciben un solo array como argumento

import numpy as np 

a = np.array([2, 4, 9], float) 

np.abs(a)     # Calcula el valor absoluto
np.square(a)  # Calcula la raiz cuadrada

print(np.sqrt(a))     # sqrt devuelve un array de la raiz cuadrada de cada elemento

print(np.exp(a))             # exp devuelve un array de la exponenciacion de el num de euler(e) por cada elemento

print(np.log(a))      # clacula el logaritmo de cada uno de los elementos del array, tambien esta log10, log2, log1p



'''Funciones trigonometricas'''
np.sin(a)  # Devuelve el seno de cada elemento del array
np.cos(a)  # Devuelve el coseno de cada elemento del array 
np.tan(a)  # Devuelve la tangente de cada elemento del array

'''Funciones estadisticas'''
np.mean(a)  # Devuelve la media del array
np.std(a)   # Devuelve la desviacion estandard del array
np.var(a)   # Devuelve la varianza en un array

