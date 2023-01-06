#!/usr/bin/env python3

import sqlite3
import csv

# lo primero conectarse al archivo database, si no existe lo creara
conection = sqlite3.connect("test.db")

#crear cursor, es con lo que vamos a trabajar en python
cursor = conection.cursor()

###----------------------------------------------------------------------------------------------------------------------------------------------###

### INSERTAR UN REGISTRO

## creamos una tabla llamada Estudiantes  varchar para caracteres y integer para numeros, el 100 son los maximos caracteres
'''cursor.execute("CREATE TABLE estudiantes (email VARCHAR(100), carrera VARCHAR(100), nombre VARCHAR(100), edad INTEGER)")'''

# insertar un registro en la tabla
'''cursor.execute("INSERT INTO estudiantes VALUES ('pepe@gmail.com', 'Artes', 'ElPepe', '27')")'''


###----------------------------------------------------------------------------------------------------------------------------------------------###

### LEEER UN REGISTRO

# leer contenido de una tabla 
'''cursor.execute("SELECT * FROM estudiantes")         # CON SELECT * FROM tabla-deseada   cogemos todos los campos de la tabla deseada

users = cursor.fetchone()  # obtenemos una row y la guardamos en una variable 
print(users)'''

###----------------------------------------------------------------------------------------------------------------------------------------------###

### INGRESAR Y LEER VARIOS REGISTROS

'''usuarios = [
            ("aaaaa@gmail.com", "aaaa", "test1", 10),
            ("eeeee@gmail.com", "eeee", "test2", 24),
            ("ddddd@gmail.com", "dddd", "test3", 15),
            ("ccccc@gmail.com", "cccc", "test4", 12),
            ("bbbbbb@gmail.com", "bbbb", "test5", 42)]

cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", usuarios)'''   # executemany para listas con muchos datos


''''cursor.execute("SELECT * FROM estudiantes")

users = cursor.fetchall()   #obtenemos todos los registros de la tabla con fetchall
for data in users:
    print(data)'''

###----------------------------------------------------------------------------------------------------------------------------------------------###

### LEER UN CSV E INSERTARLO EN LA BD

'''with open("data_base.csv") as file:
    insert = csv.reader(file)
    cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", insert)'''


# leer 
'''cursor.execute("SELECT * FROM estudiantes")
all_data = cursor.fetchall()
print(all_data)'''






# guardar cambios con commit siempre que hagamos algun cambio, agregemos o quitemos etc
#conection.commit()

conection.close()
