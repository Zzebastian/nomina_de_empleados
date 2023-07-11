# nomina_de_empleados
Este proyecto forma parte de un trabajo práctico que se construye en distintas etapas, la primera parte, es la que corresponde al siguiente enunciado

Se requiere:
Una aplicación de terminal, con un menú que conste de las siguientes opciones:

1) Agregar Usuario
2) Actualizar Usuario
3) Borrar Usuario
4) Ver Base de Datos
S) Salir

Al usuario se le va a ofrecer ese menú y va a tener un prompt para poner la opcion que busque

En el menú de agregar usuarios se le va a pedir un nombre, el cual debe ser un valor de tipo string,  un puesto de trabajo, y un email. 
el puesto de trabajo debe ser uno de los siguientes: 
Administrativo		Peon		Gerente
En caso de ingresarse otro valor, debe salir un mensaje que diga "Este es un valor incorrecto, recuerde que las opciones son Administrativo, Peon o gerente"

En el mail no hace falta que hagamos la comprobación ahora. puede ser cualquier string, en el futuro vamos a aprender cómo se hace eso de que sea si o si un formato mail
además, el programa le va a asignar un identificador numérico, que debe ir creciendo cada que agreguemos un usuario

Después, en el menú de actualizar usuario, debe pedir un id (el cual debe ser de nuestro usuario a modificar) y te va a pedir el nombre y que dejes vacío si no quieres cambiarlo, te va a pedir un puesto de trabajo y lo mismo, si dejas vacio no lo cambia, y lo mismo con el mail.  luego debe decirte los datos actualizados. y volver al menú

En borrar solo te va a pedir un usuario por id y lo va a borrar, devolviendote el nombre del usuario borrado

Y ver base de datos te va a mostrar la lista de usuarios ingresados

IMPORTANTE:

Cuando cierren el programa los datos se vana  borrar, eso es lo normal ,ya que todavía no aprendimos a generar una base de datos real, esta es sólo imaginaria
