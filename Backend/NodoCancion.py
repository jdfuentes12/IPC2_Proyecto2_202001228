from Canciones import Canciones

class ListaCanciones:
    def __init__(self):
        self.heard = None
        self.size = 0
        
    def insetarCancion(self,nombre,anio,artista,genero):
        nuevo = Canciones(nombre,anio,artista,genero)
        if self.heard == None:
            self.heard = nuevo
        else:
            nuevo.siguien = self.heard
            self.heard = nuevo
        self.size += 1
        return True