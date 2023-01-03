import xml.etree.ElementTree as ET

class lectura:
    def __init__(self):
        ruta = 'C:\Users\jose2\Downloads\ArchivoPruebaEjemplo.xml'
        tree = ET.parse(ruta)
        raiz = tree.getroot()
        
        for dato in raiz:
            for dato1 in dato:
                print(dato1)
        
    
lectura()