from datetime import datetime
import re
import bcrypt


class Calculos:
    def __init__(self):
        pass

    def normalizar_fecha(self, fecha):
        fecha_str = fecha

        formatos = [
            "%d/%m/%Y", "%d-%m-%Y",
            "%Y/%m/%d", "%Y-%m-%d",
            "%m/%d/%Y", "%m-%d-%Y",
            "%d.%m.%Y", "%Y.%m.%d"
        ]
        
        for fmt in formatos:
            try:
                fecha_normalizada = datetime.strptime(fecha_str, fmt)
                return fecha_normalizada.strftime("%Y-%m-%d")
            except ValueError:
                pass  
        
        return None
    
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
        passHash = bcrypt.hashpw(bytes(password.encode("utf-8")), bcrypt.gensalt(14))
        return passHash
     
    def validarEmails(self, email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(patron, email):
         return True
        else:
         return False
