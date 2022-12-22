#!/usr/bin/env python3

try:
    import sys
    import cProfile

except ImportError:
    print('No se pudo importar el modulo')
    sys.exit(1)

'''intentar usar diccionarios, clases y hacer algo un poco complejo con la busqueda binaria'''

class Bisect():

    def __init__(self):
        pass

    def bisect_recursive(self, lista, key):
        assert type(lista) == list, 'The parameter must be a list'
        lista.sort()
        left = 0
        right = len(lista)
        steps = 0 
        while True:
            middle = (left + right) // 2
            steps += 1
            print(middle)

            if len(lista) == 0:
                print(lista)
                return 'No se encontro la key tras {} pasos'.format(steps); 
            
            elif lista[middle] == key:
                print(lista)
                return 'ya encontramos la key tras {} pasos'.format(steps)
            
            elif lista[middle] > key: 
                # remove right
                print('rr')
                print(lista)
                return self.bisect_recursive(lista[:middle], key); 
            
            elif lista[middle] < key:
                # remove left
                print('rl')
                print(lista) 
                return self.bisect_recursive(lista[middle+1:], key)
            else:
                break
        return sys.exit(1)
        
    def binary_normal_search(self, lista, key):
        assert type(lista) == list, 'The paramater must be a list'
        lista.sort()
        left = 0
        right = len(lista)
        steps = 0
        print(lista)
        while left <= right:
            steps += 1
            middle = (left + right) // 2

            if lista[middle] == key: print(middle); return 'Se encontro la key tras {} pasos'.format(steps)
            elif lista[middle] < key: print(middle); left = middle + 1
            elif lista[middle] > key: print(middle); right = middle -1
        
        return 'No se encontro la key tras {} pasos'.format(steps)
            
    def linear_search(self, lista, key):
        for value in lista:
            if value == key: return 'Se encontro la key'
        
        return 'No se encontro la key'

        




lista_a_revisar = [v for v in range(1, 1000)]
if __name__ == '__main__':
    my_search = Bisect()
    print(my_search.linear_search(lista_a_revisar, 777))
    print(my_search.bisect_recursive(lista_a_revisar, 777))
    print(my_search.binary_normal_search(lista_a_revisar, 777))
    cProfile.run('my_search.binary_normal_search(lista_a_revisar, 777)', filename=None, sort=-1)
