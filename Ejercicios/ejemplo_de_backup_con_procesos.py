#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool
src = "/home/student-02-d54aae5a0618/data/prod/"
dest = "/home/student-02-d54aae5a0618/data/prod_backup/"

def run(dirname):

        subprocess.call(["rsync", "-arq", src+dirname, dest])


if __name__ == '__main__':
        my_dirs = []
        correct_dir = []
        for path, dirname, file in os.walk(src):
                my_dirs.append(dirname)

        for v in my_dirs:
                for a in v:
                        if os.path.isdir(src+a):
                                correct_dir.append(a)
        print(correct_dir)

        my_pool = Pool(len(correct_dir))
        my_pool.map(run, correct_dir)