from Models.Producto import Producto, Producto_Electronico, Producto_Ropa
from Models.Usuario import Usuario, Cliente, Administrador
from Models.Pedido import Pedido
from Services.Tienda_service import Tienda_service

def main() -> None:
    tienda = Tienda_service() # Creo el servicio de tienda

    # Registro usuarios
    cliente1 = tienda.registrar_usuario( tipo = "cliente", 
                                        nombre = "Ana", 
                                        email = "ana@gmail.com", 
                                        direccion_postal = "Calle A 1, Ciudad" )
    cliente2 = tienda.registrar_usuario( tipo = "cliente", 
                                        nombre = "Luis", 
                                        email = "luis@gmail.com",
                                        direccion_postal = "Avenida B 2, Ciudad" )
    cliente3 = tienda.registrar_usuario( tipo = "cliente",
                                        nombre = "Marta",
                                        email = "marta@gmail.com",
                                        direccion_postal = "Calle C 3, Ciudad" )
    admin1 = tienda.registrar_usuario( tipo = "administrador",
                                        nombre = "Carlos", 
                                        email = "carlos@gmail.com",
                                        nivel_acceso = 5 )
    print("Usuarios registrados:")
    for usuario in [cliente1, cliente2, cliente3, admin1]: # Recorro los usuarios registrados
        print(str(usuario)) # Muestro cada usuario

    # Agrego productos
    producto1 = Producto_Electronico( nombre = "Smartphone",
                                        precio = 699.99,
                                        cantidad = 50,
                                        garantia_meses = 24 )
    producto2 = Producto_Electronico( nombre = "Portátil",
                                        precio = 1299.99,
                                        cantidad = 30,
                                        garantia_meses = 12 )
    producto3 = Producto_Electronico( nombre = "Tablet",
                                        precio = 399.99,
                                        cantidad = 80,
                                        garantia_meses = 18 )
    producto4= Producto_Ropa( nombre = "Pantalones",
                                precio = 49.99,
                                cantidad = 100,
                                talla = "L",
                                color = "Negro" )
    producto5 = Producto_Ropa( nombre = "Camiseta",
                                precio = 19.99,
                                cantidad = 200,
                                talla = "M",
                                color = "Azul" )
    
    tienda.agregar_producto(producto1) # Agrego el telefono al inventario
    tienda.agregar_producto(producto2) # Agrego el portatil al inventario
    tienda.agregar_producto(producto3) # Agrego la tablet al inventario
    tienda.agregar_producto(producto4) # Agrego los pantalones al inventario
    tienda.agregar_producto(producto5) # Agrego la camiseta al inventario

    # Lista productos
    print("Productos disponibles en el inventario:")
    for producto in tienda.listar_productos():
        print(producto)

    # Simulo pedidos
    pedido1 = tienda.realizar_pedido( usuario_id = cliente1.id,
                                    items = [(producto1.id, 1), (producto4.id, 2)] ) # Ana pide 1 telefono y 2 pantalones
    if pedido1:
        print("\nResumen del pedido de Ana:")
        print(pedido1)
        print("Productos después del pedido de Ana:")
        print(producto1) # Muestro el producto 1 para ver el stock actualizado
        print(producto4) # Muestro el producto 4 para ver el stock actualizado

    pedido2 = tienda.realizar_pedido( usuario_id = cliente2.id,
                                    items = [(producto2.id, 1), (producto5.id, 3)] ) # Luis pide 1 portatil y 3 camisetas
    if pedido2:
        print("\nResumen del pedido de Luis:")
        print(pedido2)
        print("Productos después del pedido de Luis:")
        print(producto2) # Muestro el producto 2 para ver el stock actualizado
        print(producto5) # Muestro el producto 5 para ver el stock actualizado

    pedido3 = tienda.realizar_pedido( usuario_id = cliente3.id,
                                    items = [(producto3.id, 2)] ) # Ana pide 2 tablets
    if pedido3:
        print("\nResumen del pedido de Marta:")
        print(pedido3)
        print("Productos después del pedido de Marta:")
        print(producto3) # Muestro el producto 3 para ver el stock actualizado
    
    # Historial de los pedidos de los usuarios
    print("\nHistorial de pedidos un usuario:")
    historico_ana = tienda.pedidos_de_usuario(cliente1.id if cliente1 else "")  # Obtengo la lista de pedidos de Ana ordenada por fecha
    for pedido1 in historico_ana:  # Recorro cada pedido del histórico de Ana
        print(producto) # Imprimo el resumen de cada pedido para comprobar el histórico

if __name__ == "__main__": # Compruebo si se ejecuta directamente
    main() # Ejecuto la función principal

    