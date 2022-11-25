class Maravilla:
    def __init__(self, nombre, lugar, tipo):
        self.nombre = nombre
        self.lugar = lugar
        self.tipo = tipo
    
class Grafo:
    def __init__(self):
        self.vertices = []
        self.tamanio = len(self.vertices)

chichen_itza = Maravilla("Chichen Itza", "Mexico", "Arquitectonica")
muralla_china = Maravilla("Gran Muralla China", "China", "Arquitectonica")
ciudad_petra = Maravilla("Ciudad de Petra", "Jordania", "Arquitectonica")
taj_mahal = Maravilla("Taj Mahal", "India", "Arquitectonica")
machu_picchu = Maravilla("Machu Picchu", "Peru", "Arquitectonica")
coliseo = Maravilla("Coliseo de Roma", "Italia", "Arquitectonica")
cristo_redentor = Maravilla("Estatua de Cristo Redentor", "Brasil", "Arquitectonica")

maravillas = Grafo()
maravillas.vertices.append(chichen_itza)
maravillas.vertices.append(muralla_china)
maravillas.vertices.append(ciudad_petra)
maravillas.vertices.append(taj_mahal)
maravillas.vertices.append(machu_picchu)
maravillas.vertices.append(coliseo)
maravillas.vertices.append(cristo_redentor)

