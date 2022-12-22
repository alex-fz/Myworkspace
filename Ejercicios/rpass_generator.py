#!/usr/bin/env python3

try: 
    from multiprocessing import Pool
    import sys
    import os
    import numpy as np
    import string
    import csv
except:
    raise 'Some module con\'t be loaded'

### generate a series of random passwords and store the in a csv file as key, value
### and execute all with threads

def generate_random_password(num_passwords):

    my_strings = string.ascii_letters + string.digits + string.punctuation
    dict_of_passwords = {}
    for v in range(num_passwords):
        for i in range(np.random.randint(7,20)):
            try:
                dict_of_passwords[v] += my_strings[np.random.randint(0,len(my_strings))]
            except:
                dict_of_passwords[v] = my_strings[np.random.randint(0,len(my_strings))]

    return dict_of_passwords


def create_csv_file(generated_dict):
    assert type(generated_dict) == dict, 'This is not a dictionary'
    with open(os.path.join(os.path.dirname(__file__), 'random_passwords.csv'), 'w+') as file:
        fieldnames = ['Number', 'password']
        a_writer = csv.DictWriter(file, fieldnames=fieldnames)
        a_writer.writeheader()
        for key, value in generated_dict.items():
            a_writer.writerow({'Number':key, 'password':value})


def main():
    p = Pool(3)
    the_dictionary_pass = p.apply(generate_random_password, (3,))
    create_csv_file(the_dictionary_pass)
    p.close()
    p.join()
    sys.exit(0)
    

if __name__ == '__main__':
    main()
