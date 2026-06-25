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
        else:
            print("✅ Conexión a MongoDB exitosa.")
            input("Presione ENTER para continuar...")
    def cerrar(self):
        try:
            self.client.close()
        except Exception as e:
            print(f"❌ Error cerrando la conexión a MongoDB: {e}")
        else:
            print("✅ Conexión a MongoDB cerrada correctamente.")


    def correoExiste(self, email):
        try:
            usuario = self.col1.find_one({"email": email})
        except Exception as e:
            print(f"❌ Error buscando/validando usuario: {e}")
            return True  #No se crea usuario en caso de no poder determinar si existe
        return usuario is not None
        
    def crearUsuario(self, email, password, id_rol):
        try:
            #esto es x el error que se tuvo antes. Verifica que se esté pasando en bytes
            password_bytes = password.encode('utf-8') if isinstance(password, str) else password
            hashed_password_str = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
            nuevo_usuario = {
                "email": email,
                "password": hashed_password_str,
                "id_rol": id_rol
            }
            self.col1.insert_one(nuevo_usuario)
            return True
        except Exception as e:
            print(f"❌ Error creando usuario: {e}")
            return False

        ##ajuste vista, later
    def estandar(coleccion, filtro_ctdo, proyeccion_ctdo, tipo):
        os.system('cls')
        print("-"*75)
        print("-📖 Resultados de la consulta-")
        print(f"-🔎 Tipo consulta: {tipo}")
        try:
            filtro = filtro_ctdo
            proyeccion = proyeccion_ctdo
            resultados = list(coleccion.find(filtro, proyeccion))
            encontrados = list(resultados)
            if not encontrados:
                print("⚠️No se encontraron registros.")
            else:
                for evento in encontrados:
                    print(evento)     
        except Exception as e:
            print(f"⚠️ Error al realizar la consulta: {e}")
###########################################
##########################################
        

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