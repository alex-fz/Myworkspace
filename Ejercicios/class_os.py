#!/usr/bin/env python3

import os
import cProfile
import timeit

class MyPath():
    current_path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.work_path = ''

    @classmethod
    def show_file_path(cls):
        print('|||   {}   |||'.format(MyPath.current_path))

    
    def read_files_on_path(self):
        while True:
            self.work_path = os.path.pardir
            if os.path.exists(self.work_path):
                for dirpath, dirname, filenames in os.walk(self.work_path):
                    for fi in filenames:
                        if fi.endswith('.py'):
                            print(str(dirname) + '---' + fi)
                break

            else:
                pass


				

if __name__ == '__main__':
    files = MyPath()
    files.read_files_on_path()
    cProfile.run('files.read_files_on_path()')
    print(timeit.timeit('files.read_files_on_path()', 'from __main__ import files, MyPath', number=100))
    print('testing my neovim terminal')

