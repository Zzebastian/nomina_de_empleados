import json

from main import diccionario

def verificarAccion(text):
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
    mail = input(diccionario["ingresarMail"])
    print(" \033[0m")
    char1=mail.find("@")
    char2=mail.find(".com")
    if char1 > 0 and char2 > char1 + 1:
      break
    print("email invalido")
  return mail
#
def actualizarDiccionarioJSON(id,BdD):
  for key in BdD[id].keys():
    print(f"Si desea modificar el {key}, ingrese el nuevo valor")
    print("""caso contrario, ingrese "enter" """)
    nuevoValor = input("->")
    if nuevoValor == 0:
      continue
    print(f"¿Es {key} el valor correcto? ingrese (s)i o (n)o")
    conf = opcionMultiple("->")
    if conf == "s":
      text = f"Ingrese el nuevo {key}: \033[34m"
      BdD[id][key] = verificarAccion(text)
#
def obtenerDatos():
    # Obtiene los datos guardados en la base de datos, o bien, en caso de no tener, crea una nueva.
    try:
        with open("nomina_de_empleados/Datos_Empleados.json") as file:
            BdD = json.load(file)
    except:
        BdD ={}
    return BdD
#
def guardarDatosJSON(BdD):
  with open("nomina_de_empleados/Datos_Empleados.json", "w") as file:
    json.dump(BdD, file)
#