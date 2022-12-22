#!/usr/bin/env python3

try:
    import subprocess
    import os
    import sys
    from time import sleep
    from threading import Thread
    from my_inter_shell import display_info, select_path ### Delete this only test
    import logging
except Exception as error:
    print(error)
    sys.exit(1)

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'python_shell.log'), filemode='a', 
                    level=logging.INFO, format='%(asctime)s %(levelneme)s %(message)s')


def options():
    '''All the options available in the program, it force the user to select
    aomething in the allowed list'''

    sleep(1)
    allowed = ['copy', 'move', 'git automated', 'delete', 'create', 'exit', 'cat', 'display info']

    while True:
        for v in allowed: print(v)
        selection = input('Input the option that you want to execute: ').lower()
        if selection in allowed:
            break
        else:
            print('That\'s not a valid option')

    return selection


### Copy option
def copy_path(dict_of_display):
    '''this is the copy option, display all the content of the dictionary
    that must be passed of parameter and the user select the file or dir
    he wants to copy, the the program ask the user a path destination 
    for the copy file, also the user have the option for cancel the copy'''


    assert type(dict_of_display) == dict, logging.error('Assertion error produced in copy_path')
    print('Select what you want to copy')

    for k, v in dict_of_display.items(): print(str(k) + '----' + v)
    selection = int(input('Select the number of the path you want to copy: '))
    copy_path = dict_of_display.get(selection)

    print('Select the destination path')
    the_dest_path = select_path()

    while True:
        sleep(1)
        selection_2 = input('Are you sure that you want to copy:\n---{}--- \nto\n---{}---\n[yes/no]: '.format(copy_path, the_dest_path)).lower()
        if selection_2 == 'yes':
            subprocess.run(['cp', copy_path, the_dest_path])
            print('succesful')
            break
        else:
            break


### Move option
def move_path(dict_of_display):
    '''This is the move option, display all the content of the dictionary
    that must be passed as parameter, the user select the file he want to move
    and then it selcts the path of destination also the user have the option
    to cancel the move'''


    assert type(dict_of_display) == dict, logging.error('Assertion error produced in move_path')
    print('Select what you want to copy')

    for k, v in dict_of_display.items(): print(str(k) + '----' + v)
    selection = int(input('Select the number of the path you want to move: '))
    move_path = dict_of_display.get(selection)

    print('Select the sestination path')
    the_dest_path = select_path()

    while True:
        sleep(1)
        selection_2 = input('Are you sure that you want to move:\n---{}--- \nto\n---{}---\n[yes/no]: '.format(move_path, the_dest_path)).lower()
        if selection_2 == 'yes':
            subprocess.run(['mv', move_path, the_dest_path])
            print('succesful')
            break
        else:
            break


### create option
def create_file_or_dir(work_path):
    '''This is the create option, it requires a work path as parameter
    where is the file or dir it will be created, this function ask the user
    if he wants to create a directory, a file or exit, in function of he what
    input the program will execute the mkdir command or touch command + the path
    of work'''
    
    exit = False
    while not exit:
        selection = input('Do you want create a file or a directory?[dir/file/exit]: ').lower()
        match selection:
            case 'dir':
                print('Ok you are going to create a directory')
                exit = True
            case 'file':
                print('Ok you are going to create a file')
                exit = True
            case 'exit':
                exit = True
            case _:
                print('That\'s not a valid option')
                continue
    #####
    os.chdir(work_path)
    match selection:
        case 'dir':
            name_dir = input('The name of your directory: ')
            subprocess.run(['mkdir', name_dir])
            print('The directory was succesfully created')
        case 'file':
            name_file = input('The name of your file: ')
            subprocess.run(['touch', name_file])
            print('The file was succesfully created')
        case 'exit':
            pass


### delete option
def delete(dict_of_display):
    '''This is the delete option, it display all the content of the dictionary
    that must be passed as parameter and, the user seleect the file he want to delete
    if he say yes it will delete the file'''


    assert type(dict_of_display) == dict, logging.error('Assertion error produced in delete function')
    for key, value in dict_of_display.items(): print(str(key) + '----' + value)
    selection = int(input('Select the number of the file you want to delete: '))
    delete_path = dict_of_display.get(selection)

    if input('Are you sure you want to delete the file:\n{}\n[yes/no]'.format(os.path.basename(delete_path))).lower() == 'yes':
        subprocess.run(['rm', delete_path])
        print(f'Succesfully deleted the file {os.path.basename(delete_path)}')
    else:
        pass

### cat option
def cat(dict_of_display):
    '''This is the cat function it display all the content of the dictionary that must be passed
    as parameter, the user select the file and it will display the content of the file'''


    assert type(dict_of_display) == dict, logging.error('Assertion error produced in cat function')

    for key, value in dict_of_display.items(): print(str(key) + '----' + str(os.path.basename(value)))
    selection = int(input('Select the number you wan to cat:  '))
    cat_path = dict_of_display.get(selection)

    if input('Are you sure you wan to cat the file:\n{}\n[yes/no]'.format(os.path.basename(cat_path))) == 'yes':
        subprocess.run(['cat', cat_path])
    else:
        pass


