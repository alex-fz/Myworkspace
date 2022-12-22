#!/usr/bin/env python3

try:
    import pandas as pd
    import logging
    import numpy as np
    import os
    import threading
    from time import sleep
    from memory_profiler import profile

except Exception as error:
    print('Something went wrong: %s'%error)

finally:
    logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'logs_pd.log'), filemode='w+',
                    level=logging.INFO, encoding='utf-8', format='%(asctime)s %(levelname)s %(message)s')
    


class WorkCsv(threading.Thread):
    work_csv = pd.read_csv(os.path.join(os.path.dirname(__file__), 'amazon.csv'), encoding='iso-8859-1')

    logging.info(msg='Setting as class atribute the dataframe reading the csv file %s'%work_csv)

    def __init__(self):
        super(WorkCsv, self).__init__()
        self.shape = self.work_csv.shape
        self.english_months =  {'January':'','February':'','March':'','April':'','May':'','June':'',
                                            'July':'','August':'','Septembre':'','October':'','November':'','December':''}
    
    def run(self):
        logging.info(msg='Running thread and functions')
        self.obtain_months_name()
        self.change_month_name()
        self.show_info()
        

    def obtain_months_name(self):
        '''This function gets the name of the months of the csv
        it must be shorted, then it change its own dict 
        and inputs each corresponding month in his place'''
        logging.info(msg='obtain_months_name was called')

        month_braz = []
        for n in range(300):
            if self.work_csv.loc[n, 'month'] not in month_braz:
                month_braz.append(self.work_csv.loc[n, 'month'])
            elif len(month_braz) >= 12:
                break
        
        index = 0
        for key in self.english_months.keys():
            self.english_months[key] = month_braz[index]
            index += 1
    

    def change_month_name(self):
        '''before calling this function the obtain month name
        function must be called, this function change the month names'''
        logging.info(msg='change_month_name was called')


        self.obtain_months_name()

        for n in range(self.shape[0]):
            for key, value in self.english_months.items():
                if self.work_csv.loc[n, 'month'] == value:
                    self.work_csv.loc[n, 'month'] = key

    
    def store_changes_csv(self):
        logging.info(msg='store_change_csv was called')
        self.work_csv.to_csv(os.path.join(os.path.dirname(__file__), 'amazon_test_month.csv'))

    
    def show_info(self):
        logging.info(msg='show info was called')
        length_fires = self.work_csv.loc[self.work_csv['year'].between(2000,2005)].shape[0]
        print(f'there were a total of {length_fires} fires between 2000 and 2005')

        popular_state = self.work_csv.loc[self.work_csv['year'].between(2000,2005)].state.mode()
        print(f'The most appared state is {popular_state.product()}')

        worst_day = self.work_csv.loc[self.work_csv['year'].between(2000,2005)]
        worst_day = worst_day.loc[worst_day['number'].max()]
        print('The worst day was: ')
        print(worst_day)

        mean_fires = self.work_csv['number'].mean()
        print(f'The mean of the fire is {round(mean_fires, ndigits=2)}')
    


def main():
    instance_test = WorkCsv()
    logging.info(msg='Starrting main and thread...')
    instance_test.start()
    logging.info(msg='Running thread...')
    instance_test.join()
    logging.info('Thread closed')
        

if __name__ == '__main__':
    main()
    
    