# Arrays multidimensionales

import numpy as np

# array = np.array([0,1,2,3,4,5])
# print(type(array))
# print(array)

notas = [v for v in range(10,25,3)]
notas_array = np.array(notas, dtype=float)  # con dtype indicas el tipo de dato que almacenamos en el arreglo
print(notas_array)
print(type(notas_array))

array_bidimensional_notas = np.array(([0,1,2,3,4], notas))  # array de dos dimensionas, pasar como tupla
print(array_bidimensional_notas)

print("DIMENSIONES:")
print(array_bidimensional_notas.ndim)   # ndim para ver el numor de dimensiones
print(notas_array.ndim)

print("SHAPE: ")
print(array_bidimensional_notas.shape)  # shape mostrara la morfa del array  ej: (2,6)  1.numero = filas 2.numeros = elemnetos
print(notas_array.shape)    # ej: (6,)  1.numero = elementos



### ARRAYS ESPECIALES / Matrices
print("ARRAY ZEROS:")
zeros_array = np.zeros((2,3), dtype=float)  # el metodo zeros creara una lista de solo ceros
print(zeros_array)

#-----------------

print("ARRAY ONES: ")
ones_array = np.ones((3,4), dtype=float)  # el metodo ones crear una lista de solo unos
print(ones_array)

#----------------
# la mtriz identidad tiene tantas columnas como filas, en la diagonal principal de elementos tiene unos y el resto de elementos son ceros

print("IDENTITY ARRAY: ")
id_array = np.identity((4), dtype=float)   # tambien se puede usar el metodo eye que es el mismo, es una matriz cuadrada
print(id_array)

#--------------
print("ARRGANGE ARRAY: ")
ar_array = np.arange(1,9)  # arange devolvera un array con el rango de valores indicados
print(ar_array)


