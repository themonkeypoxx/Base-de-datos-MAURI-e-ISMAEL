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
        
    def getNombre(self, email):
        try:
            resultado = self.col2.find_one({"email": email})
            if resultado:
                return resultado.get("nombre")
            return None
        except Exception as e:
            print(f"❌ Error validando roles: {e}")
            return None

    def crearCliente(self, nombre, apellido, email, direccion):
        try:
            nuevo_cliente = {
                "nombre": nombre,
                "apellido": apellido,
                "email": email,
                "direccion": direccion
                }
            self.col2.insert_one(nuevo_cliente)
            return True
        except Exception as e:
            print(f"❌ Error creando usuario: {e}")
            return False
            



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

    def crearProductos(self, codigo, nombre, precio, descripcion):
        try:
            nuevo_producto = {
                "codigoBarra": codigo,
                "nombreProd": nombre,
                "precio": precio,
                "descripcion": descripcion
            }
            self.col3.insert_one(nuevo_producto)
            return True
        except Exception as e:
            print(f"❌ Error creando producto: {e}")
            return None
        
    #Editar y borrar  (MAURI) ###################
    #####################
    def editarProducto(self, codigo, nombre, precio, descripcion):
        try:
            resultado = self.col3.update_one(
                {"codigoBarra": codigo},
                {"$set": {
                    "nombreProd": nombre,
                    "precio": precio,
                    "descripcion": descripcion
                }}
            )
            if resultado.modified_count > 0:
                return True
            else:
                return None  # No encontró el producto :v
        except Exception as e:
            print(f"❌ Error editando producto: {e}")
            return None

    def eliminarProducto(self, codigo):
        try:
            resultado = self.col3.delete_one({"codigoBarra": codigo})
            if resultado.deleted_count > 0:
                return True
            else:
                return None
        except Exception as e:
            print(f"❌ Error eliminando producto: {e}")
            return None

    def editarPedido(self, id_pedido, fecha_entrega):
        try:
            from bson import ObjectId
            resultado = self.col4.update_one(
                {"_id": ObjectId(id_pedido)},
                {"$set": {"fecha_entrega": fecha_entrega}}
            )
            if resultado.modified_count > 0:
                return True
            else:
                return None
        except Exception as e:
            print(f"❌ Error editando pedido: {e}")
            return None

    def eliminarPedido(self, id_pedido):
        try:
            from bson import ObjectId
            resultado = self.col4.delete_one({"_id": ObjectId(id_pedido)})
            if resultado.deleted_count > 0:
                return True
            else:
                return None
        except Exception as e:
            print(f"❌ Error eliminando pedido: {e}")
            return None

    def listarPedidos(self, email):
        try:
            resultados = list(self.col4.find({"email_cliente": email}))
            if not resultados:
                return None
            return resultados
        except Exception as e:
            print(f"❌ Error listando pedidos: {e}")
            return None



##################### Extra

    def getCodigoBarra(self, codigo):
        try:
            codigoBarra = self.col3.find_one({"codigoBarra": codigo})
            if codigoBarra:
                return codigoBarra.get("codigoBarra", None)
            else:
                return None
        except Exception as e:
            print(f"❌ Error obteniendo código de barras: {e}")
            return None
        
##########################################################################
##########              PEDIDOS C.R.U.D                     ##############
##########################################################################
    def calculoPrecio(self, cantidad, codigo):
        try:
            resultado = self.col3.aggregate([
                {
                    "$match": { "codigoBarra": codigo }
                },
                {
                    "$project": {
                        "codigoBarra": 1,
                        "nombreProd": 1,
                        "precio": 1,
                        "cantidad": { "$literal": cantidad },
                        "total": {
                            "$multiply": [
                                { "$toDouble": "$precio" }, cantidad  #convierte el string a número ay mamá te extraño tanto sql
                            ]
                        }
                    }
                }
            ])
            doc = next(resultado, None)
            if doc:
                print(doc["total"]) #test
                return doc
        except Exception as e:
            print(f"❌ Error calculando el precio: {e}")
            return None
