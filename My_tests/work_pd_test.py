#!/usr/bin/env python3

import work_pd_csv as wps
import cProfile
import time
import unittest
import timeit
from memory_profiler import profile



if __name__ == '__main__':
    test_list_2 = ['Patata', 'Spiderman', 'Thor']
    
    #profile all

    #cProfile.run('wps.work_with_pandas(wps.create_csv(wps.create_dictionary(lista=test_list_2)))')
    
    # time all

    '''start_time = time.time()
    wps.work_with_pandas(wps.create_csv(wps.create_dictionary(lista=test_list_2)))
    final_time = time.time() - start_time
    print(final_time)'''

    # time 10000 times with timeit
    stmt = ''
    stup = '''import work_pd_csv as wps;test_list_2 = ['Patata', 'Spiderman', 'Thor'] ;wps.work_with_pandas(wps.create_csv(wps.create_dictionary(lista=test_list_2)))
                '''

    #print(timeit.timeit( setup=stup, number=1000000 ))

    wps.main(test_list_2)

