## Sistema básico de consultas a BDD MongoDB en consola Python usando pymongo

Se reutilizó código programado el año pasado (pensado para una BDD SQL, readaptado a Mongo) para el inicio de sesión, creación de cuentas e interfaces de este programa.

## Cuentas por defecto dentro de la base de datos (Incluída en entrega al profesor).

- **Cuenta de usuario:** user@test.com / Us3r_Test!! 

- **Cuenta de administrador:**  admin@test.com / Adm1n_Test!!

Se especifican los usuarios por como funcionan los roles y la creación de usuarios dentro del programa.
Rol de administrador solo puede ser otorgado desde la Base de Datos.
- **EL MENÚ PRINCIPAL SOLO PUEDE CREAR USUARIOS DE ROL 2 (USUARIOS COMUNES)**


## Distribución de funciones (Código)
 **Funciones de Crear y Listar productos: Ismael Figueroa** <br> 
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


**Funciones de Inicio de sesión, creación de usuarios: Ismael Figueroa** <br>
    <br>
    Base-de-datos-MAURI-e-ISMAEL\vista\menu_GENERAL.py (Reutilizado)
    <br>
    Base-de-datos-MAURI-e-ISMAEL\modelo\base_datos.py Líneas 31 a 99 
    <br>
    Base-de-datos-MAURI-e-ISMAEL\controlador\mediador.py Líneas 20 a 76
    
    
**Funciones de Crear y listar pedidos: Ismael Figueroa** <br>
  <br>
  Base-de-datos-MAURI-e-ISMAEL\vista\LISTADO_GENERAL.py (LISTADO EN GENERAL)