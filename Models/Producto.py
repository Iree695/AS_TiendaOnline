import uuid # Para generar IDs únicos
class Producto: # Clase base para productos
    def __init__(self, nombre: str, precio: float, cantidad) -> None:
        self.nombre = nombre # Nombre del producto
        self.id = str(uuid.uuid4().hex) # ID único del producto
        self.precio = precio # Precio del producto
        self.cantidad = cantidad # Cantidad en stock
    
    def agregar_stock(self, cantidad) -> bool:
        self.cantidad += cantidad
    
    def actualizar_stock(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto(id = {self.id}, nombre = {self.nombre}, precio = {self.precio:.2f}, cantidad = {self.cantidad})"  # Devuelvo un resumen textual del producto
    

class Producto_Electronico(Producto): # Subclase para productos electrónicos
    def __init__(self, nombre, precio, cantidad, garantia_meses):
        super().__init__(nombre, precio, cantidad)
        self.garantia_meses = garantia_meses
    
    def __str__(self):
        return f"{super().__str__()}, Garantia: {self.garantia_meses} meses"
    
class Producto_Ropa(Producto): # Subclase para productos de ropa
    def __init__(self, nombre, precio, cantidad, talla, color):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        self.color = color
    
    def __str__(self):
        return f"{super().__str__()}, Talla: {self.talla}, Color: {self.color}"