import os, json
os.system("cls")

import funciones, diccionario

BdD = funciones.obtenerDatos()

def agregarEmpleado():
  global BdD
  id = len(BdD) + 1

  nombre = funciones.verificarAccion(diccionario.textos["agregarNombre"])
  apellido = funciones.verificarAccion(diccionario.textos["agregarApellido"])
  
  print()
  puesto = funciones.opcionMultiple(diccionario.textos["agregarCategoria"])
  mail = funciones.verificarEmail()
  empleado = {"Nombre": nombre,
              "Apellido": apellido,
              "Puesto": puesto,
              "mail": mail,
             }
  
  BdD[id] = empleado
  
  funciones.guardarDatosJSON(BdD)
  print(diccionario.textos["exito"])
  for data in BdD[id]:
    print(f"{data:<10} | {empleado[data]}")
#
def actualizarEmpleado():
  global BdD

  while True:
    try:
      id = input(diccionario.textos["preguntaPuesto"])
      id = int(id)

      if id > len(BdD)+1 and id <= 0:
        print(diccionario.textos["idDesconocido"])
        continue
      ID = str(id)

      if BdD[ID] == None:
        print("")
        print("empleadoYaEliminado")
        print("")
        break
    except:
      print(diccionario.textos["idErroneo"])
      continue

    print(f"""Desea modificar los datos correpondientes a {BdD[ID]["Nombre"]}, {BdD[ID]["Apellido"]} """)
    conf= funciones.opcionMultiple("->")
    
    if conf == "s":
      funciones.actualizarDiccionarioJSON(ID,BdD)
      funciones.guardarDatosJSON(BdD)
      print(diccionario.textos["procesoExitoso"])
      for key in BdD[ID].keys():
        print(f"{key:<10} | {BdD[ID][key]}")
      break   
    else:
      print(diccionario.textos["sinCambios"])
      break
#
def borrarUsuario():
  global BdD
  
  while True:
    try:
      userId = input(diccionario.textos["preguntaId"])
      userId = int(userId)
      userId_str = str(userId)
      if BdD[userId_str] == None:
        print("")
        print(diccionario.textos["empleadoEliminado"])
        print("")
        break
    except:
      continue
    
    if userId <= len(BdD)+1 and userId > 0:
      text= f"""Desea eliminar a {BdD[userId_str]["Nombre"]}, {BdD[userId_str]["Apellido"]} """
      conf= funciones.opcionMultiple(text)
      if conf == "s":
        BdD[userId] = None
        funciones.guardarDatosJSON(BdD)
        print(diccionario.textos["procesoExitoso"])
        break
      else:
        print(diccionario.textos["sinCambios"])
        break
    else:
      continue
#
def verBdD(): #Imprime de forma atractiva la Base de datos
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
        opcion = funciones.opcionMultiple("-> ", ["1", "2", "3", "4", "s"], "Solo \033[31m1, 2, 3 o 4 o S\033[0m son valores posibles")
        
        if opcion == "1":
            agregarEmpleado()
        elif opcion == "2":
            actualizarEmpleado()
        elif opcion == "3":
            borrarUsuario()
        elif opcion == "4":
            verBdD()
        else:
            print(diccionario.textos["exit"])
            break
#
opcionesIniciales()

