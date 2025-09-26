import uuid # Para generar IDs únicos
from datetime import datetime # Para manejar fechas
from typing import List, Tuple # Para anotaciones de tipos
from .Usuario import Cliente # Importo Cliente para el tipo de cliente en el pedido
from .Producto import Producto # Importo Producto para manejar los productos en el pedido
class Pedido:
    def __init__(self, cliente: Cliente, items: List[Tuple[str, int]]) -> None:
        self.cliente = cliente # Cliente que realiza el pedido
        self.productos = Producto # Lista de productos en el pedido
        self.id = str(uuid.uuid4().hex) # ID único del pedido
        self.fecha: datetime = datetime.now() # Fecha del pedido
        self.items: List[Tuple[str, int]] = items # Lista de tuplas (ID del producto, cantidad)

    def calcular_total(self):
        total = sum(producto.precio * producto.cantidad for producto in self.productos) # Suma el precio de cada producto por su cantidad
        return total
    
    def __str__(self): # Representación en cadena del pedido
        return (
            f"Pedido ID: {self.id}, Cliente: {self.cliente.nombre}, Productos: [{self.items}], Fecha: {self.fecha}, Numero de productos: {self.numero_productos}"
            ) # Devuelvo una cadena que incluye el id, la fecha, el nombre del cliente y el total del pedido