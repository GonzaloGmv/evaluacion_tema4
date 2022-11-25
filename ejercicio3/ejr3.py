class Maravilla:
    def __init__(self, nombre, lugar, tipo):
        self.nombre = nombre
        self.lugar = lugar
        self.tipo = tipo
    
class Grafo:
    def __init__(self):
        self.vertices = []
        self.tamanio = 0

class NodoArista:
    def __init__(self, distancia, destino):
        self.distancia = distancia
        self.destino = destino
    
class NodoVertice:
    def __init__(self, info):
        self.info = info
        self.aristas = []
        self.tamanio = 0

# se llaman origen y destino pero al no ser dirigido da igual cual sea cada uno.
def insertar_arista(distancia, origen, destino):
    arista = NodoArista(distancia, destino)
    origen.aristas.append(arista)
    arista = NodoArista(distancia, origen)
    destino.aristas.append(arista)