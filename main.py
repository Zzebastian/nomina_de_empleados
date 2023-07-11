import os

BdD = []

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
def _opcionMultiple(text, opciones = ["y", "n"], siError ="Only (y)es and (n)o are available options"):
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
def agregarUsuario():
  global BdD
  id = len(BdD) + 1
  text = "Ingrese el Nombre: \033[34m"
  nombre = _verificarAccion(text)
  text = "Ingrese el Apellido: \033[34m"
  apellido = _verificarAccion(text)
  print("Ingrese el puesto en el que trabajará")
  puesto = _opcionMultiple("(P)eon, (A)dministrativo (G)erente", "Sólo es posible ingresar \033[32m p a g\033[0m")
  mail = _verificarEmail()
  empleado = {"Id": id,
              "Nombre": nombre,
              "Apellido": apellido,
              "Puesto": puesto,
              "mail": mail,
             }
  BdD.append(empleado)
  print("El proceso fue exitoso")
  for data in empleado:
    print(f"{data:<10} | {empleado[data]}")
#
def actualizarUsuario():
  global BdD
  while True:
    try:
      id = input("Ingrese el id del empleado ")
      id = int(id)
      if id <= len(BdD)+1 and id > 0:
        print("seguir acá")
        ####################
        break
      else:
        continue
    except:
      continue
#
#borrarUsuario()
#
# verBdD()
#
def opcionesIniciales():
    while True:
        print("Qué desea hacer?")
        print("1) Agregar Usuario")
        print("2) Actualizar Usuario")
        print("3) Borrar Usuario")
        print("4) Ver Base de Datos")
        print("S) Salir")
        opcion = _opcionMultiple("-> ", ["1", "2", "3", "4", "5"], "Solo \033[31m1, 2, 3 o 4 o 5\033[0m son valores posibles")
        if opcion == "1":
            agregarUsuario()
        # elif opcion == "2":
        #     actualizarUsuario()
        # elif opcion == "3":
        #     borrarUsuario()
        # elif opcion == "4":
        #     verBdD()
        else:
            print("Gracias por utilizar la Base de datos")
            break
#
