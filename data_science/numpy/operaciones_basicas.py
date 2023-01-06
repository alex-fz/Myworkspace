### Los array nos permiten realizar operaciones aritmeticas elemento a elemento directamente

import numpy as np

array = np.arange(1,9)


array.shape = (2,4) # De esta manera reorganizamos la forma del array y lo convertimos a bidimendional
print(array)

#------------------------------------------------------
print("SUMA: ")
print(array + array)  # se suma elemento a elemento cosa que con listas normales no se puede hacer
#------------------------------------------------------
print("RESTA: ")
print(array - array) # se resta elemento a elemento cosa que con listas normales no se puede hacer
#------------------------------------------------------
print("MULTIPLICACION: ")
print(array * array) # se multiplica elemento a elemento cosa que con listas normales no se puede hacer
#------------------------------------------------------
print("PRODUCTO: ")
print(array ** array) # se expone elemento a elemento cosa que con listas normales no se puede hacer
#------------------------------------------------------
print("DIVISION: ")
print(array / array) # se divide elemento a elemento cosa que con listas normales no se puede hacer

