#!/usr/bin/env python3

import re

'''Validate a password, min len 8 characters, upper lower and
at least one character non alphanumeric, no spaces
if its valid return True else return it's not valid'''


def validate_password(password):
    '''Function for validate the password'''
    pattern = r'^[\w|\W]?.*[\W]+.*'
    encontrado = re.search(pattern, password)
    if encontrado != None and len(password) >= 8:
        return True
    else:
        return False


if __name__ == '__main__':
    print(validate_password(input('Input a password: ')))
    





