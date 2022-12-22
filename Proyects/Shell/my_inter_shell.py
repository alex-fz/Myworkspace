#!/usr/bin/env python3

try:
    import psutil
    import subprocess
    import os
    import sys
    from time import sleep
    from threading import Thread
    import pathlib
    import inter_shell_options as isp
    import automated_git as ag
    import logging
except Exception as error:
    print(error)
    sys.exit(1)


# for prevent errors change the dirpath to the path of the dir file
os.chdir(os.path.dirname(__file__))

# using the logging info for logs
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'python_shell.log'), filemode='w+', 
                    level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()

# Change to False for get logs
logger.disabled = False


def select_path():
    '''starts in the home path and the user type the dir he wants to go
    when he is in his desire dir when he input x it will return the path to that directory'''

    path_to_check = pathlib.Path.home()
    while True:
        sleep(1)
        try:
            os.chdir(path=path_to_check)
        except FileNotFoundError:
            path_to_check = pathlib.Path.home()
            print('That file/directory doesnt exist')
            logging.error('FileNotFounError was produced in the select path function, returning the path home for retry')

        subprocess.run(['pwd'])
        print('*'*70)
        subprocess.run(["ls"])
        print("*"*70)
        append_path = input("Input the directory or press x for set the current path:   ")
        if append_path == 'x':
            break
        else:
            path_to_check = path_to_check.joinpath(append_path)
            print(path_to_check)
    os.system('clear')

    logging.info(' The select_path function was called and Returning the path %s', path_to_check)
    return path_to_check
    


def display_info(a_path='/'):
    '''Returns a dict of the path of the file
    of the selected files'''

    os.system('clear')
    print('-'*50)
    # free_gb have the all free space in gb of the disk

    free_gb = psutil.disk_usage(a_path).free // 10**6
    # current dir path have the path of the working file

    current_dir_path = os.path.dirname(a_path)
    # this display all the contents of the current path and store them as a list

    a = subprocess.check_output(['ls', a_path], timeout=2)
    content_in_dir = str(a).replace('\\n', '\\').replace("'", "").replace("b", "").split('\\')


    dict_with_elements = {}


    ## display all the info

    print(f'There are {free_gb} free gb in the disk\nYou are working in the path: {current_dir_path}\nThe content of this path is: ')
    for i,v in enumerate(content_in_dir):
        if len(v) > 0:
            print('{}{}'.format(str(i + 1) + '.', str(v)))
            dict_with_elements[i + 1] = str(a_path) + '/' + v


    print('-'*50)
    # Return the content of the actual directory in a dictionary
    logging.info('display_info function was called, returning a dictionary: %s', dict_with_elements)
    return dict_with_elements


def main():
    '''the main program executes here i use the match and case statement
    for execute the different option, the program will run until the user
    select the option exit, also sleep 3 seconds when the function finish'''

    user_selection = 'u'
    while user_selection != 'exit':
        path_to_work = select_path()
        user_selection = isp.options()

        match user_selection:
            case 'copy':
                isp.copy_path(display_info(path_to_work)) ### from inter_shell_options.py
                sleep(3)
                logging.info('The copy case was produced in main, from inter_shell_options the copy_path function was called path working: %s', str(path_to_work))

            case 'move':
                isp.move_path(display_info(path_to_work)) ### from inter_shell_options.py
                sleep(3)
                logging.info('The move case was produced in main, from inter_shell_options the move_path function was called path working: %s', str(path_to_work))

            case 'create':
                isp.create_file_or_dir(path_to_work) ### from inter_shell_options.py
                sleep(3)
                logging.info('The create case was produced in main, from inter_shell_options the create_file_or_dir function was called path working: %s', str(path_to_work))

            case 'delete':
                isp.delete(display_info(path_to_work)) ### from inter_shell_options.py
                sleep(3)
                logging.info('The delete case was produced in main, from inter_shell_options the delete function was called path working: %s', str(path_to_work))

            case 'git automated':
                a_thread = ag.MyGitClass(path_to_work)
                ag.commit(a_thread=a_thread) ### from automated_git.py
                sleep(3)
                logging.info('The git automated case was produced in main, from automated_git the commit function was called path working: %s', str(path_to_work))

            case 'cat':
                isp.cat(display_info(path_to_work)) ### from inter_shell_options.py
                sleep(3)
                logging.info('The cat case was produced in main, from inter_shell_options the cat function was called path working: %s', str(path_to_work))

            case 'display info':
                display_info(path_to_work)
                logging.info('The display info case was produced, from my_inter_shell called the display_info function path working: %s', str(path_to_work))
                

            case 'exit':
                logging.info('The exit case was produced in main, exiting of the program...')
                break

    # in case user type exit will esit with sys.exit(0) with no problems
    sys.exit(0)


if __name__ == '__main__':
    main()
