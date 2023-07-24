# Archivo que recrea la base de datos original en caso de necesitarse
import sqlite3

conexion = sqlite3.connect('nomina_de_empleados/Datos_de_Empleados.db')
cursor = conexion.cursor()

# Archivo JSON original
Datos = {"1": {"Nombre": "John", "Apellido": "Doe", "Puesto": "Peón", "mail": "john.doe@example.com"},
        "2":{"Nombre": "Michael", "Apellido": "Johnson", "Puesto": "Peón", "mail": "michael.johnson@example.com"}, 
        "3": {"Nombre": "Emily", "Apellido": "Brown", "Puesto": "Gerente", "mail": "emily.brown@example.com"}, 
        "4":{"Nombre": "Daniel", "Apellido": "Wilson", "Puesto": "Administrativo", "mail": "daniel.wilson@example.com"}}

cursor.execute('DROP TABLE IF EXISTS datos_empleados')

# Se crea la tabla que contendrá los elementos
cursor.execute('CREATE TABLE datos_empleados \
            (idEmpleado INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(15) NOT NULL, \
            apellido VARCHAR(15) NOT NULL, puesto TEXT CHECK(puesto IN ("Peón", "Administrativo", "Gerente")) NOT NULL, \
            mail VARCHAR(25) NOT NULL)')

# Se colocan los elementos en la tabla
for key in Datos:
    cursor.execute(f'INSERT INTO datos_empleados (nombre, apellido, puesto, mail) \
                VALUES ("{Datos[key]["Nombre"]}", "{Datos[key]["Apellido"]}", "{Datos[key]["Puesto"]}", "{Datos[key]["mail"]}")')
conexion.commit()
conexion.close()
