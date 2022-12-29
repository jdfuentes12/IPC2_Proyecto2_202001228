from NodoCancion import ListaCanciones

class Playlist:
    def __init__(self,nit,vinyl,compacto,categoria):
        self.nit = nit
        self.vinyl = vinyl
        self.compacto = compacto
        self.categoria = categoria
        self.conciones  = ListaCanciones()
        self.siguien = None