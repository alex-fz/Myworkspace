### Indexacion y slicing

# El slicing (filtrado) sigue la siguiente forma [i:j:k]
# Donde i es el indice iniacial; j es el indice de parada; y k es el incremento (step) no nulo

import numpy as np

a = np.array(range(64)).reshape((8,8))
#print(a)

print(a[1,1])  # el primer valor corresponde a la fila, y el segundo corresponde al elemento dentro de la fila

print(a[0:7:2,]) # selecciona desde la fila 0 a la 6 de dos en dos

print(a[1,3:]) # selecciona la segunda fila, y los elementos a partir del indice 3 hasta el final

print(a[[1,3,5], [3,6,7]])  ## SELECCIONAR ELEMENTOS PARTICULARES: la primera lista corresponde al indice de las filas que queremos
                            ## y la segunda lista corresponde al indice de cada elemento de las filas pasadas antes


print(a[[1,3,5], ::3])  # traera los elementos de las filas con indice 1,3,5 y los traera de tres en tres


## INDEXACION BOOLEANA, no es mas que una indexacion normal pero con una condicion logica

data = np.arange(8)
#print(data)

print(data < 4) # Devolvera un array con booleanos, devolvera true si el elemento en esa posicion cumple con la condicion, si no  devolvera false en esa posicion

print(data[data < 4]) # devolvera un array solo con los elementos que cumpla la condicion
data[np.array([ True,  True,  True,  True, False, False, False, False])] # lo mismo que el de arriba


friends = np.array(['alex', 'lorena', 'ibai', 'cristian', 'mateo'])

print('alex' in friends)
print(friends[friends!='lorena'])  # devolvera el array con todos los nombres menos el indicado

