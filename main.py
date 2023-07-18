import json

try:
  with open("Datos_Empleados.json") as file:
    BdD = json.load(file)
except:
  BdD ={}

def _cargarDatosJSON(BdD):
  with open("Datos_Empleados.json", "w") as file:
    json.dump(BdD, file)
#
def _verificarAccion(text):
  while True:
    data = input(text)
    print(f"\033[0mEstás seguro que {data} es el valor deseado?")
    print("Ingrese cualquier tecla ara continuar o\033[32m n\033[0m")
    verif = input("->")
    if verif.lower() != "n":
      return data
      break
    print("Re-escríbelo por favor")
#
def _opcionMultiple(text, opciones = ["s", "n"], siError ="solo (s)i y (n)o son opciones válidas"):
  while True:
    opcion = input(text).strip()
    if opcion.lower() not in opciones:
      print(siError)
    else:
      break
  return (opcion)
# 
def _verificarEmail():
  while True:
    mail = input("Ingrese un email válido: \033[34m")
    print(" \033[0m")
    ch1=mail.find("@")
    ch2=mail.find(".com")
    if ch1 > 0 and ch2 > ch1 + 1:
      break
    print("email invalido")
  return mail
#
def _actualizarDiccionarioJSON(id,BdD):
  for key in BdD[id].keys():
    text = f"Desea modificar el {key}: "
    conf = _opcionMultiple(text)
    if conf == "s":
      text = f"Ingrese el nuevo {key}: \033[34m"
      BdD[id][key] = _verificarAccion(text)
#
def agregarEmpleado():
  global BdD
  id = len(BdD) + 1
  text = "Ingrese el Nombre: \033[34m"
  nombre = _verificarAccion(text)
  text = "Ingrese el Apellido: \033[34m"
  apellido = _verificarAccion(text)
  print("Ingrese el puesto en el que trabajará: ")
  puesto = _opcionMultiple("(P)eon, (A)dministrativo (G)erente", "Sólo es posible ingresar \033[32m p a g\033[0m")
  mail = _verificarEmail()
  empleado = {"Nombre": nombre,
              "Apellido": apellido,
              "Puesto": puesto,
              "mail": mail,
             }
  BdD[id] = empleado
  _cargarDatosJSON(BdD)
  print("El proceso fue exitoso")
  for data in BdD[id]:
    print(f"{data:<10} | {empleado[data]}")
#
def actualizarEmpleado():
  global BdD
  while True:
    try:
      id = input("Ingrese el id del empleado ")
      id = int(id)
      ID = str(id)
      if BdD[ID] == None:
        print("")
        print("Empleado Eliminado")
        print("")
        break
    except:
      continue
    if id <= len(BdD)+1 and id > 0:
      text= f"""Desea modificar los datos correpondientes a {BdD[ID]["Nombre"]}, {BdD[ID]["Apellido"]} """
      conf= _opcionMultiple(text)
      if conf == "s":
        _actualizarDiccionarioJSON(ID,BdD)
        _cargarDatosJSON(BdD)
        print("El proceso fue exitoso")
        for key in BdD[ID].keys():
          print(f"{key:<10} | {BdD[ID][key]}")
        break   
      else:
        print("No se han realizado cambios en la base de datos")
        break
    else:
      continue
#
def borrarUsuario():
  global BdD
  while True:
    try:
      id = input("Ingrese el id del empleado ")
      id = int(id)
      ID = str(id)
      if BdD[ID] == None:
        print("")
        print("Empleado Eliminado")
        print("")
        break
    except:
      continue
    if id <= len(BdD)+1 and id > 0:
      text= f"""Desea eliminar a {BdD[ID]["Nombre"]}, {BdD[ID]["Apellido"]} """
      conf= _opcionMultiple(text)
      if conf == "s":
        BdD[ID] = None
        _cargarDatosJSON(BdD)
        print("El proceso eliminación fue exitoso")
        break
      else:
        print("No se han realizado cambios en la base de datos")
        break
    else:
      continue
#
def verBdD():
  global BdD
  for id in BdD.keys():
    ID = str(id)
    if BdD[ID] == None:
      continue
    text = "ID"
    print(f"{text:<10} | {id}")
    for key in BdD[ID].keys():
      print(f"{key:<10} | {BdD[ID][key]}")
    print("")
#
def opcionesIniciales():
    while True:
        print("Qué desea hacer?")
        print("1) Agregar Empleado")
        print("2) Actualizar Empledo")
        print("3) Borrar Empleado")
        print("4) Ver Base de Datos")
        print("S) Salir")
        opcion = _opcionMultiple("-> ", ["1", "2", "3", "4", "s"], "Solo \033[31m1, 2, 3 o 4 o S\033[0m son valores posibles")
        if opcion == "1":
            agregarEmpleado()
        elif opcion == "2":
            actualizarEmpleado()
        elif opcion == "3":
            borrarUsuario()
        elif opcion == "4":
            verBdD()
        else:
            print("Gracias por utilizar la Base de datos")
            break
#
opcionesIniciales()

