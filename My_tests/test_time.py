#!/usr/bin/env python3

import datetime
import re


def ask_user_birthday():
    birthday = []
    while not len(birthday) >= 3:
        birthday.clear()
        year = input('Introduzca su año de nacimiento [DDDD]: ')
        buscar = re.search(r'^\d\d\d\d$', year)
        if buscar != None:
            birthday.append(year)
        else:
            continue
        day = input('Introduzca su mes de nacimiento [DD]: ')
        buscar = re.search(r'^\d\d?$', day)
        if buscar != None:
            birthday.append(day)
        else:
            continue
        month = input('Introduzca su dia de nacimiento [DD]: ')
        buscar = re.search(r'^\d\d?$', month)
        if buscar != None:
            birthday.append(month)
        else:
            continue
    
    return birthday
            



def calculate_date(lista):
    now = datetime.datetime.now().date()
    next_year = datetime.date(datetime.datetime.now().year + 1, int(lista[1]), int(lista[2]))
    days = next_year - now

    return f'quedan {days.days} dias para tu cumpleaños'

    

if __name__ == '__main__':
    print(calculate_date(ask_user_birthday()))
    