#!/usr/bin/env python3

try:
    import pandas as pd
    import numpy as np
    import sys
    import os
    import logging
    import psutil
    import csv

except Exception as error:
    print("Error while import: {}".format(error))


### Set path variables
dir_path = os.path.dirname(__file__)

# Create log dir, and data dir and set path
log_path = os.path.join(dir_path, "Logs")
data_path = os.path.join(dir_path, "Data")
if not os.path.exists(log_path): 
    os.mkdir(log_path)

elif not os.path.exists(data_path):
    os.mkdir(data_path)
else:
    pass

### Set BasicConfig logging
logging.basicConfig(filename=os.path.join(log_path, "log_unn.log"), filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


def ensure_data_frame(data_frame):

    if not type(data_frame) == type(pd.DataFrame()):
        raise ValueError("parameter is not a dataframe, ensure to create before")


## Main class for work 
class PdDict():
    
    def __init__(self, work_dictionary:dict):
        
        self.work_dictionary = work_dictionary
        self.data_frame = ""

    def create_data_frame(self):
        df = pd.DataFrame(self.work_dictionary)
        logging.info(msg="Created dataframe")
        self.data_frame = df
        return df

    def analize(self):
       
        ensure_data_frame(self.data_frame)
        
        self.data_frame:pd.DataFrame()
        print(self.data_frame.loc[0, 3])





if __name__ == "__main__":
    test_dict = {key + 1:[str(value) + "." + "Value", np.random.randint(1,100)] for key, value in enumerate(range(1,10))}
    instance_test = PdDict(work_dictionary=test_dict)
    instance_test.create_data_frame()
    instance_test.analize()
