#!/usr/bin/env python3
import logging
import cProfile

logging.basicConfig()
def un_bucle(num1, num2):
    add = 1
    final = 7
    while final > 0:
        
        logging.debug('aa')
        print((num1 + add) + (num2 + add))
        final -= 1


if __name__ == '__main__':
    cProfile.run('un_bucle(1,6)')