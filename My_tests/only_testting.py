#!/usr/bin/env python3

import cProfile
import os

var_entorno = os.environ
path_to_check = var_entorno.get('HOME') + '/Documents/Programacion'

def check_files(path_to_check):
    if os.path.isdir(path_to_check):
        for path, dirs, files in os.walk(path_to_check):
            for v in files:
                if v.endswith('.py') and len(v) < 7:
                    print(v)
    else:
        raise FileExistsError('Directory was not founded') 



cProfile.run('check_files(path_to_check)', filename=None, sort=-1)
check_files(path_to_check=path_to_check)