#!/usr/bin/env python3
import cProfile
import timeit




def crear_diccionario(my_dict):
    assert type(my_dict) == dict, 'Esto no es un diccionario'
    aumento = 1
    for v in range(1,25):
        my_dict[v] = [v for v in range(1,aumento + 1)]
        aumento += 1
    
    return my_dict

def value_exists(my_other_dict):
    assert type(my_other_dict) == dict, 'Esto no es un diccionario'
    for key, value in my_other_dict.items():
        try:
            print(f' Key: {key} Aqui si hay indice 7 ,  {value[7]}')
        except IndexError:
            print(f' key: {key} Aqui no hay indice 7')


if __name__ == '__main__':
    empty_dict = {}
    '''cProfile.run('crear_diccionario(empty_dict)', filename=None, sort=-1)'''
    created_dict = crear_diccionario(empty_dict)
    cProfile.run('value_exists(created_dict)', filename=None, sort=-1)
    print(timeit.timeit('crear_diccionario(empty_dict)', 'from __main__ import crear_diccionario, empty_dict', number=10000))
