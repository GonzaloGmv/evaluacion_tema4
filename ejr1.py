tabla = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}

class Nodo:
    def __init__(self, freq, der, izq):
        self.freq = freq
        self.der = der
        self.izq = izq

class Letra:
    def __init__(self, letra, freq):
        self.letra = letra
        self.freq = freq

def coctel(lista):
    for i in range(len(lista) - 1, 0, -1):
        control = False
        for j in range(i, 0, -1):
            if lista[j].freq < lista[j - 1].freq:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
                control = True
        for j in range(i):
            if lista[j].freq > lista[j + 1].freq:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                control = True
        if control == False:
            break
    return lista

def datos(tabla):
    letras = []
    for i in tabla.keys():
        letras.append(Letra(i, tabla[i]))
    coctel(letras)
    return letras

def huffman(lista):
    lista = datos(lista)
    arbol = lista
    while len(arbol) > 1:
        izq = lista.pop(0)
        der = lista.pop(0)
        freq = der.freq + izq.freq
        nodo = Nodo(freq, der, izq)
        arbol.append(nodo)
        coctel(arbol)
    return arbol

arbol = huffman(tabla)