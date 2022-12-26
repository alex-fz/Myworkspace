#!/usr/bin/env python3

try:
    import math
    import pandas as pd
    import numpy as np
    import os 
    import sys
    import logging
    import datetime

except Exception as error:
    print("Error: %s"%error)

# Set work paths
dir_path = os.path.dirname(__file__)

# Set logging config
logging.basicConfig(filename=os.path.join(dir_path, "logs_testt1.log"), filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


### CREATE CLASS FOR CREATE SPECIAL DICTIONARYS

class DictionClass():
    
    colors = ["Orange", "Yellow", "Black", "White", "Blue", "Purple",
            "Green", "Red", "Gray", "Brown", "Pink"]


    def __init__(self, list_names:list):
        self.list_names = list_names

    def random_dictionary(self):
        dict_complete = {}

        for name in self.list_names:
            random_date = datetime.datetime(np.random.randint(1940, 2022), 
                                            np.random.randint(1,12), np.random.randint(1,31)).date()

            random_color = np.random.choice(self.colors)
            random_age = np.random.randint(1,100)
            dict_complete[name] = (random_date.strftime("%Y/%m/%d"), random_color, random_age)
        
        return dict_complete

### CREATE CLASS FOR  CREATE WITH PANDAS AND CSV


class WorkPandas():
    def __init__(self, dictionary:dict):
        self.dictionary = dictionary

    def CreateCsv(self):
        df = pd.DataFrame.from_dict(self.dictionary)
        df.to_csv(os.path.join(dir_path, "work_dic.csv"))






def main():

    #Set a test list names
    test_names = ["Alex", "Lorena", "Pepe", "Ibai", "Destru"]
    
    #Create an instance For the DictionClass with the test_names list
    #And a random dictionary
    creator = DictionClass(list_names=test_names)
    a_dictionary = creator.random_dictionary()
    
    #With the random dictionary create an istance for the work pandas class 
    #And create a csv
    pandas_work = WorkPandas(a_dictionary)
    pandas_work.CreateCsv()





if __name__ == "__main__":
    main()


