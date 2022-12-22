#!/usr/bin/env python3

import csv
import random
import sys

'''def my_binary_search(or_list, key):
    left = 0
    right = len(or_list) 
    or_list.sort()
    while left <= right:
        middle = (right + left) // 2
        print(middle)
        print(or_list)


        if len(or_list) == 0: break
        
        if or_list[middle] == key:
            return 'your key is {}'.format(key)
        
        if key < or_list[middle]:
            return my_binary_search(or_list[:middle], key)
        else:
            return my_binary_search(or_list[middle + 1:], key)

    return 'No se encontro'


pasar_lista = ['pepe','juan','pedro','zariel','cristian','federico','kirito']

print(my_binary_search(pasar_lista, ''))

'''


'''def another_binary(or_list, key):
    or_list.sort()
    left = 0
    right = len(or_list)
    steps = 1

    while left <= right:
        middle = (left + right) // 2
        print(middle)

        if or_list[middle] == key: return 'YA LO ENCONTRE {} me tomo {} pasos'.format(key, steps)
        if or_list[middle] < key: left = middle +1; print('ELIMINANDO LADO IZQUIERDO\n')
        if or_list[middle] > key: right = middle -1; print('ELIMINANDO LADO DERECHO\n')
        steps += 1

    return 'NO SE ENCONTRO'


lista_nums = [v for v in range(1,100000000)]
print(another_binary(lista_nums, 54689))'''


'''
class Seeker():

    def __init__(self, lista, key):
        self.lista = sorted(lista)
        self.key = key

    def binary_search(self):
        left = 0
        right = len(self.lista) - 1
        while left <= right:
            print(self.lista)
            
            middle = int((left + right) / 2)
            print(middle)
            if self.lista[middle] == self.key: return 'Se encontro la key ' + f'at index {middle - 1}'; break
            elif self.lista[middle] < self.key: print('ELIMINANDO LADO IZQUIERDO'); left = middle + 1
            elif self.lista[middle] > self.key: print('ELIMINANDO LADO DERECHO'); right = middle - 1
        

    
    def linear_search(self):
        pass



buscador = Seeker(['pepe','juan','pedro','zariel','cristian','federico','kirito'], 'pepe')
print(buscador.binary_search())
'''
    

def binary_in_csv(csv_file, key):

    list_for_search = []
    with open(csv_file , 'r') as file:
        my_reader = csv.reader(file)

        for row in my_reader:
            list_for_search.append(int(random.randint(1, 1000)))
    
    file.close()
    list_for_search.sort()
    print(list_for_search)
    left = 0
    right = len(list_for_search) - 1
    steps = 1
    se_encontro = False
    while left <= right:
        middle = (left + right) // 2
        print(middle)
        if list_for_search[middle] == key: print('se encontro despues de {} pasos'.format(steps));se_encontro = True ;break
        elif list_for_search[middle] < key: left = middle + 1; print('Borrando lado izquierdo')
        elif list_for_search[middle] > key: right = middle - 1; print('Borrando lado derecho')
        elif steps > 100:
            print('No se encontro')
            break
        steps += 1

    if se_encontro:
        pass
    else:
        print('No se encontro')
    

binary_in_csv(sys.argv[1], int(sys.argv[2]))







