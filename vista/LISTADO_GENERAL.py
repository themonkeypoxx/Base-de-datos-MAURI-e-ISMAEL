import os
from prettytable import PrettyTable 

class General:
      def __init__(self):
            pass
      def ListarProd_General(self, tipo):
        if tipo == "error":
                self.mensajeError("productos.nada")
        else: 
                os.system('cls')
                print("-"*75)
                print("-📖 Resultados de la consulta-")
                print("-🔎 Todos los productos-")
                tabla = PrettyTable()
                tabla.field_names = ["Codigo de Barras", "Producto","Descripción","Precio"]
                for productos in tipo:
                    codigo = productos.get("codigoBarra", "N/A")
                    nombre = productos.get("nombreProd", "N/A")
                    desc = productos.get("descripcion", "N/A")
                    precio = productos.get("precio", 0)
                    precio_mostrar = f"${precio}"
                    tabla.add_row([codigo, nombre, desc, precio_mostrar])
                print(tabla)

      def mensajeError(self, error):
            if error == "productos.nada":
                print("⁉️ No hay productos en la tienda o algo salió mal durante la consulta.\n💡 Vuelva a intentar más tarde.")
                input("ENTER para continuar...")