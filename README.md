## Sistema básico de consultas a BDD MongoDB en consola Python usando pymongo

Se reutilizó código programado el año pasado (pensado para una BDD SQL, readaptado a Mongo) para el inicio de sesión, creación de cuentas e interfaces de este programa.

## Cuentas por defecto dentro de la base de datos (Incluída en entrega al profesor).

--***ℹ️ Al ejecutar desde app.py***

- **👤Cuenta de usuario:** user@test.com / Us3r_Test!! 

- **👤Cuenta de administrador:**  admin@test.com / Adm1n_Test!!

--***ℹ️ Es importante usar la cuenta de administrador al autenticar para probar las funciones de admin. El programa no crea cuentas de administrador. El rol de administrador solo puede ser otorgado a un usuario con un cambio hecho desde la BDD***

--- **⚠️ Si existen problemas para iniciar sesión con usuarios especificados, ejecutar desde archivos "menu_admin_test_directo.py" o "menu_user_test.py"**
<br>
## FUNCIONES DENTRO DEL CÓDIGO
<br>
- Autenticación y creación de cuentas de usuario y perfiles de cliente
<br>
- CRUD Productos (Admin)
<br>
- CRUD Pedidos (Cliente)
<br>
- R Productos (Admin y Cliente)
<br>


## Distribución del desarrollo de las funciones (Código)
 **🟩Funciones de Crear y Listar productos: Ismael Figueroa** <br> 
    <br>
    Base-de-datos-MAURI-e-ISMAEL\vista\menu_ADMINS.py líneas 69 a 91 (Menús y formularios)
    <br>
    Base-de-datos-MAURI-e-ISMAEL\controlador\mediador.py líneas 82 a 94 (Controlador)
    <br>
    Base-de-datos-MAURI-e-ISMAEL\modelo\base_datos.py Líneas 108 a 121 (Consulta para listar)
    <br>
    Base-de-datos-MAURI-e-ISMAEL\modelo\base_datos.py Líneas 130 a 142 (Crear Productos)
    <br>
    Base-de-datos-MAURI-e-ISMAEL\vista\LISTADO_GENERAL.py (LISTADO EN GENERAL)


**🟩Funciones de Inicio de sesión, creación de usuarios: Ismael Figueroa** <br>
    <br>
    Base-de-datos-MAURI-e-ISMAEL\vista\menu_GENERAL.py (Reutilizado)
    <br>
    Base-de-datos-MAURI-e-ISMAEL\modelo\base_datos.py Líneas 31 a 99 
    <br>
    Base-de-datos-MAURI-e-ISMAEL\controlador\mediador.py Líneas 20 a 76
    
    
**🟩Funciones de Crear y listar pedidos: Ismael Figueroa** <br>
  <br>
  Base-de-datos-MAURI-e-ISMAEL\vista\LISTADO_GENERAL.py (LISTADO EN GENERAL)