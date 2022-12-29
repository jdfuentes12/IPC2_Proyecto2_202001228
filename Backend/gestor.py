from Usuario import Usuario
import json

class Gestor:
    def __init__(self,):
        self.heard = None
        self.size = 0
        
    def ingresarUsuario(self,nombre,nit,direccion, email,empresa):
        nuevo = Usuario(nombre,nit,direccion, email,empresa)
        if self.heard == None:
            self.heard = nuevo
        else:
            nuevo.siguien = self.heard
            self.heard = nuevo
        self.size += 1
        return True
    
