import os, json

os.system("cls")

import funciones, diccionario

def agregarEmpleado():
  while True:
    nombre = input(diccionario.textos["agregarNombre"])
    apellido = input(diccionario.textos["agregarApellido"])
    
    puestoKey = funciones.opcionMultiple(diccionario.textos["agregarCategoria"], diccionario.puestos.keys(),diccionario.textos["errorCategoría"])
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
  print(diccionario.textos["procesoExitoso"])
#
def actualizarEmpleado():
  while True:
    try:
      emplId = input(diccionario.textos["preguntaId"])
      print("\033[0m")
      empleado = funciones.obtenerEmpleadoBdD(emplId)
    except:
      print(diccionario.textos["idDesconocido"])
      continue
    
    print("\033[0m")
    print(f"""Desea modificar los datos correpondientes a {empleado["Nombre"]}, {empleado["Apellido"]}""")

    conf= funciones.opcionMultiple("->")

    if conf.lower() == "s":
      funciones.modificarEmpleado(empleado)
      print(diccionario.textos["procesoExitoso"])
      for key in empleado:
        print(f'{key:<10} | {empleado[key]:<10}')
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
  #Verifica e inicializa la Base de datos en caso de ser necesario
  funciones.VerificarBdD()

  while True:
    
    print(diccionario.entrada["Inicial"])
    print(diccionario.entrada["Agregar"])
    print(diccionario.entrada["Actualizar"])
    print(diccionario.entrada["Borrar"])
    print(diccionario.entrada["Ver"])
    print(diccionario.entrada["Salir"])
    opcion = funciones.opcionMultiple("-> \033[34m", diccionario.entrada["Opciones"].values(), diccionario.entrada["Problema"])
    print("\033[0m")

    if opcion == diccionario.entrada["Opciones"]['agregar']:
      agregarEmpleado()
    elif opcion == diccionario.entrada["Opciones"]['actualizar']:
      actualizarEmpleado()
    elif opcion == diccionario.entrada["Opciones"]['borrar']:
      borrarEmpleado()
    elif opcion == diccionario.entrada["Opciones"]['ver']:
      funciones.imprimirBdD()
    else:
      funciones.cerrarBdD()
      print(diccionario.textos["exit"])
      break
#
opcionesIniciales()

