class Maravilla:
    def __init__(self, nombre, lugar, tipo):
        self.nombre = nombre
        self.lugar = lugar
        self.tipo = tipo
    
class Grafo:
    def __init__(self):
        self.vertices = []
        self.tamanio = len(self.vertices)

class NodoArista:
    def __init__(self, distancia, destino):
        self.distancia = distancia
        self.destino = destino
    
class NodoVertice:
    def __init__(self, info):
        self.info = info
        self.aristas = []

# se llaman origen y destino pero al no ser dirigido da igual cual sea cada uno.
def insertar_arista(distancia, origen, destino):
    arista = NodoArista(distancia, destino)
    origen.adyacentes.append(arista)
    arista = NodoArista(distancia, origen)
    destino.adyacentes.append(arista)


#creamos las maravillas como objetos
chichen_itza = Maravilla("Chichen Itza", "Mexico", "Arquitectonica")
muralla_china = Maravilla("Gran Muralla China", "China", "Arquitectonica")
ciudad_petra = Maravilla("Ciudad de Petra", "Jordania", "Arquitectonica")
taj_mahal = Maravilla("Taj Mahal", "India", "Arquitectonica")
machu_picchu = Maravilla("Machu Picchu", "Peru", "Arquitectonica")
coliseo = Maravilla("Coliseo de Roma", "Italia", "Arquitectonica")
cristo_redentor = Maravilla("Estatua de Cristo Redentor", "Brasil", "Arquitectonica")

#creamos los vertices del grafo
nodo_chichen_itza = NodoVertice(chichen_itza)
nodo_muralla_china = NodoVertice(muralla_china)
nodo_ciudad_petra = NodoVertice(ciudad_petra)
nodo_taj_mahal = NodoVertice(taj_mahal)
nodo_machu_picchu = NodoVertice(machu_picchu)
nodo_coliseo = NodoVertice(coliseo)
nodo_cristo_redentor = NodoVertice(cristo_redentor)

#añadimos los vertices al grafo
maravillas = Grafo()
maravillas.vertices.append(nodo_chichen_itza)
maravillas.vertices.append(nodo_muralla_china)
maravillas.vertices.append(nodo_ciudad_petra)
maravillas.vertices.append(nodo_taj_mahal)
maravillas.vertices.append(nodo_machu_picchu)
maravillas.vertices.append(nodo_coliseo)
maravillas.vertices.append(nodo_cristo_redentor)

#creamos las aristas
insertar_arista(12800, nodo_chichen_itza, nodo_muralla_china)
insertar_arista(11800, nodo_chichen_itza, nodo_ciudad_petra)
insertar_arista(14500, nodo_chichen_itza, nodo_taj_mahal)
insertar_arista(3800, nodo_chichen_itza, nodo_machu_picchu)
insertar_arista(9400, nodo_chichen_itza, nodo_coliseo)
insertar_arista(6600, nodo_chichen_itza, nodo_cristo_redentor)
insertar_arista(7200, nodo_muralla_china, nodo_ciudad_petra)
insertar_arista(3900, nodo_muralla_china, nodo_taj_mahal)
insertar_arista(16600, nodo_muralla_china, nodo_machu_picchu)
insertar_arista(8100, nodo_muralla_china, nodo_coliseo)
insertar_arista(15400, nodo_muralla_china, nodo_cristo_redentor)
insertar_arista(4000, nodo_ciudad_petra, nodo_taj_mahal)
insertar_arista(12800, nodo_ciudad_petra, nodo_machu_picchu)
insertar_arista(2500, nodo_ciudad_petra, nodo_coliseo)
insertar_arista(8600, nodo_ciudad_petra, nodo_cristo_redentor)
insertar_arista(17000, nodo_taj_mahal, nodo_machu_picchu)
insertar_arista(6000, nodo_taj_mahal, nodo_coliseo)
insertar_arista(12600, nodo_taj_mahal, nodo_cristo_redentor)
insertar_arista(10800, nodo_machu_picchu, nodo_coliseo)
insertar_arista(4700, nodo_machu_picchu, nodo_cristo_redentor)
insertar_arista(7300, nodo_coliseo, nodo_cristo_redentor)
1