#!/usr/bin/env python3

# def check_season(month):
#     seasons = {"otoño":["septiembre", "octubre", "noviembre", "otoño"],
#                 "invierno":["diciembre", "enero", "febrero", "invierno"],
#                 "primavera":["marzo", "abril", "mayo", "primavera"],
#                 "verano":["junio", "julio", "agosto", "verano"]}
    
#     for key, values in seasons.items():
#         if month.lower() in values:
#             print("Estamos en {}.".format(key))

# check_season("enero")

import numpy as np

def factorial(number:int):
    assert number > 0, "El numero debe ser mayor de 0"

    list_mult = [v for v in range(1, number+1)]
    number = np.prod(list_mult)
    print(number)

if __name__ == "__main__":
    factorial(6)
