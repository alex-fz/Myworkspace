#!/usr/bin/env python3

import random
import re
import sys



def show_on_screen(random_word, accert_letter):
    hidden_word = []
    for letter in random_word:
        if letter in accert_letter:
            hidden_word.append(letter)
        else:
            hidden_word.append('__')
    
    print(' '.join(hidden_word))

def eleccion_usuario():
    pattern = r'^[A-Za-z]$'
    while True:
        letter = input('Input a letter: ')
        is_valid = re.search(pattern, letter)
        if is_valid != None:
            break
        else:
            print('Su eleccion no es una letra, vuelva a introducir: ')
            pass
    
    return letter.lower()


def main(random_word):
    vidas = 8
    lista_random_sorted = sorted(list(set(random_word)))
    letras_acertadas = []
    while vidas > 0:
        show_on_screen(random_word, letras_acertadas)
        print(letras_acertadas)
        letra = eleccion_usuario()
        if letra in random_word and letra not in letras_acertadas:
            letras_acertadas.append(letra)

        else:
            print('has perdido una vida, ahora te quedan {} vidas'.format(vidas))
            vidas -= 1

        if len(lista_random_sorted) == len(letras_acertadas):
            show_on_screen(random_word, letras_acertadas)
            print('HAS GANADO')
            sys.exit(0)
        

    
    print(random_word)
    print('HAS PERDIDO')


if __name__ == '__main__':
    words_list = ['patata', 'pez', 'reloj']
    random_word = random.choice(words_list)
    main(random_word)

   