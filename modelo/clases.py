import re
import bcrypt


class Calculos:
    def __init__(self):
        pass

    
    def validadorContras(self, password):
        if len(password) < 10:
            return False
        tiene_mayuscula = re.search(r'[A-Z]', password)
        tiene_minuscula = re.search(r'[a-z]', password)
        tiene_numero = re.search(r'[0-9]', password)
        tiene_simbolo = re.search(r'[!@#$%^&*(),.?"{}|<>/\']', password)
        if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
            return True
        else:
            return False
        
    def encriptar_Contrasena(self, password):
        password_bytes = password.encode('utf-8') if isinstance(password, str) else password
        hashed_password_str = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
        return hashed_password_str
     
    def validarEmails(self, email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(patron, email):
         return True
        else:
         return False

    def validarNombre(self, nombre):
        tiene_simbolo = re.search(r'[]!@#$%^&*(),.?"{}|<>/]', nombre)
        if tiene_simbolo:
            return False
        else:
            return True
        
    def calcular_total_precio(self, lista_productos):
    #Suma el valor de "precioCantidad" por cada producto en la listaaaaaaaaaaaaaa
        return sum(producto["precioCantidad"] for producto in lista_productos)
    