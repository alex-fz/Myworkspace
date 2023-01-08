### Funciones Universales binarias
'''Son funciones que realizan operaciones elemento-a-elemento sobre datos en una ndarray.
Las funciones binarias toman dos arrays y devuelven uno o mas arrays.'''

import numpy as np

arr = np.array([5,36,17,18,9])
arr_2 = np.array([8,24,17,19,9])

print(np.add(arr,arr_2))  # add es la funcion de suma y devuelve un array de la suma de elemento a elemento
print(np.subtract(arr,arr_2)) # substract es la funcion de resta y devuelve un array de la resta de elemento a elemento
print(np.multiply(arr,arr_2)) # multiply es la funcion de multiplicar y devuelve un array de la multiplicacion de elemento a elemento
print(np.divide(arr,arr_2)) # divide es la funcion de division y devuelve un array de la division de elemento a elemento

print(np.array_equal(arr, arr_2)) # evalua si los dos arrays tienen los mismos elementos en las mismas posiciones y devuelve un bool

print(np.fmin(arr, arr_2)) # fmin compara los dos arrays elemento a elemento y devuelve un array con los elemento mas bajos comparados
print(np.fmax(arr, arr_2)) # fmax compara los dos arrays elemento a elemento y devuelve un array con los elemento mas altos comparados

