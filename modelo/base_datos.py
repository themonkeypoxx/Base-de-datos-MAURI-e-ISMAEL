import pymongo
import bcrypt
import os

class Conexion:
    def __init__(self, mongosito, nombreDB, col1, col2, col3, col4, col5):
        try:
            self.client = pymongo.MongoClient(mongosito)
            self.db = self.client[nombreDB]
            self.col1 = self.db[col1]
            self.col2 = self.db[col2]
            self.col3 = self.db[col3]
            self.col4 = self.db[col4]
            self.col5 = self.db[col5]
        except Exception as e:
            print(f"❌ Error conectando a MongoDB: {e}")
    def cerrar(self):
        try:
            self.client.close()
        except Exception as e:
            print(f"❌ Error cerrando la conexión a MongoDB: {e}")
        else:
            print("✅ Conexión a MongoDB cerrada correctamente.")



 #####################################################################
 ############              LOGIN Y SIGN IN             ############### (BASE DE DATOS) 
 #####################################################################


    def correoExiste(self, email):
        try:
            usuario = self.col1.find_one({"email": email})
        except Exception as e:
            print(f"❌ Error buscando/validando usuario: {e}")
            return True  #No se crea usuario en caso de no poder determinar si existe
        return usuario is not None
        
    def crearUsuario(self, email, password, id_rol):
        try:
            nuevo_usuario = {
                "email": email,
                "password": password,
                "id_rol": id_rol
            }
            self.col1.insert_one(nuevo_usuario)
            return True
        except Exception as e:
            print(f"❌ Error creando usuario: {e}")
            return False
 

    def validarLogin(self, email, password):
        try:
            usuario = self.col1.find_one({"email": email})
            if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
                return True
            else:
                return False
        except Exception as e:
            print(f"❌ Error validando login: {e}")
            return False
        

    def validarRoles(self, email):
        try:
            usuario = self.col1.find_one({"email": email})
            if usuario:
                return usuario.get("id_rol", None)
            else:
                return None
        except Exception as e:
            print(f"❌ Error validando roles: {e}")
            return None


#########################################################################
##########               LISTADO ESTÁNDAR                ################
#########################################################################

    def estandar(self, filtro_ctdo, proyeccion_ctdo):
        try:
            filtro = filtro_ctdo
            proyeccion = proyeccion_ctdo
            resultados = list(self.col3.find(filtro, proyeccion))
            encontrados = list(resultados)
            # CONSULTA DENTRO DE MONGODB !!!! db.eventos.find({},{"_id": 0, "invitados": 0})
            #                                                 (FILTRO CTDO)         (PROYECCION_CTDO)
            if not encontrados:
                return None
            else:
                return encontrados
        except Exception as e:
            print(f"⚠️ Error al realizar la consulta: {e}")


##########################################################################
##########            PRODUCTOS C.R.U.D                     ##############
##########################################################################

    #Crear

    def crearProductos(self, nombre, precio, descripcion):
        try:
            nuevo_producto = {
                "nombreProd": nombre,
                "precio": precio,
                "descripcion": descripcion
            }
            self.col3.insert_one(nuevo_producto)
            return True
        except Exception as e:
            print(f"❌ Error creando producto: {e}")
            return None
        
    #Editar (MAURI)
