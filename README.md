## Sistema básico de consultas a BDD MongoDB en consola Python usando pymongo

Se reutilizó código programado el año pasado (pensado para una BDD SQL, readaptado a Mongo) para el inicio de sesión, creación de cuentas e interfaces de este programa.

## Cuentas por defecto dentro de la base de datos (Incluída en entrega al profesor).

--***ℹ️ Al ejecutar desde app.py***

- **👤Cuenta de administrador:**  admin@test.com / Adm1n_Test!!
--*En en el caso de cuenta de usuario cliente, no es necesario iniciar con uno precreado*

--***ℹ️ Es importante usar la cuenta de administrador al autenticar para probar las funciones de admin. El programa no crea cuentas de administrador. El rol de administrador solo puede ser otorgado a un usuario con un cambio hecho desde la BDD***

--- **⚠️ Si existen problemas para iniciar sesión con usuarios, ejecutar desde archivos "menu_admin_test_directo.py" o "menu_user_test.py"**
<br>

## FUNCIONES DENTRO DEL CÓDIGO
<br>
- Autenticación y creación de cuentas de usuario y perfiles de cliente
<br>
- CRUD Productos (Admin)
<br>
- CRUD Pedidos (Cliente)
<br>
- Leer Productos (Admin y Cliente)
<br>


## Distribución del desarrollo de las funciones (Código)
**🟩Funciones de Crear y Listar (tanto Productos como Pedidos): Ismael Figueroa** <br> 



**🟩Funciones de Inicio de sesión, creación de usuarios: Ismael Figueroa (únicamente ajustes para mongo)** <br>



**🟩Funciones de editar y borrar (tanto Productos como Pedidos): Mauricio Manterola**