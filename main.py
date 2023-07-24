import os, json
os.system("cls")

import funciones, diccionario

def agregarEmpleado():
  while True:
    nombre = input(diccionario.textos["agregarNombre"])
    print("")
    apellido = input(diccionario.textos["agregarApellido"])
    print("")
    puestoKey = funciones.opcionMultiple(diccionario.textos["agregarCategoria"], ["p", "a", "g"],diccionario.textos["errorCategoría"])
    puesto = diccionario.puestos[puestoKey]
    print("")
    mail = funciones.verificarEmail()

    empleado = {"Nombre": nombre,
                "Apellido": apellido,
                "Puesto": puesto,
                "mail": mail,
              }

    for data in empleado:
      print(f"{data:<10} | {empleado[data]}")
    
    verif = funciones.opcionMultiple(diccionario.textos["verificarDatosIngresado"])
    if verif == "s":
      break

  funciones.guardarEmpleadoBdD(empleado)
  print(diccionario.textos["exito"])
#
def actualizarEmpleado():
  while True:
    try:
      emplId = input(diccionario.textos["preguntaId"])
      print("\033[0m")
      empleado = funciones.obtenerEmpleadoBdD(emplId)
    except:
      print(diccionario.textos["idErroneo"])
      continue
    
    print("\033[0m")
    print(f"""Desea modificar los datos correpondientes a {empleado["Nombre"]}, {empleado["Apellido"]}""")

    conf= funciones.opcionMultiple("->")

    if conf.lower() == "s":
      funciones.modificarEmpleado(empleado)
      print(diccionario.textos["procesoExitoso"])
      break   
    else:
      print(diccionario.textos["sinCambios"])
      break
#
def borrarEmpleado():
  while True:
    try:
      emplId = input(diccionario.textos["preguntaId"])
      print("\033[0m")
      funciones.obtenerEmpleadoBdD(emplId)
      print("")
      break
    except:
      print(diccionario.textos["idDesconocido"])
      continue
  conf = funciones.opcionMultiple(diccionario.textos["eliminarEmpleado?"])
  if conf == "s":
    funciones.borrarEmpleadoBdD(emplId)
    print(diccionario.textos["empleadoEliminado"])
  else:
    print((diccionario.textos["sinCambios"]))
#
def opcionesIniciales():
  while True:
    print("")
    print("Qué desea hacer? \n ")
    print("1) Agregar Empleado")
    print("2) Actualizar Empleado")
    print("3) Borrar Empleado")
    print("4) Ver Base de Datos")
    print("S) Salir")
    opcion = funciones.opcionMultiple("-> \033[34m", ["1", "2", "3", "4", "s"], "Solo \033[31m1, 2, 3 o 4 o S\033[0m son valores posibles")
    print("\033[0m")
    if opcion == "1":
      agregarEmpleado()
    elif opcion == "2":
      actualizarEmpleado()
    elif opcion == "3":
      borrarEmpleado()
    elif opcion == "4":
      funciones.imprimirBdD()
    else:
      print(diccionario.textos["exit"])
      break
#
opcionesIniciales()

