import json, sqlite3
import diccionario
pathBdD = 'nomina_de_empleados/Datos_de_Empleados.db'
# Operaciones sobre la base de datos

conexion = None

def VerificarBdD():
    # Obtiene los datos guardados en la base de datos, o bien
    # En caso de no tener, Re-crea la Base de Datos de prueba
    global conexion
    if conexion != None:
      conexion.commit()
      conexion.close()
    try:
        conexion = sqlite3.connect(pathBdD)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM datos_empleados')
        
        conexion.commit()
        conexion.close()
    except:
        import Database_Empleados
        imprimirBdD()
#
def imprimirBdD():
  conexion = sqlite3.connect(pathBdD)
  cursor = conexion.cursor()

  cursor.execute('SELECT * FROM datos_empleados')

  registros = cursor.fetchall()

  print(f"\033[32m{diccionario.tabla[0]:<10} | {diccionario.tabla[1]:<15} | {diccionario.tabla[2]:<15} | {diccionario.tabla[3]:<15} | {diccionario.tabla[4]:<10}\033[0m")

  for registro in registros:
      print(f'{registro[0]:<10} | {registro[1]:<15} | {registro[2]:<15} | {registro[3]:<15} | {registro[4]:<10}')
  
  conexion.commit()
  conexion.close()
#
def guardarEmpleadoBdD(empleado):
  conexion = sqlite3.connect(pathBdD)
  cursor = conexion.cursor()
  cursor.execute(f'INSERT INTO datos_empleados (nombre, apellido, puesto, mail) \
                  VALUES ("{empleado["Nombre"]}", "{empleado["Apellido"]}", "{empleado["Puesto"]}", "{empleado["mail"]}")')
  
  conexion.commit()
  conexion.close()
#
def obtenerEmpleadoBdD(id):
  conexion = sqlite3.connect(pathBdD)
  cursor = conexion.cursor()
  cursor.execute(f'''SELECT * FROM datos_empleados WHERE idEmpleado={id}''')
  
  registro = cursor.fetchall()
  empleado = {"ID": registro[0][0],
              "Nombre": registro[0][1],
              "Apellido": registro[0][2],
              "Puesto": registro[0][3], 
              "Mail": registro[0][4],
            }
  for data in empleado:
      print(f"{data:<10} | {empleado[data]}")
  
  conexion.commit()
  conexion.close()

  return empleado
#
def actualizarEmpleadoBdD(empleado):
  print("seguir acá")
  print(empleado)
  
  conexion = sqlite3.connect(pathBdD)
  cursor = conexion.cursor()
  cursor.execute(f'UPDATE datos_empleados SET nombre = "{empleado["Nombre"]}", apellido = "{empleado["Apellido"]}", \
                 puesto = "{empleado["Puesto"]}", mail = "{empleado["Mail"]}" \
                  WHERE idEmpleado = "{empleado["ID"]}"')
  
  conexion.commit()
  conexion.close()
#
def borrarEmpleadoBdD(id):
  conexion = sqlite3.connect(pathBdD)
  cursor = conexion.cursor()
  cursor.execute('SELECT * FROM datos_empleados')
  cursor.execute(f'DELETE FROM datos_empleados WHERE idEmpleado={id}')
  
  conexion.commit()
  conexion.close()
#

# Operaciones fuera de la base de datos
def verificarAccion(text):
  while True:
    data = input(text)
    print(f"\033[0mEstás seguro que {data} es el valor deseado?")
    print("Ingrese cualquier tecla para continuar o\033[32m n\033[0m")
    verif = input("->")
    if verif.lower() != "n":
      return data
      break
    print("Re-escríbelo por favor")
#
def opcionMultiple(text, opciones = ["s", "n"], siError ="solo (s)i y (n)o son opciones válidas"):
  while True:
    opcion = input(text).strip()
    if opcion.lower() not in opciones:
      print(siError)
    else:
      break
  return (opcion)
# 
def verificarEmail():
  while True:
    mail = input(diccionario.textos["ingresarMail"])
    print(" \033[0m")
    verif = esmail(mail)
    if verif == True:
      break
    print(diccionario.textos["emailInvalido"])
  return mail
#
def esmail(mail):
  char1=mail.find("@")
  char2=mail.find(".com")
  if char1 > 0 and char2 > char1 + 1:
    verif = True
    return verif
  else:
    verif = False
  return verif
#
def modificarEmpleado(empleado):
  for key in empleado:
    if key == 'ID':
      # empleado[key] = str(empleado[key])
      continue

    print(f"Si desea modificar el {key}, ingrese el nuevo valor")
    print("""caso contrario, ingrese "enter" """)
    
    nuevoValor = input("->")
    if nuevoValor == "":
      continue

    if key == 'Mail':
      verif = esmail(nuevoValor)
      if verif == False:
        print(diccionario.textos["emailInvalido"])
        continue
    elif key == 'Puesto':
      if nuevoValor not in diccionario.puestos.values():
        print(diccionario.textos["puestoEquivocado"])
        continue
    
    empleado[key] = nuevoValor

  actualizarEmpleadoBdD(empleado)
#
