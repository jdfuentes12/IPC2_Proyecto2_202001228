class Usuario:
    def __init__(self,nombre,nit,direccion, email,empresa):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.email = email
        self.empresas = empresa
        self.usuario = self.nit
        self.password = self.email
        self.siguien = None