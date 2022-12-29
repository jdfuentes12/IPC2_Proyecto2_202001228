from Usuario import Usuario

class ListaUsuario:
    def __init__(self):
        self.heard = None
        self.size = 0
        
    def agregarUsuario(self,nombre,nit,direccion, email,empresa):
        nuevo = Usuario(nombre,nit,direccion, email,empresa)
        if self.heard == None:
            self.heard = nuevo
        else:
            nuevo.siguien = self.heard
            self.heard = nuevo
        self.size += 1
        return nuevo
    
    def buscarUsuario(self, nit, email):
        tmp = self.heard
        
        while tmp != None:
            if tmp.nit == nit and tmp.email == email:
                return tmp
            tmp = tmp.siguien
        return None
        