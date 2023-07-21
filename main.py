import os, json
os.system("cls")
try:
  with open("nomina_de_empleados/Datos_Empleados.json") as file:
    BdD = json.load(file)
except:
  BdD ={}

textos = {"agregarNombre" : "Ingrese el Nombre: \033[34m",
            "agregarApellido" : "Ingrese el Apellido: \033[34m",
            "agregarCategoria" : """(P)eon, (A)dministrativo (G)erente", "Sólo es posible ingresar \033[32m p a g\033[0m""",
            "ingresarMail": "Ingrese un email válido: \033[34m"}

def _cargarDatosJSON(BdD):
  with open("nomina_de_empleados/Datos_Empleados.json", "w") as file:
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
    mail = input(textos["ingresarMail"])
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
    print(f"Si desea modificar el {key}, ingrese el nuevo valor")
    print("""caso contrario, ingrese "enter" """)
    nuevoValor = input("->")
    if nuevoValor == 0:
      continue
    print(f"¿Es {key} el valor correcto? ingrese (s)i o (n)o")
    conf = _opcionMultiple("->")
    if conf == "s":
      text = f"Ingrese el nuevo {key}: \033[34m"
      BdD[id][key] = _verificarAccion(text)
#
def agregarEmpleado():
  global BdD
  id = len(BdD) + 1
  
  nombre = _verificarAccion(textos["agregarNombre"])
  
  apellido = _verificarAccion(textos["agregarApellido"])
  print("Ingrese el puesto en el que trabajará: ")
  puesto = _opcionMultiple(textos["agregarCategoria"])
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
      if id > len(BdD)+1 and id <= 0:
        print("El id ingresado no pertenece a la base de datos")
        continue
      ID = str(id)
      if BdD[ID] == None:
        print("")
        print("El empleado ha sido eliminado previamente")
        print("")
        break
    except:
      print("El id ingresado debe ser un número entero positivo")
      continue
    print(f"""Desea modificar los datos correpondientes a {BdD[ID]["Nombre"]}, {BdD[ID]["Apellido"]} """)
    conf= _opcionMultiple("->")
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
#
def borrarUsuario():
  global BdD
  while True:
    try:
      userId = input("Ingrese el id del empleado ")
      userId = int(userId)
      userId_str = str(userId)
      if BdD[userId_str] == None:
        print("")
        print("Empleado Eliminado")
        print("")
        break
    except:
      continue
    if userId <= len(BdD)+1 and userId > 0:
      text= f"""Desea eliminar a {BdD[userId_str]["Nombre"]}, {BdD[userId_str]["Apellido"]} """
      conf= _opcionMultiple(text)
      if conf == "s":
        BdD[userId] = None
        _cargarDatosJSON(BdD)
        print("El proceso eliminación fue exitoso")
        break
      else:
        print("No se han realizado cambios en la base de datos")
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

