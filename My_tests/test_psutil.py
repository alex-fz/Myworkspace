#!/usr/bin/env python3

import psutil


free_space = [x / psutil.cpu_count()*100 for x in psutil.getloadavg()]
'''teeest only'''
print(free_space)
print(f'{free_space} this is your free space on disk')

def obtain_process(process):
    '''function for verify if a proccess passed is running
    also prints info of the process'''
    for p in psutil.process_iter():
        if p.name() == process:
            return p
    return 'No se encontro'


def cpu_utilization(times, time):
    '''function for prints the cpu percent usage
    the times and the time as the user wants, also
    if the parameters is not in range of 1 to 100
    it will give an assertion error'''
    assert times and time in range(1,100)
    while times > 0:
        print(psutil.cpu_percent(time))
        times -= 1

def temperatures():
    '''function for print the current temperature 
    of the pc'''
    my_temperatures = psutil.sensors_temperatures()
    print(my_temperatures.keys())
    eleccion = input('que temperatura desea mirar: ')
    print(f'la temperatura actual es de: {my_temperatures[eleccion][0][1]} ºC')

temperatures()

if __name__ == '__main__':
    print(obtain_process('bash'))
    cpu_utilization(times=5, time=2)
    temperatures()
