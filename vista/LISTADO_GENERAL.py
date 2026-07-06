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
                input("ENTER para continuar...")

      def mensajeError(self, error):
            if error == "productos.nada":
                print("⁉️ No hay productos en la tienda o algo salió mal durante la consulta.\n💡 Vuelva a intentar más tarde.")
                input("ENTER para continuar...")
            elif error == "pedidos.nada":
                print("⁉️ No hay pedidos creados en tu cuenta o algo salió mal durante la consulta.\n💡 Vuelva a intentar más tarde.")
                input("ENTER para continuar...")                  

      def ListarPedidos_General(self, nombre, tipo):
        if tipo == "error":
                self.mensajeError("pedidos.nada")
        else: 
                os.system('cls')
                print("-"*75)
                print("-📖 Resultados de la consulta-")
                print(f"-🔎 Pedidos de {nombre}-")
                tabla = PrettyTable()
                tabla.field_names = ["Número del Pedido", "Codigo Barra Producto", "Cantidad del Producto", "Precio (Cantidad)", "Precio Total Pedido"]
                cta = 0
                for pedido in tipo:
                  num_pedido = cta
                  precio_total = pedido.get("precioTotal", 0)
                  productos = pedido.get("productos", [])

                  for producto in productos:
                        codigo = producto.get("codigoBarra", "N/A")
                        cantidad = producto.get("cantidad", "N/A")
                        precio = producto.get("precioCantidad", 0)
                        tabla.add_row([num_pedido, codigo, cantidad, f"${precio}", f"${precio_total}"])
                  cta+=1

                print(tabla)
                input("ENTER para continuar...")