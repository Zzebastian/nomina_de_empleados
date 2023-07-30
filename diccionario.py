textos = {"agregarNombre": "\033[0mIngrese el Nombre: \033[34m\n",
            "agregarApellido": "\033[0mIngrese el Apellido: \033[34m\n",
            "agregarCategoria": """\033[0m(P)eón, (A)dministrativo o (G)erente, Sólo es posible ingresar \033[32m p a g \033[34m\n""",
            "errorCategoría": "\033[0mSolo es posible ingresar \033[32m p a g \033[0m ",
            "puestoEquivocado": "\033[0mLa categoría ingresada es incorrecta, los valores posibles son: \033[32mPeón, Administrativo o Gerente\033[0m",
            "ingresarMail": "\033[0mIngrese un email válido: \033[34m",
            "emailInvalido": "\033[0mEl mail ingresado es inválido, no se efectúan cambios",
            "preguntaPuesto": "\033[0Ingrese el puesto en el que trabajará: \033[34m",
            "verificarDatosIngresado": "\033[0m¿Son correctos los datos impresos en pantalla? s/n \033[34m",
            "procesoExitoso": "\033[0mEl proceso fue exitoso",

            "preguntaId": "\033[0mIngrese el id del empleado \033[34m",
            "idDesconocido": "\033[0mEl id ingresado no pertenece a la base de datos \n ",
            
            "eliminarEmpleado?": "\033[0m¿Realmente desea eliminar el empleado? (S/N)\nEl proceso de eliminación es irreversible \033[34m",
            "empleadoYaEliminado": "\033[0mEl empleado ha sido eliminado previamente",
            "sinCambios": "\n\033[0mNo se han realizado cambios en la base de datos",
            "empleadoEliminado": "\033[0mEmmpleado Eliminado \n",
            "exit": "\033[32mGracias por utilizar la Base de datos\033[0m",
            
            "BdD_Cerrada": "\033[0mLa conexión a la Base de Datos ha sido cerrada",
            "presionaEnter": "\033[0m\nPresiona Enter para continuar",
            }
            # diccionario.textos[""]
puestos = {"p": "Peón",
           "a": "Administrativo",
           "g": "Gerente",
           }

tabla = ("id", "Nombre", "Apellido", "Puesto", "mail")

entrada = {"Inicial": "\nQué desea hacer? \n ",
            "Agregar": "1) Agregar Empleado",
            "Actualizar": "2) Actualizar Empleado",
            "Borrar": "3) Borrar Empleado",
            "Ver": "4) Ver Base de Datos",
            "Salir": "S) Salir",
            "Opciones": {'agregar' :"1", 'actualizar' :"2", 'borrar': "3",
                          'ver' :"4", 'salir' :"s"},
            "Problema": "Solo \033[31m1, 2, 3 o 4 o S\033[0m son valores posibles",
            }
