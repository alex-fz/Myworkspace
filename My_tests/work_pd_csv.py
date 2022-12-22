#!/usr/bin/env python3

try:
    import csv
    import sys
    import re
    import os
    import logging
    import pandas as pd
    import numpy as np
    from concurrent import futures
    from memory_profiler import profile

except Exception as error:
    print('Something went wrong importing %s'%error)

# Set dirpath
dir_path = os.path.dirname(__file__)


# Set the configuration for the logs
logging.basicConfig(filename=os.path.join(dir_path, 'work_pd-csv.log'), filemode='a',
                    level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')



def create_dictionary(lista:list):
    '''Receive a list and for each element of that list
    the element will be the key of the dict and the values would be
    random numbers'''

    dict_to_return = {}

    for element in lista:
        dict_to_return[element] = [np.random.randint(1,100) for v in range(3)]

    return dict_to_return

def create_csv(dictionary:dict):
    '''Receive the complete dictionary, this will create a csv
    in this format: Name,Number1,Number2,Number3'''

    path_file_csv = os.path.join(dir_path, 'Work_pd-csv.csv')

    if os.path.exists(path_file_csv):
        print('A csv with that name already exist in that path')
        logging.error(msg='A path with a csv already exist with the name that was input')
        return path_file_csv
    else:
        mode_file = 'w+'
    
        with open(path_file_csv, mode=mode_file) as file:
            the_fieldnames = ['Name','Number1','Number2','Number3']
            writer = csv.DictWriter(f=file, fieldnames=the_fieldnames)
            writer.writeheader()

            for key, values in dictionary.items():
                writer.writerow({'Name':key,'Number1':values[0],'Number2':values[1],'Number3':values[2]})
        logging.info(msg='csv created at: %s'%path_file_csv)    
    file.close()

    return path_file_csv


def work_with_pandas(path:str):
    '''Work with the csv and pandas'''

    if not os.path.exists(path):
        raise FileNotFoundError('This path doesn\'t exist')
    
    work_pandas = pd.read_csv(filepath_or_buffer=path)
    print(work_pandas.columns)


@profile
def main(lista:list):
    executor = futures.ThreadPoolExecutor(len(lista))
    complete_dictionary = executor.submit(create_dictionary, lista).result()
    path_csv = executor.submit(create_csv, complete_dictionary).result()
    executor.submit(work_with_pandas, path_csv)
    
    

if __name__ == '__main__':
    test_list = ['Patata', 'Spiderman', 'Thor']
    main(lista=test_list)
    

