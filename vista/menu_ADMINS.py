from controlador.mediador import Mediador
import os
from prettytable import *
class Menu_Admin:
    def __init__(self):
        self.mediador = Mediador()

    def mostrarMenu(self):
            while True:
                os.system("cls")
                print("################ MENÚ ADMIN ################")
                print(" 1.- Listar productos\n 2.- Crear nuevo producto\n 3.- Editar producto\n 4.- Borrar producto\n 5.- Cerrar sesión")
                print("############################################")

                eleccion = input("Seleccione lo que quiere hacer: ")
                try:
                    eleccion = int(eleccion)
                    if eleccion < 1 or eleccion > 5: 
                        print("⁉️ Ingrese un número válido.")
                        input("ENTER para continuar")
                        continue
                except ValueError:
                    print("⁉️ Ingrese números enteros solamente.")
                    input("ENTER para continuar")
                    continue
                
                break 

            if eleccion == 1:
                self.listarProductos()
                input("ENTER para continuar")
                self.mostrarMenu()
            elif eleccion == 2:
                self.formularioProductos()
                self.mostrarMenu()
            elif eleccion == 3:
                pass
                input("ENTER para volver...")
                self.mostrarMenu()
            elif eleccion == 4:
                pass
                input("ENTER para volver...")
                self.mostrarMenu()
            elif eleccion == 5:
                print("Cerrando sesión...")
                input("ENTER para continuar")
                return
            
                


#######################################################
###########           MENSAJES          ###############
#######################################################
    def mensajeError(self, error):
        os.system('cls')
        if error == "productos.nada":
            print("⁉️ No existe ningún registro aún!\n💡Será devuelto al menú. Asegúrese de agregar un producto")
            input("Enter para continuar...")
        elif error == "producto.fallo.crear":
            print("")
    
    def mensajeExito(self, exito):
        os.system('cls')
        if exito == "producto.crear":
            print("✅ Producto registrado correctamente!")
            input("Enter para continuar...")

#######################################################
################   LISTADO      #######################
#######################################################

    def listarProductos(self):
        self.mediador.listarProductos()

#######################################################
###########           CREACION          ###############
#######################################################

    def formularioProductos(self):
        os.system('cls')
        print("######### Registro de Producto ##########")
        nombre = input("Nombre producto: " )
        precio = input("Precio (CLP): $")
        desc = input("Descripcion breve: ")
        codigo = input("Digite codigo de barras: ")
        tipo = self.mediador.crearProducto(codigo, nombre, precio, desc)
        if tipo == "error":
            self.mensajeError("producto.fallo.crear")
        else:
            self.mensajeExito("producto.crear")
