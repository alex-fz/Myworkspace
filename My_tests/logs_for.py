import logging
import os

logging.basicConfig(filename='testint_logging.log', filemode='w+', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def count_dictionary(dictionary:dict):
    assert type(dictionary) == dict, logging.error('An assertion error ocurred in function count_dictionary')

    for key, value in dictionary.items():
        print('ID NUMBER: ' + str(key))
        print('--------------------------')
        logging.info('the loop is executing')
        
        for k, v in value.items():
            try:
                print(k + ': ' + v)
            except TypeError:
                logging.error('A type error ocurred')
                


if __name__ == '__main__':
    name_dicts = {1: {'Name':'Alex', 'Class':'A', 'Age': 19, 'height':1.80},
                2: {'Name':'Carolina', 'Class':'C', 'Age': 23, 'height':1.58},
                3: {'Name':'Steven', 'Class': 'B', 'Age': 17, 'height':1.71},
                4: {'Name':'Lorena', 'Class':'A', 'Age': 28, 'height':1.54}}

    count_dictionary(dictionary=name_dicts)
    
    print(os.path.dirname(__file__))