### Agregar y quitar valores a un array

import numpy as np

arr = np.arange(0,20,2)
print(arr)

arr_flot = np.random.rand(4,3)  # Rand del submodulo random de numpy genera numeros aleatorios enre el 0 y el 1, toma como parametro...
print(arr_flot)                 # cuantas filas y columnas queremos que tengra el array en este caso 4 filas y 3 columnas


arr_int = np.random.randint(10, size=(2,3)) # Numero enteros hasta 10, size indica la forma del array
print(arr_int)

arr_full = np.full((3,3),5)  # full toma como primer parametro la forma del array y como segundo un numero con el que se llena el array
print(arr_full)              # por ejemplo este array solo tendra cincos


arr = np.append(arr, [12,13,14,200]) # append agrega los elemntos al final, (el primer arg es el array que quereos modificar)
print(arr)

arr = np.insert(arr, 2, [1,2]) # insert toma como primer parametro un array, como segundo el indice, y tercero los valores que deseamos insertar
print(arr)   # insert inserto donde queramos los valores, (Insert convierte el array en unidemensional CUIDADO!)


arr_int = np.delete(arr_int, 1, axis=0)     # delete eliminara el elmento deseado, toma como primer argumneto el array, como segundo el indice y como tercero el axis
print(arr_int)                              # El axis es el eje de la matriz, si es 0 == filas y si es 1 == columnas
                                            # este ejemplo eliminara la segunda fila 
