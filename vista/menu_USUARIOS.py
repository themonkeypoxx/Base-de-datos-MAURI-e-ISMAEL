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
        print(" 1.- Listar Pedidos\n 2.- Hacer un pedido\n 3.- Cancelar Pedido (Borrar)\n 4.- Editar un pedido\n 5.- Cerrar sesión ")
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
                correo = self.email 
                self.listarPedidos(nombre, correo)
                self.mostrarMenu(nombre)
            elif seleccion == 2:
                lista_productos = []
                self.formularioPedidos(lista_productos)
                self.mostrarMenu(nombre)
            elif seleccion == 3:
                self.formularioCancelarPedido()
                self.mostrarMenu(nombre)
            elif seleccion == 4:
                self.formularioEditarPedido()
                self.mostrarMenu(nombre)
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


### para agregar pedidos
    def formularioPedidos(self, lista):
        while True:
            print("="*75)
            self.listarProductos()
            print("="*75)
            print("💡 Escriba 'salir' si desea volver al menú\nSi escribe 'salir' perderá todo su carrito.")
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
        while True:
            os.system('cls')
            print("="*75)
            ctdad_prod = input("Ingrese las unidades que encargará: ")
            try:
                ctdad_prod = int(ctdad_prod)
            except Exception:
                self.mensajes("error", "cantidad.erronea") 
                continue
            else:
                tipo, codigo = mediador.calcularPrecio(ctdad_prod, codigoBarra)
                if tipo == "error":
                    self.mensajes(tipo, codigo)
                    self.formularioPedidos(lista)
                else:
                    precio = codigo
                    producto = {"codigoBarra":codigoBarra,
                                "cantidad": ctdad_prod,
                                "precioCantidad": precio}
                    lista.append(producto)
                    break
        while True:
                    os.system('cls')
                    print("¿Desea agregar más productos al pedido?")
                    opcion = input("(S/N): ")
                    opcion = opcion.strip().capitalize()
                    if opcion == "S":
                        self.formularioPedidos(lista)
                    elif opcion == "N":
                        correo = self.email
                        precioTotal = mediador.calcuarPrecio_Total(lista)
                        if precioTotal == "error":
                            self.mensajes(precioTotal, "pedido.crear.fallo")
                            return
                        tipo, codigo = mediador.crearPedido(lista, precioTotal, correo)
                        if tipo == "error":
                            self.mensajes(tipo, codigo)
                            return
                        else:
                            self.mensajes(tipo, codigo)
                            return
                    else:
                        input("Ingrese 's' o 'n'\nENTER para volver a intentar")
                        continue
                    
    def formularioCancelarPedido(self):
        os.system('cls')
        print("cancelar pedido") 
        pedidos = mediador.obtPedidos(self.email)
        if pedidos is None:
            self.mensajes("error", "no.pedidos")
            return 
        for i, pedido in enumerate(pedidos):
            print(f"{i} - Precio total: ${pedido.get('precioTotal')}")
        try:
            eleccion = int(input("Ingrese el numero del pedido a cancelar: "))
            pedido_elegido = pedidos[eleccion]
        except (ValueError, IndexError):
            print("Numero Invalido")
            input("ENTER para continuar")
            return
        confirmacion = input("¿seguro que desea cancelar este pedido? (S/N): ").strip().upper()
        if confirmacion != "S":
            print("Operacion cancelada")
            input("ENTER para continuar")
            return
        resultado =mediador.eliminarPedido(str(pedido_elegido["_id"]))
        if resultado =="error":
            self.mensajes("error", "pedido.crear.fallo")
        else:
            self.mensajes("exito", "pedido.cancelar")
            
    def formularioEditarPedido(self):
        os.system('cls')
        print("Editar Pedido")
        pedidos = mediador.obtPedidos(self.email)
        if pedidos is None:
            self.mensajes("error", "no.pedidos")
            return
        for i, pedido in enumerate(pedidos):
            print(f"{i} - Precio total: ${pedido.get('precioTotal')}")
        try:
            eleccion = int(input("ingrese el numero del pedido a editar: "))
            pedido_elegido = pedidos[eleccion]
        except (ValueError, IndexError):
            print("numero invalido.")
            input("ENTER para continuar")
            return
        productos = pedido_elegido.get("productos", [])
        for j, prod in enumerate(productos):
            print(f"{j} - Código: {prod.get('codigoBarra')} | Cantidad: {prod.get('cantidad')}")
        try:
         prod_eleccion = int(input("Ingrese el número del producto a editar: "))
         producto_elegido = productos[prod_eleccion]
        except (ValueError, IndexError):
            print("⁉️ Número inválido.")
            input("ENTER para continuar...")
            return
        try:
            nueva_cantidad = int(input("nueva cantidad: "))
        except:
            print("⁉️ Ingrese un numero entero")
            input("ENTER para continuar")
            return     
        producto_elegido["cantidad"] = nueva_cantidad                
        resultado  = mediador.editarPedido(str(pedido_elegido["_id"]), productos)
        if resultado == "error":
            self.mensajes("error", "pedido.crear.fallo")
        else:
            self.mensajes("exito", "pedido.editar")    
















#################################################
################## LISTADO ######################
#################################################

## Estas funciones no están mal, son así de cortas xq nomas llaman otras
    def listarProductos(self): 
        mediador.listarProductos()

    def listarPedidos(self, nombre, email):
        mediador.listarPedidos(nombre, email)











#ESTA PARTE MOVER SIEMPRE AL FINAL.
######################################################
################## MENSAJES ##########################
######################################################

    def mensajes(self, tipo, codigo):
        if tipo == "error":
            if codigo == "codigo.erroneo.barras":
                print("⁉️ El código de barras ingresado no existe o se ingresó mal.")
                input("ENTER para volver a listar productos y reintentar.")
            elif codigo == "cantidad.erronea":
                print("⁉️ Ingrese solamente números enteros.")
                input("ENTER para volver a ingresar una cantidad.") 
            elif codigo == "calculo.fallo":
                print("⁉️ No se pudo calcular el precio de este producto en su pedido.")
                input("ENTER para volver a intentar\nLos productos agregados con anterioridad se conservan aún en el pedido.") 
            elif codigo == "pedido.crear.fallo":
                input("⁉️ Ocurrió un error durante la creación de su pedido.\nENTER para volver al menú...")
            elif codigo == "no.pedidos":
                input("⁉️ No hay pedidos realizados desde tu cuenta.\nENTER para volver al menú...")

        elif tipo == "exito":
            if codigo == "pedido.crear":
                input("ℹ️ El pedido fue creado con éxito!.\nENTER para volver al menú...")    
            elif codigo == "pedido.cancelar": 
                input("Pedido cancelado con éxito! \nENTER para volver al menú...")
            elif codigo == "pedido.editar":
                input("Pedido editado con éxito!. \nENTER para volver al menú...")
