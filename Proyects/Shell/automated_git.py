#!/usr/bin/env python3
try:
    import os
    import subprocess
    from multiprocessing.dummy import Pool
    import threading
    import sys

except Exception as error:
    print(error)
    sys.exit(1)


class MyGitClass(threading.Thread):
    '''Automated gits using threading by the threading module
    as atribute it will need a path were it must be the git repo'''
    def __init__(self, path_to_go):
        self.path_to_go = path_to_go
        threading.Thread.__init__(self)

    def run(self):
        '''the threading module requres the run function to work but we override
        writing our script, so it knows what to do'''
        my_bool = self.stage_part()
        self.value = my_bool
        self.commit_part(self.value)

    def stage_part(self):
        '''staging part of the automated gits, it will show the status of the repo and
        it will add all the files to the staging part, (change the return to false for no commit)'''
        os.chdir(self.path_to_go)
        subprocess.run(['git', 'status'])
        subprocess.run(['git','add','*'])
        # change this bool for commiting or not: True = commit, False = No commit
        return True


    def commit_part(self, bool):
        '''if the returned bool of the staging part is true this will commit all the staged files
        with and automated git message'''
        if bool:
            my_commit = 'Practices or tests [automated commit]'
            subprocess.run(['git','commit','-m',my_commit])


def commit(a_thread):
    '''this function is called in the main program, execute all the thread
    and waits for his finish, the parameter must be an instance of MyGitClass'''
    a_thread.start()
    a_thread.join()
    print(a_thread.value)

    

    

