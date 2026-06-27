from vista.menu_ADMINS import Mediador, Menu_Admin
from vista.menu_USUARIOS import Menu_user
import os
from pwinput import pwinput 
mediador = Mediador() 

class MenuGeneral:

    def _init_(self):
        pass
    def principal(self):
        os.system("cls")
        print("####################### MENÚ PRINCIPAL #######################")
        print("¿Qué desea hacer?")
        print(" 1.- Iniciar sesión \n 2.- Crear Cuenta \n 3.- Cerrar programa") 
        print("##############################################################")
        while True:
            seleccion = input("Ingrese su elección: ")
            try:
                seleccion = int(seleccion)
            except:
                print("Ingrese un número, por favor.")
                continue
            else:
                if seleccion < 1 or seleccion > 3:
                    print("Ingrese una opción válida.")
                    continue
                else:
                    break
        self.procesarEleccion(seleccion)


    def procesarEleccion(self, seleccion):

        if seleccion == 1: 
            self.iniciarSesion()
            self.principal()

        elif seleccion == 2:
            self.crearCuenta()
            self.principal()
            
        elif seleccion == 3:
            print("Hasta pronto!")
            input("ENTER para continuar...")
            os.system("cls")
            mediador.conexion.cerrar()


    def crearCuenta(self):
        while True:
            os.system("cls")
            print("-"*50)
            email = input("Ingrese su correo electrónico: ")
            print("-"*50)
            tipo, codigo = mediador.validarCorreoCrear(email)
            if tipo == "error":
                self.mensajes(tipo, codigo)
                continue
            else:
                email = email.strip().lower()
                break
        while True:
            os.system("cls")
            print("-"*50)
            print("Ingrese una contraseña que pueda recordar\n Debe contener números, símbolos, letras mayúsculas y minúsculas")
            print("-"*50)
            password = pwinput(prompt= "Ingrese su contraseña: ")
            tipo, codigo = mediador.validarContrasenaCrear(password)
            if tipo == "error":
                self.mensajes(tipo, codigo)
                continue
            else:
                password = codigo
                tipo, codigo = mediador.crearUsuario(email, password)
                self.formularioCliente_Crear(email, tipo)
                self.mensajes(tipo, codigo)
                break

    def iniciarSesion(self):
            while True:
                print("Ingrese su correo electrónico")
                emailInicio = input("Correo electrónico: ")
                print("Ingrese su contraseña")
                contraInicio = pwinput(prompt= "Contraseña: ")
                tipo, codigo = mediador.validarLogin(emailInicio, contraInicio)
                if tipo == "error":
                    self.mensajes(tipo, codigo)
                    os.system("cls")
                    continue
                else:
                    emailInicio = tipo
                    rolUser = codigo
                    break
                
            print("Has iniciado sesión correctamente")
            print("Serás redirigido al menú...")
            input("ENTER para continuar...")
            if rolUser == 1:
                MenuAdm = Menu_Admin()
                MenuAdm.mostrarMenu()
                self.principal()
            elif rolUser == 2:
                Menu_usuario = Menu_user(emailInicio)
                Menu_usuario.getNombre()
        
    def formularioCliente_Crear(self, email, tipo):
        if tipo == "error":
            return
        tpN = "error"
        cdN = "valor.erroneo.nombres"
        while True:
            os.system('cls')
            print("-"*50)
            nombre = input("Ingresa tu nombre: ")
            valido = mediador.validarNombre(nombre)
            if valido == True:
                if nombre == "error":
                    print(f"🚫 El nombre '{nombre}' no está permitido en el sistema.\nPruebe con otro.\n💡 Sugerencia: Utilice su nombre real o un apodo.")
                    input("==========================================================\nENTER para continuar...")
                    continue
                break
            self.mensajes(tpN, cdN)
            continue
        while True:
            os.system('cls')
            print("="*50)
            apellido = input("Ingresa tu apellido: ")
            valido_ap = mediador.validarNombre(apellido)
            if valido == True:
                break
            self.mensajes(tpN, cdN)
            continue
        print("="*50)
        print("Ingresa tu dirección: ")
        direccion_casa = input("Dirección (EJ: #450 Calle Brasil): ")
        direccion_ciudad = input("Ciudad: ")
        direccion = {
                "casa": direccion_casa,
                "ciudad": direccion_ciudad
                }
        mediador.crearCliente(nombre, apellido, email, direccion)
        







#########
    def mensajes(self, tipo, codigo):
        if tipo == "error":
            if codigo == "usuario.existente":
                print("⁉️ Este nombre de usuario ya tiene una cuenta registrada.\n 💡 Intente con otro nombre o agregué números al que ya ingresó.")
                input("ENTER para volver a ingresar...")
            elif codigo == "contrasena.insegura":
                print("⁉️ La contraseña no cumple con los estándares solicitados.")
                input("ENTER para volver a ingresar...")
            elif codigo == "usuario.existe.correo":
                print("⁉️ Ya existe un usuario vinculado a este correo.")
                input("ENTER para volver a ingresar...")
            elif codigo == "correo.erroneo":
                print("⁉️ El correo ingresado no es válido\n 💡 Lo más probable es que falte un dominio (EJ: @gmail.com)")
                input("ENTER para volver a ingresar...")    
            elif codigo == "usuario.falla.creacion":
                print("⁉️ El usuario no pudo ser creado")
                input("ENTER para continuar...")
            elif codigo == "no.autenticar":
                print("⁉️ Nombre o contraseña incorrectos.")
                input("ENTER para volver a intentar...")
            elif codigo == "valor.erroneo.nombres":
                print("⁉️ Ingresa un valor válido")
                input("ENTER para continuar...")                
        elif tipo == "exito":
            if codigo == "usuario.creado":
                print("✅ El usuario ha sido creado con éxito!")
                input("ENTER para continuar...")