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
                print(" 1.- Crear nuevo destino\n 2.- Crear nuevo Paquete \n 3.- Listar destinos \n 4.- Listar paquetes \n 5.- Editar destino\n 6.- Editar Paquetes\n 7.- Eliminar destino\n 8.- Salir")
                print("############################################")

                eleccion = input("Seleccione lo que quiere hacer: ")
                try:
                    eleccion = int(eleccion)
                    if eleccion < 1 or eleccion > 8: 
                        print("⁉️ Ingrese un número válido.")
                        input("ENTER para continuar")
                        continue
                except ValueError:
                    print("⁉️ Ingrese números enteros solamente.")
                    input("ENTER para continuar")
                    continue
                
                break 

            if eleccion == 1:
                self.formulario_destinos()
            elif eleccion == 2:
                self.formulario_paquetes()
            elif eleccion == 3:
                self.listarDestinos()
                input("ENTER para volver...")
                self.mostrarMenu()
            elif eleccion == 4:
                self.listarPaquetes()
                input("ENTER para volver...")
                self.mostrarMenu()
            elif eleccion == 5:
                self.formulario_editarDestino()
            elif eleccion == 6:
                self.formulario_editarPaquete()
            elif eleccion == 7:
                self.eliminarDestino()
            elif eleccion == 8:
                print("Cerrando sesión...")
                input("ENTER para continuar")
                return


#######################################################
###########           MENSAJES          ###############
#######################################################
    def mensajeError(self, error):
        if error == "paquete.destinos.cero":
            print("⁉️ No existen destinos!")
            input("ENTER para volver al menú...")
        elif error == "paquete.costo":
            print("⁉️ El costo ingresado no es válido (use punto para decimales).")
            input("ENTER para volver...")
        elif error == "destino.guardar_fallido":
            print("⁉️ Un error ocurrió añadiendo el destino.")
            input("ENTER para volver...")
        elif error == "id.inexistente":
            print("⁉️ No existen registros asociados a la ID especificada.")
            input("ENTER para volver...")
        elif error == "fecha.invalida":
            print("⁉️ La fecha que ingresó es invalida.")
            input("ENTER para volver...")
        elif error == "paquete.error.crear":
            print("⁉️ Un error ocurrió y no se pudo seguir con el proceso")
            input("ENTER para volver...")
    
    def mensajeExito(self, exito):
        if exito == "destino.guardar":
            print("✅ Destino registrado con éxito!")
            input("ENTER para volver...")



#######################################################
###########           CREACION          ###############
#######################################################

    def formulario_paquetes(self):
        hay_destinos = self.mediador.validarCreacionPaquetes()
        if not hay_destinos:
            self.mensajeError("paquete.destinos.cero")
            self.mostrarMenu()
            return
        os.system("cls")
        print("### REGISTRO DE PAQUETES ###")
        nombre = input("Nombre del paquete: ")
        descripcion = input("Descripción: ")
        #HOLA, aca el paquete pasa a base de datos pero como "vacio" por asi decirlo
        #luego se editan las fechas de inicio y de fin segun los destinos que se le asocien
        tipo, codigo = self.mediador.paquetePre_creacion(nombre, descripcion)
        if tipo == "error":
            self.mensajeError(codigo)
            self.mostrarMenu()
        id_ultimo = self.mediador.obtenerUltimo_paq()
        d = 1
        self.formulario_relacion(id_ultimo, d)


    def formulario_relacion(self, id_ultimo, d):
        while True:
            self.listarDestinos()
            print("Seleccione un destino para el paquete")
            id_destino = input("ID del destino: ")
            if not id_destino.isdigit():
                self.mensajeError("id.inexistente")
                continue   
            else:
                id_valida = self.mediador.validarID(id_destino)

                if not id_valida:
                    self.mensajeError("id.inexistente")
                    continue
                else:
                    break
        while True:
            fecha = input("Ingrese la fecha de ida al destino (AAAA-MM-DD): ")
            tipo, fecha = self.mediador.normalizar_fecha(fecha)
            if tipo == "error":
                codigo = fecha
                self.mensajeError(codigo)
                continue 
            self.mediador.relacionarPaquete(id_ultimo, id_destino, fecha)
            respuesta = input("¿Desea seguir agregando destinos? (s/n) : ")
            respuesta = respuesta.lower()
            if respuesta == "s":
                d += 1
                self.formulario_relacion(id_ultimo, d)
            elif respuesta == "n":
                self.mediador.paquete_consumado(id_ultimo, d)
                break
        self.mostrarMenu()

    def formulario_destinos(self):
        os.system("cls")
        print("### REGISTRO DE DESTINO ###")

        nombre = input("Nombre del destino: ")
        descripcion = input("Descripción: ")
        actividades = input("Actividades: ")
        costo = input("Costo: ")
        #ESTO ES EL MEDIADOR VERIFICANDO QUE ESTÉN BIEN PUESTOS LOS DATOS, CREANDO EL OBJ Y DEVOLVIENDO RESULTADOS
        tipo, codigo = self.mediador.crearDestinos(nombre, descripcion, actividades, costo)

        if tipo == "error":
            self.mensajeError(codigo)
            self.formulario_destinos()
        else:
            self.mensajeExito(codigo)
            self.mostrarMenu()

    #######################################################
###########     LISTAR DESTINOS Y PAQUETES     ########
#######################################################

    def listarDestinos(self):
        os.system("cls")
        hay_destinos = self.mediador.validarCreacionPaquetes()
        if not hay_destinos:
            self.mensajeError("paquete.destinos.cero")
            self.mostrarMenu()
        
        columnas, filas = self.mediador.obtenerDestinos()

        print("======= DESTINOS DISPONIBLES =======")
        tabla = PrettyTable()
        tabla.field_names = columnas 

        for fila in filas:
            tabla.add_row(fila)
        print(tabla)


    def listarPaquetes(self):
        os.system("cls")
        columnas, filas = self.mediador.obtenerPaquetes()
        if len(filas) == 0:
            print("⚠️ Actualmente no existen paquetes turísticos registrados.")
            input("ENTER para continuar")
            return

        print("========== PAQUETES TURÍSTICOS DISPONIBLES ==========")
        tabla = PrettyTable()
        tabla.field_names = columnas 

        for fila in filas:
            tabla.add_row(fila)
        print(tabla)

       

    def formulario_editarDestino(self):
        print("### EDICIÓN DE DESTINO ###")
        self.listarDestinos()
        id_destino = input("Ingrese el ID del destino que desea editar: ")
        if not id_destino.isdigit():
            print("⁉️ ID inválido.")
            input("ENTER para volver...")
            self.formulario_editarDestino()
            return   
        else:
            id_valida = self.mediador.validarID(id_destino)

            if not id_valida:
                self.mensajeError("id.inexistente")
                self.formulario_editarDestino()
                return

        columna = input("Qué desea editar? (nombre / descripcion / actividades / costo) ('s') Si desea salir: ").lower()
        if columna not in ["nombre", "descripcion", "actividades", "costo", "s"]:
            print("⁉️ Columna inválida.")
            input("ENTER para volver...")
            self.formulario_editarDestino()
            return
        elif columna == "s":
            self.mostrarMenu()
            return
        nuevo_valor = input(f"Ingrese el nuevo valor para {columna}: ")
        tipo, codigo = self.mediador.editarDestino(id_destino, columna, nuevo_valor)

        if tipo == "error":
            self.mensajeError(codigo)
            self.formulario_editarDestino()
        else:
            print("✅ Destino editado con éxito!")
            input("ENTER para volver...")
            self.mostrarMenu()



    def formulario_editarPaquete(self, id_paquete=None, id_relacion=None):
        print("### EDICIÓN DE PAQUETE ###")
        self.listarPaquetes()
        id_paquete = input("Ingrese el ID del paquete que desea editar: ")
        Eleccion = input("¿Desea editar destinos asociados? (s/n): ").lower()
        if Eleccion == 's':
            
            Destinos_asociados = self.mediador.obtenerDestinos_asociados(id_paquete)
            print("Destinos asociados al paquete:")
            for destino in Destinos_asociados:
                print(destino)
            EleccionEdicion = input("¿Desea agregar un nuevo destino asociado? (s/n): ").lower()
            if EleccionEdicion == 's':
                self.formulario_relacion(id_paquete, len(Destinos_asociados) + 1)
                

            EleccionEdicion = input("¿Desea eliminar algún destino asociado? (s/n): ").lower()
            if EleccionEdicion == 's':
                print("\nIngrese el ID del destino que desea eliminar:")

                for d in Destinos_asociados:
                    print(f"{d[0]} - {d[1]} (Fecha: {d[2]})")

                id_destino = input("ID del destino a eliminar: ")

                tipo, codigo = self.mediador.eliminarDestino_asociado(id_paquete, id_destino)

                if tipo == "error":
                    self.mensajeError(codigo)
                else:
                    print("✅ Destino asociado eliminado correctamente.")
        if not id_paquete.isdigit():
            print("⁉️ ID inválido.")
            input("ENTER para volver...")
            self.formulario_editarPaquete()
            return
        columna = input("Qué desea editar? (nombre / descripcion / fecha inicio / fecha fin / costo) ('s') Si desea salir: ").lower()
        if columna not in ["nombre", "descripcion", "fecha inicio", "fecha fin", "costo", "s"]:
            print("⁉️ Columna inválida.")
            input("ENTER para volver...")
            self.formulario_editarPaquete()
            return
        elif columna == "s":
            self.mostrarMenu()
            return
        if columna == "costo":
            columna = "precio_total"
        elif columna == "fecha inicio":
            columna = "fecha_inicio"
        elif columna == "fecha fin":
            columna = "fecha_fin" 
        nuevo_valor = input(f"Ingrese el nuevo valor para {columna}: ")
        tipo, codigo = self.mediador.editarPaquete(id_paquete, columna, nuevo_valor)

        ### NO SE ESTÁ CONSUMANDO EL PAQUETE DESPUÉS DE EDITARLO, POR LO TANTO NO SE ACTUALIZAN LAS FECHAS AUTOMÁTICAMENTE
        self.consumarpaquete(id_paquete)
        if tipo == "error":
            self.mensajeError(codigo)
            self.formulario_editarPaquete()
        else:
            print("✅ Paquete editado con éxito!")
            input("ENTER para volver...")
            self.mostrarMenu()





    def eliminarDestino(self):
        os.system("cls")
        print("### ELIMINACIÓN DE DESTINO ###")
        self.listarDestinos()
        id_destino = input("Ingrese el ID del destino que desea eliminar: ")
        input("Verificando relaciones con paquetes...")
        resultado = self.mediador.existe_relacion_destino(id_destino)
        if resultado > 0:
            print("⁉️ No se puede eliminar el destino porque está asociado a un paquete.")
            eleccion = input("¿Desea eliminar el destino asociado en cada paquete? (s/n): ").lower()
            if eleccion == 's':
                self.mediador.eliminar_conjunto_relaciones(id_destino)
                print("Eliminando destino asociado en paquetes...")

                ### 
            else:
                self.mostrarMenu()
                return

        if not id_destino.isdigit():
            print("⁉️ ID inválido.")
            input("ENTER para volver...")
            self.eliminarDestino()
            return 
        else:
            id_valida = self.mediador.validarID(id_destino)

            if not id_valida:
                self.mensajeError("id.inexistente")
                self.eliminarDestino()
                return            

        tipo, codigo = self.mediador.eliminarDestino(id_destino)

        if tipo == "error":
            self.mensajeError(codigo)
            self.eliminarDestino()
        else:
            print("✅ Destino eliminado con éxito!")
            input("ENTER para volver...")
            self.mostrarMenu()



    def eliminar_paquete(self):
        os.system("cls")
        self.listarPaquetes
        id_paquete =input("ingrese el id de el Paquete a eliminar")

        if not id_paquete.isdigit():
            print("id invalida")
            self.eliminar_paquete
        else:
            id_valida  = self.mediador.validar_ID(id_paquete)
            if not id_valida:
                self.mensajeError("id.inexistente")
                self.eliminar_paquete()
                return
            
        self.mediador.eliminar_paquete(id_paquete)
        print("✅ Paquete eliminado correctamente.")
        input("ENTER para volver...")
        self.mostrarMenu
        
    

    

        