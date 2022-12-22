#!/usr/bin/env python3
import numpy as np
import sys
import random

class Personaje():
    health = 100
    x_position = random.randint(1, 500)
    y_position = random.randint(1, 500)
    def __init__(self):
        self.velocity = 3
        pass
    
    def damage_receive(self, num_damage):
        print('Ha recibido {} puntos de daño'.format(num_damage))
        self.health -= num_damage
        print('You have right know {} pints of health'.format(self.health))

    def walk(self, right_or_left, up_or_down):
        '''True = Right, False  = Left
            True = up, False = down'''
        information = 'ahora estoy en la posicion {} y de altura {}'.format(self.x_position, self.y_position)
        execute = 0
        while execute == 0:
            if right_or_left:
                self.x_position += self.velocity
                print(information)
                execute = 1
            elif right_or_left == False:
                self.x_position -= self.velocity
                print(information)
                execute = 1
            else:
                self.x_position 
                print(information)
                sys.exit(0)
                
            if up_or_down:
                self.y_position += self.velocity
                print(information)
                execute = 1
            elif up_or_down == False:
                self.y_position -= self.velocity
                print(information)
                execute = 1
            else:
                self.y_position
                print(information)
                sys(exit)



class Mago(Personaje):
    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.health = 50
    
    def health_me(self):
        self.health += random.randint(1,100)



    

def main():
    character = Mago()
    for n in range(10): 
        character.walk(True, False)
        print(character.health)
        character.health_me()
        print(character.health)


if __name__ == '__main__':
    main()



        
        
