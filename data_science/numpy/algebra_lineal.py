import numpy as np

'''Numpy tiene el submodulo de linalg para utilizar mas metodos de de la algebra lineal'''
#-----------------------------------------------------------------------------------------------------------
## Producto de arrays

a = np.array([1,2,3], dtype=float)
b = np.array([0,1,1], dtype=float)

# para realizar un producto entre arrays unidimensionales utilizamos el metodo dot de numpy
'''dot realiza un producto escalar, un producto escalar realiza una multiplicacion elemento a elemento
y suma los resultados finales, entonces dot devuelve un numero que es el escalar de todo el array'''

#print(np.dot(a, b))
#a.dot(b)


#-----------------------------------------------------------------------------------------------------------
print("PRODUCTO DE MATRICES: ")
## Producto de matrices
c = np.array([[5,2],[4,8]], dtype=float)
d = np.array([[2,4],[5,3]], dtype=float)

                                                                                                        # [[5. 2.]
                                                                                                        #  [4. 8.]] 
                                                                                                # -----------------------------
                                                                                             # *          [[2. 4.]
                                                                                                        #  [5. 3.]] 
                                                                                                # -----------------------------
                                                                                                        # [[a = 20. b = 26.]
                                                                                                        #  [c = 48. d = 40.]]

                                                                                        # Proceso de multiplicacion es matrices:
                                                                                            # a = (5 * 2) + (2 * 5)
                                                                                            # b = (5 * 4) + ( 2 * 3)
                                                                                            # c = (4 * 2) + (8 * 5)
                                                                                            # d = (4 * 4) + (8 * 3)




print(c, "\n-----------------------------")                                                
print(d, "\n-----------------------------")

# tambien se puede usar dot pero no es recomendado
print(c.dot(d))


'''Pero para multiplicar matrices es mejor el operador at @, es mas legible y mas fiable'''
print(c @ d)

#-----------------------------------------------------------------------------------------------------------

## Multiplicar un array ndimensional con uno unidimensional
print("PRODUCTO DE MATRICES DE DIFERENTES DIMENSIONES: ")

e = np.array([[0,1,4], [5,2,3], [1,4,8]], dtype=float)
f = np.array([2,3,5], dtype=float)
print(e, "\n--------------------------------")
print(f, "\n--------------------------------")
'''Formas de multiplicarlo: '''
np.dot(e,f)
e @ f
print(np.matmul(e, f))

#-----------------------------------------------------------------------------------------------------------
'''el determinante es el resultado de la multiplicacion de la diagonal y esta se le resta
la multiplicacion de todos los que no son de la diagonal'''
## Determinante de una matriz
g = np.array([[8,5], [3,4]])
print(g, "\n------------------------------")
print(np.linalg.det(g))

#-----------------------------------------------------------------------------------------------------------

## Auto-valores y auto-vectores
valores, vectores = np.linalg.eig(g)
print(valores, "\n--------------------------")
print(vectores, "\n--------------------------")
