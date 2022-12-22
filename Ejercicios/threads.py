from multiprocessing import Pool
import threading
from concurrent import futures
from multiprocessing import Process
Process()
###

### Modulos de multiprocessing y threads todo para mejorar la performance cuando sea necesario

###
def una_fucion():
    lista = []
    for v in range(1,1000):
        lista.append(v)
    return lista


p = Pool(4)
hola = p.apply(una_fucion)
print(len(hola))


