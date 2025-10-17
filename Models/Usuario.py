import uuid
class Usuario:
    def __init__(self, nombre, email)-> None:
        self.id:str = uuid.uuid4().hex
        self.nombre:str = nombre
        self.email:str = email
    
    def __str__(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"
    
    def is_admin(self):
        return False

    
class Cliente(Usuario):
    def __init__(self, nombre, email, direccion_postal)-> None:
        super().__init__(nombre, email) # Atributos cohyhhhhjmunes con la clase Usuario
        self.direccion_postal = direccion_postal # Direccion postal del cliente
    
class Administrador(Usuario):
    def __init__(self, nombre, email, nivel_acceso) -> None:
        super().__init__(nombre, email) # Atributos comunes con la clase Usuario
        self.nivel_acceso = nivel_acceso # Nivel de acceso del administrador
    
    def is_admin(self):
        return True