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
        
 #####################################################################
 ############              LOGIN Y SIGN IN             ############### 
 #####################################################################
        
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
                    input("ENTER para continuar...")
                    roltest = self.conexion.validarRoles(emailInicio)
                    #esta funcion se usará asumiendo que adminRRHH = 1 y usuario = 2. ASEGURARSE de que estén
                    #definidos así en la BDD
                    return emailInicio, roltest
        else:
            return ("error", "no.autenticar")
        
    def getNombre(self, email):
        nombre = self.conexion.getNombre(email)
        if nombre is None:
            nombre = "error"
        else:
            return nombre
        
    def validarNombre(self, nombre):
        validador = modelo.clases.Calculos()
        nombre = validador.validarNombre(nombre)
        if nombre == True:
            return True
        else: 
            return False
        
    def crearCliente(self, nombre, apellido, email, direccion):
        guardado = self.conexion.crearCliente(nombre, apellido, email, direccion)
    
####################################################################
############# PRODUCTOS ###########################################
###################################################################

    def listarProductos(self):
        filtro = {}
        proyeccion = {}
        tipo = self.conexion.estandar(filtro, proyeccion)
        if tipo is None:
            tipo = "error"
        return tipo
    
    def crearProducto(self, codigo, nombre, precio, desc):
        tipo = self.conexion.crearProductos(codigo, nombre, precio, desc)
        if tipo is None:
            tipo = "error"
        return tipo