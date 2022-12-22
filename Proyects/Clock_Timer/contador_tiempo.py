#!/usr/bin/env python3
import time

def my_clock():
    se_ejecuta = True
    while se_ejecuta:
        try:
            time_to_count = input('input time like this: HH:MM:SS    ')
            time_to_count = time_to_count.split(':')
            time_to_count = [int(v) for v in time_to_count]
            print(time_to_count)
            se_ejecuta = False
        except:
            print('You have input something different of a number')

    
    
    if time_to_count[0] > 24 or time_to_count[1] > 64 or time_to_count[2] > 64:
        print('The introduced data was invalid/wrong, the process will be restarted')
        return my_clock()
    else:

        print('The clock is running!')
        seconds = (time_to_count[0] * 3600) + (time_to_count[1] * 60) + (time_to_count[2])
        
        while seconds > 0:
            time.sleep(1)
            respuesta = time.strftime('%X', time.gmtime(seconds))
            print(respuesta)
            seconds -= 1
        
        print('YOUR TIME IS OVER')
            


my_clock()