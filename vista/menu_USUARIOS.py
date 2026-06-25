import os
from vista.menu_ADMINS import Mediador
mediador = Mediador()
from prettytable import *

class Menu_user:
    def __init__(self, numeroUser):
        self.numeroUser = numeroUser
    def mostrarMenu(self):
        os.system("cls")
        print("####################### MENÚ USUARIOS #######################")
        print(" 1.- Reservar un paquete turístico\n 2.- Ver reservas\n 3.- Cerrar sesión ")
        print("#############################################################")
        seleccion = input("Elija una opción:  ")
        self.procesarEleccion(seleccion)




    def procesarEleccion(self, seleccion):
        try:
            seleccion = int(seleccion)
        except: 
            print("Ingrese un número entero.")
            input("ENTER para continuar...")
            self.mostrarMenu()
        else:
            if seleccion == 1:
                self.formularioReservas()
                self.mostrarMenu()
            elif seleccion == 2:
                self.listarReservasUsuario()
                self.mostrarMenu()
            elif seleccion == 3:
                print("¿Cerrar sesión?")
                confirmacion = input("(S | N):  ")
                confirmacion = confirmacion.strip().upper()
                if confirmacion == "N":
                    self.mostrarMenu()
                elif confirmacion == "S":
                    print("Cerrando sesión...")
                    input("ENTER para continuar...")
                    return
            else: 
                print("Ingrese solo las opciones disponibles.")
                input("ENTER para continuar...")



#####################################
    def listarReservasUsuario(self):
        id_usuario = self.numeroUser
        hay_reservas = mediador.verificarSiHay(id_usuario)
        if not hay_reservas:
            self.mensajes("error", "no.reservas")
            return
        username = mediador.obtenerNombre(id_usuario)
        columnas, filas = mediador.mostrarReservas(id_usuario)
        print(f"========== RESERVAS DE {username} ==========")
        tabla = PrettyTable()
        tabla.field_names = columnas 
        for fila in filas:
            tabla.add_row(fila)
        print(tabla) 
        input("ENTER para continuar...")








    def formularioReservas(self):
        self.listarPaquetes()
        id_paquete = input("Ingrese la ID del paquete que desea reservar o 's' si desea volver: ")
        if id_paquete == 's':
            return
        id_usuario = self.numeroUser
        tipo, codigo = mediador.reservarPaquete(id_paquete, id_usuario)
        self.mensajes(tipo, codigo)


    def mensajes(self, tipo, codigo):
        if tipo == "error":
            if codigo == "reserva.fallida":
                print("⁉️ No se pudo crear la reserva.")
                input("ENTER para continuar...")
            elif codigo == "no.reservas":
                print("⁉️ No hay ninguna reserva asociada al usuario")
                input("ENTER para continuar...")
        elif tipo == "exito":
            if codigo == "reserva.crear":
                print("✅ La reserva se realizó con éxito")
                input("ENTER para continuar...")

    def listarPaquetes(self):
        os.system("cls")
        id_usuario = self.numeroUser
        columnas, filas = mediador.obtenerPaquetesDisp(id_usuario)
        if len(filas) == 0:
            print("⚠️ Actualmente no existen paquetes turísticos registrados o el usuario \n reservó todo el contenido disponible")
            input("ENTER para continuar")
            return

        print("========== PAQUETES TURÍSTICOS DISPONIBLES ==========")
        tabla = PrettyTable()
        tabla.field_names = columnas 
        for fila in filas:
            tabla.add_row(fila)
        print(tabla) 