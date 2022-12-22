#!usr/bin/env python3


def return_popular_word(file):
    '''This function will return the most popular word of a file'''
    contain_words_appear = {}
    with open(file, 'r') as my_file:
        for words in my_file.readlines():
            try:
                contain_words_appear[words.replace('\n', '')] += 1
            except KeyError:
                contain_words_appear[words.replace('\n', '')] = 1
        my_file.close()

    return max(contain_words_appear.items())

def decorate_output(funcion):
    print('la palabra mas aparecida es: {} y aparece un total de {} veces'.format(funcion[0], funcion[1]))


decorate_output(return_popular_word('/home/zardix/Documents/Programacion/palabras.txt'))