from modelo.base_datos import Conexion
import modelo.clases

class Mediador:
    def __init__(self):
        self.conexion = Conexion(
            mongosito = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.1",
            nombreDB = "Sumativa-4",
            col1 = "usuarios",
            col2 = "clientes",
            col3 = "productos",
            col4 = "pedidos",
            col5 = "administradores"
        )

    def procesar_eleccion_menu(self, eleccion):
        return eleccion 

    def validarCreacionPaquetes(self):
        columnas, filas = self.conexion.obtenerDestinos()
        return filas is not None and len(filas) > 0

    def crearDestinos(self, nombre, descripcion, actividades, costo):
        nombre = nombre.capitalize()
        try:
            costo = float(costo)
        except:
            return ("error", "precio.costo") #ERROR 1 (al insertar datos)
        destinoNuevo = modelo.clases.Destino(nombre, descripcion, actividades, costo)
        guardado = self.conexion.registrarDestinos(destinoNuevo)
        if guardado is True:
            return ("exito", "destino.guardar")
        else:
            return ("error", "destino.guardar_fallido") #ERROR 2 (al mandar a bdd)
        
    def obtenerDestinos(self):
        columnas, filas = self.conexion.obtenerDestinos()
        return columnas, filas
    
    def obtenerPaquetes(self):
        columnas, filas = self.conexion.obtenerPaquetes()
        return  columnas, filas
    
    def editarDestino(self, id_destino, columna, nuevo_valor):
        actualizado = self.conexion.editarDestino(id_destino, columna, nuevo_valor)

        if actualizado:
            return ("exito", "destino.actualizar")
        else:
            return ("error", "destino.actualizar_fallido")
        
    def editarPaquete(self, id_paquete, columna, nuevo_valor):
        actualizado = self.conexion.editarPaquete(id_paquete, columna, nuevo_valor)

        if actualizado:
            return ("exito", "paquete.actualizar")
        else:
            return ("error", "paquete.actualizar_fallido")


    def eliminarDestino(self, id_destino):
        eliminado = self.conexion.eliminarDestino(id_destino)
        if eliminado:
            return ("exito", "destino.eliminar")
        else:
            return ("error", "destino.eliminar_fallido")
        
    def validarID(self, id_destino):
        resultado = self.conexion.buscarID_destino(id_destino)
        return resultado is not None and len(resultado) > 0
    
    def paquetePre_creacion(self, nombre, descripcion):
        #esto enrealidad es la creacion del paquete con datos irrelevantes, para poder relacionarlo
        #con destinos en el menú de creación. Cuando se relacione con destinos, se editarán las fechas y precio
        #correspondientes de forma automática y será visible para todos.

        fecha_inicio = "2000-10-10"
        fecha_fin = "2002-10-10" 
        precio_total = 7357
        paqueteNuevo = modelo.clases.Paquete(nombre, descripcion, fecha_inicio, fecha_fin, precio_total)
        guardado = self.conexion.registrarPaquetes(paqueteNuevo)
        if guardado is True:
            return ("exito", "")
        else:
            return ("error", "paquete.error.crear")
        
    def obtenerUltimo_paq(self):
        id_ultimo = self.conexion.ultimoPaquete()
        return id_ultimo

#####


    def normalizar_fecha(self, fecha):
        calculos = modelo.clases.Calculos()
        fecha_final = calculos.normalizar_fecha(fecha)
        if fecha_final is None:
            return ("error", "fecha.invalida")
        else:
            fecha = fecha_final
            return ("exito", fecha)

    def relacionarPaquete(self, id_ultimo, id_destino, fecha):
        id_paquete = id_ultimo[0]
        relacionNueva = modelo.clases.Relacion_paquete(id_paquete, id_destino, fecha)
        relacionado = self.conexion.relacionPaquete_Destino(relacionNueva)
        if relacionado:
            return ("exito", "")
        else:
            return ("error", "relacion.fallo")
        

    def paquete_consumado(self, id_ultimo, d):
        id_paquete = id_ultimo[0]
        fechas = self.conexion.obtenerExtremosFecha(id_paquete)
        if d > 1:
            fecha_fin = fechas[0][0]
            fecha_inicio = fechas[0][1]
        elif d <= 1:
            fecha_inicio = fechas[0][0]
            fecha_fin =fecha_inicio
        precio_total = self.conexion.obtenerCostos(id_paquete)
        precio_total = precio_total[0][0]
        paqueteConsumado = modelo.clases.Paquete_consumado(fecha_inicio, fecha_fin, precio_total, id_paquete)
        guardado = self.conexion.consumarPaquete(paqueteConsumado)



### NUEVO ###
    def formulario_relacion_paquete(self): 
        destinos = self.conexion.obtenerDestinos()

        return destinos
    def obtenerDestinos_asociados(self, id_paquete):
        destinos_asociados = self.conexion.obtenerDestinos_asociados(id_paquete)
        return destinos_asociados
    
    def obtenerDestinos_asociados(self, id_paquete):
        destinos_asociados = self.conexion.obtenerDestinos_asociados(id_paquete)
        return destinos_asociados
    
    def eliminarDestino_Paquete(self, id_paquete, id_destino):
        eliminado = self.conexion.eliminarDestino_Paquete(id_paquete, id_destino)
        if eliminado:
            return ("exito", "destino_paquete.eliminar")
        else:
            return ("error", "destino_paquete.eliminar_fallido")
        
    def eliminarDestino_asociado(self, id_paquete, id_destino):
        resultado = self.conexion.paqueteExiste(id_paquete)
        if not resultado:
            return ("error", "paquete inexistente")

        destinos = self.obtenerDestinos_asociados(id_paquete)
        if not destinos:
            return ("error", "paquete sin destinos")

        ids_destinos = [str(d[0]) for d in destinos]  

        if str(id_destino) not in ids_destinos:
            return ("error", "destino no encontrado en el paquete")

        try:
            cursor = self.conexion.cursor()
            sql = """
                DELETE FROM paquete_relacion
                WHERE id_paquete = %s AND id_destino = %s
            """
            cursor.execute(sql, (id_paquete, id_destino))
            self.conexion.commit()
            cursor.close()

            return ("exito", "destino eliminado")

        except Exception as e:
            print("❌ Error al eliminar destino:", e)
            return ("error", "fallo en la base de datos")

    def eliminar_conjunto_relaciones(self, id_paquete):
        eliminado = self.conexion.eliminar_conjunto_relaciones(id_paquete)
        if eliminado:
            return ("exito", "relaciones.eliminar")
        else:
            return ("error", "relaciones.eliminar_fallido")
        
    def existe_relacion_destino(self, id_destino):
        resultado = self.conexion.existe_relacion_destino(id_destino)
        return resultado
 


 ###########################
        
    def validarContrasenaCrear(self, password):
        validador = modelo.clases.Calculos()
        validar_contra = validador.validadorContras(password)
        if validar_contra == True:
            password = validador.encriptar_Contrasena(password)
            return ("exito", password)
        else:
            return ("error", "contrasena.insegura")
        
    def validarCorreoCrear(self, email):
        validador = modelo.clases.Calculos()
        validar_correo = validador.validarEmails(email)
        if validar_correo == False:
            return ("error", "correo.erroneo")
        else: 
            correo_existe = self.conexion.correoExiste(email)
            if correo_existe == True:
                return ("error", "usuario.existe.correo")
            else:
                return ("exito", email)

    def crearUsuario(self, email, password):
        id_rol = 2
        guardado = self.conexion.crearUsuario(email, password, id_rol)
        if guardado == True:
            return ("exito", "usuario.creado")
        else:
            return ("error", "usuario.falla.creacion")
        
    def validarLogin(self, emailInicio, contraInicio):
        es_valido = self.conexion.validarLogin(emailInicio, contraInicio)
        if es_valido:
                    empleado = self.conexion.numeroEmpleado(emailInicio)
                    numeroUser = empleado[0]
                    roltest = self.conexion.validarRoles(emailInicio)
                    rolUser = roltest[0]
                    #esta funcion se usará asumiendo que adminRRHH = 1 y usuario = 2. ASEGURARSE de que estén
                    #definidos así en la BDD
                    return numeroUser, rolUser
        else:
            return ("error", "no.autenticar")
    
    def reservarPaquete(self, id_paquete, id_usuario):
        reservaNueva = modelo.clases.Reserva(id_usuario, id_paquete)
        reservado = self.conexion.reservar(reservaNueva)
        if reservado  == True:
            return ("exito", "reserva.crear")
        else:
            return ("error", "reserva.fallida")
        
    def mostrarReservas(self, id_usuario):
        columnas, filas = self.conexion.obtenerReservas(id_usuario)
        return columnas, filas
    
    def verificarSiHay(self, id_usuario):
        resultados = self.conexion.verificarHayReservas(id_usuario)
        return resultados is not None and len(resultados) > 0
    
    def obtenerNombre(self, id_usuario):
        username = self.conexion.obtenerNombre(id_usuario)
        return username

    def obtenerPaquetesDisp(self, id_usuario):
        columnas, filas = self.conexion.obtenerReservasDisponibles(id_usuario)
        return columnas, filas

    def eliminar_paquete(self, id_paquete):
        resultados = self.conexion.eliminar_paquete(id_paquete)
        return resultados