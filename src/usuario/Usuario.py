

class Usuario:
    def __init__(self, nombre_usuario: str, nombre: str,
                apellido: str, contrasena: str, fecha_de_nacimiento: str,
                edad: int) -> None:
        self.nombre_usuario = nombre_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.edad = edad
