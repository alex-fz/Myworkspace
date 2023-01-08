### Transformaciones

import numpy as np

## As type: este metodo nos permite modificar el tipo de dato de los valores de una array

arr_int = np.random.randint(100, size=(3,4))
print(arr_int)
print(arr_int.astype(float))

## Sort: este metodo nos permite ordenar los valores de un array

arr_int.sort()  # oredenara fila por fila los valores
#arr_int.sort(axis=0)  #ordenara columna por columna los valores
print(arr_int)


## Reshape: este metodo nos permite modificar las dimensiones de un array

arr_int: np.ndarray = arr_int.reshape(6,2)  # reshape toma como primer parametro las filas y como segundo las columnas para el reshape
print(arr_int)


## Flatten: este metodo crea un array unidimensional desde el original

plano_arr: np.ndarray = arr_int.flatten()
print(plano_arr)

## To list: este metodo crea una lista a partir de un array

lista_arr = plano_arr.tolist()
print(lista_arr, type(lista_arr))

## Separar y juntar arrays

arrays = np.split(arr_int, 6)  # como primer parametro el array que queremos dividir, y el segundo en cuantas partes lo queremos dividir 
print(arrays)

print(np.concatenate((arrays[1], arrays[0]), axis=0))  # concatenate es para juntar los arrays, como primer parametro toma una tupla
                                                        # con los array que quremos juntar y como segundo parametro el axis si lo queremos
                                                        #juntar horizontal o verticalmente, en este caso verticalmente



## La matriz transpuesta: las filas las transforma en columnas

t_arr = arr_int.T
print(t_arr)
