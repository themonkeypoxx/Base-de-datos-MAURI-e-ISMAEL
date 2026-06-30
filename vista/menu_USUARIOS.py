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
        while True:
            print("="*75)
            self.listarProductos()
            print("="*75)
            print("💡 Escriba 'salir' si desea volver al menú.")
            codigoBarra = input("Digita el código de barras del producto que quieres agregar al pedido: ")
            if codigoBarra == "salir" or codigoBarra == "Salir":
                input("Sera redireccionado al menú.\nENTER para continuar...")
                return
            tipo, codigo = mediador.validarCodigoBarra(codigoBarra)
            if tipo == "error":
                self.mensajes(tipo, codigo)
                continue
            else:
                break
            ## Aquí más adelante (de Ismael para Ismael)- AGREGAR QUE EL USUARIO
            ## PUEDA AGREGAR CANTIDAD Y FECHA DE ENVÍO/RETIRO.
            ## LA FECHA DEL PEDIDO SE AGREGARÁ DE FORMA AUTOMÁTICA, ASÍ COMO LOS PRECIOS Y EL PRECIO TOTAL
            ######
            ## Recordatorio: LOS PRODUCTOS DENTRO DE UN PEDIDO SON SUBDOCUMENTOS
            ## (ES DECIR: Debo hacer un bucle de codigo de barra y cantidad, luego otro bucle para la fecha de retiro/entrega)

            
















#################################################
################## LISTADO ######################
#################################################
    def listarProductos(self): 
        mediador.listarProductos()












#ESTA PARTE MOVER SIEMPRE AL FINAL.
######################################################
################## MENSAJES ##########################
######################################################

    def mensajes(self, tipo, codigo):
        if tipo == "error":
            if codigo == "codigo.erroneo.barras":
                print("⁉️ El código de barras ingresado no existe o se ingresó mal.")
                input("ENTER para volver a listar productos y reintentar.")


