import os
from vista.menu_ADMINS import Mediador
mediador = Mediador()
from prettytable import *

class Menu_user:
    def __init__(self, email):
        self.email = email

    def getNombre(self):
        nombre = mediador.getNombre(self.email)
        if nombre == "error":
            print("⁉️ Algo salió mal")
            input("ENTER para volver al menú principal...")
            return
        self.mostrarMenu(nombre)

    def mostrarMenu(self, nombre):
        os.system("cls")
        print("####################### MENÚ USUARIOS #######################")
        print(" 1.- Listar Pedidos\n 2.- Hacer un pedido\n 3.- Cancelar Pedido (Borrar)\n 4.- Cambiar fecha de entrega de un pedido (Editar)\n 5.- Cerrar sesión ")
        print("#############################################################")
        seleccion = input("Elija una opción:  ")
        self.procesarEleccion(seleccion, nombre)




    def procesarEleccion(self, seleccion, nombre):
        try:
            seleccion = int(seleccion)
        except: 
            print("Ingrese un número entero.")
            input("ENTER para continuar...")
            self.mostrarMenu(nombre)
        else:
            if seleccion == 1:
                pass
                self.mostrarMenu(nombre)
            elif seleccion == 2:
                self.formularioPedidos()
                self.mostrarMenu(nombre)
            #######AGREGAR 3 Y 4
            elif seleccion == 5:
                print("¿Cerrar sesión?")
                confirmacion = input("(S | N):  ")
                confirmacion = confirmacion.strip().upper()
                if confirmacion == "N":
                    self.mostrarMenu(nombre)
                elif confirmacion == "S":
                    print("Cerrando sesión...")
                    input("ENTER para continuar...")
                    return
            else: 
                print("Ingrese solo las opciones disponibles.")
                input("ENTER para continuar...")
                self.mostrarMenu(nombre)


#################################################
##########  FORMULARIOS PARA OPERAR    ##########
#################################################

    def formularioPedidos(self):
        self.listarProductos()




#################################################
################## LISTADO ######################
#################################################
    def listarProductos(self): 
        mediador.listarProductos()



#ESTA PARTE MOVER SIEMPRE AL FINAL.
######################################################
################## MENSAJES ##########################
######################################################


