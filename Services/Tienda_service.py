from Models.Pedido import Pedido
from Models.Producto import Producto
from Models.Usuario import Usuario, Cliente, Administrador
from typing import List, Tuple # Para anotaciones de tipos de listas y tuplas

class Tienda_service:
    def __init__(self) -> None:
        self.usuarios = {}
        self.productos = {}
        self.pedidos = []
    
    def registrar_usuario(self, tipo, nombre, email, direccion_postal = None, nivel_acceso = None): # Registro de un nuevo usuario
        if tipo == "cliente": # Verifico el tipo de usuario a crear
            usuario = Cliente(nombre = nombre, email = email, direccion_postal = direccion_postal)# Atributos específicos del cliente
        elif tipo == "administrador": # Verifico el tipo de usuario a crear
            usuario = Administrador(nombre = nombre, email = email, nivel_acceso = nivel_acceso) # Atributos específicos del administrador
        else:
            raise ValueError("Tipo de usuario no válido") # Si el tipo no es correcto, lanzo un error
        self.usuarios[usuario.id] =  usuario # Guardo el usuario en el diccionario con su id como clave
        return usuario # Devuelvo el usuario creado para que pueda mostrarse su resumen

    
    def agregar_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto # Agrego el producto al diccionario

    def eliminar_producto(self, producto_id: str) -> bool:
        if producto_id in self.productos: # Verifico si el producto existe
            del self.productos[producto_id]  # Elimino el producto del inventario
            return True  # Devuelvo True eliminación se realizó
        return False  # Devuelvo False si no existía 

    def listar_productos(self) -> List[Producto]: # Lista de todos los productos disponibles
        return list(self.productos.values()) # Devuelvo una lista de todos los productos

    def realizar_pedido(self, usuario_id: str, items: List[Tuple[str, int]]) -> Pedido:
        usuario = self.usuarios.get(usuario_id)  # Recupero el usuario a partir de su id
        if not isinstance(usuario, Cliente):  # Verifico que el usuario exista y sea de tipo cliente
            return None  # Devuelvo None si el usuario no existe o no es cliente
        
        lineas: List[Tuple[Producto, int]] = []  # Preparo una lista que almacena las líneas con objetos producto y cantidades
        for producto_id, cantidad in items:  # Recorro identificador de producto y cantidad solicitada
            producto = self.productos.get(producto_id)  # Busco en el inventario por su id
            if producto is None:  # Verifico que exista
                return None  # Devuelvo None si no existe
            if not producto.agregar_stock(cantidad):  # Compruebo que haya stock para la cantidad pedida
                return None  # Devuelvo None si no hay stock suficiente
            lineas.append((producto, cantidad))  # Si está correcto, agrego la línea con el producto encontrado y la cantidad

        for producto, cantidad in lineas:  # Recorro las líneas ya validadas para actualizar los stocks
            producto.actualizar_stock(-cantidad)  # Descuento del inventario las unidades correspondientes de cada producto

        pedido = Pedido(cliente=usuario, items=lineas)  # Creo el objeto Pedido con el cliente y las líneas confirmadas
        self.pedidos.append(pedido)  # Guardo el pedido en el histórico de pedidos del servicio
        return pedido  # Devuelvo el pedido creado para que pueda mostrarse su resumen

    def pedidos_de_usuario(self, usuario_id: str) -> List[Pedido]:
        pedidos_usuario = [p for p in self.pedidos if p.cliente.id == usuario_id]  # Filtro los pedidos que pertenecen al usuario indicado
        pedidos_ordenados = sorted(pedidos_usuario, key=lambda p: p.fecha)  # Ordeno la lista de pedidos filtrados por la fecha del pedido
        return pedidos_ordenados  # Devuelvo la lista ordenada de pedidos del usuario