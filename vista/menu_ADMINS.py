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
            input("ENTER para continuar...")
        elif error == "producto.fallo.crear":
            print("⁉️ Ocurrió un error al crear el producto.")
            input("ENTER para continuar...")
        elif error == "producto.existente.barra":
            print("⁉️ Ya existe un producto con este código de barras\n💡Será devuelto al menú. Asegúrese de digitar el código de barras correspondiente al producto")
            input("ENTER para continuar...")           
    
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
        codigo_B = input("Digite codigo de barras: ")
        tipo, codigo = self.mediador.validarCodigoBarra(codigo_B)
        if tipo == "error":
            self.mensajeError("producto.existente.barra")
            return
        tipo = self.mediador.crearProducto(codigo_B, nombre, precio, desc)
        if tipo == "error":
            self.mensajeError("producto.fallo.crear")
        else:
            self.mensajeExito("producto.crear")
