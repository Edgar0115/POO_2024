#codificar la clase usuarios

from conexionBD import *
import hashlib
import datetime

class Usuario:
    def __init__(self,nombre, apellidos, email, password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasena=self.hash_password(password)
    def hash_password(self,password):
    
        def registrar(self):
            return 0
        