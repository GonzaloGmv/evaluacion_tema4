tabla = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}

class Nodo:
    def __init__(self, letra, freq, der, izq, valor):
        self.freq = freq
        self.der = der
        self.izq = izq
        self.letra = letra
        self.valor = valor

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
        letras.append(Nodo(i, tabla[i], None, None, None))
    coctel(letras)
    return letras

def huffman(lista):
    lista = datos(lista)
    arbol = lista
    while len(arbol) > 1:
        izq = lista.pop(0)
        izq.valor = '0'
        der = lista.pop(0)
        der.valor = '1'
        freq = der.freq + izq.freq
        nodo = Nodo(None, freq, der, izq, None)
        arbol.append(nodo)
        coctel(arbol)
    return arbol

def comprimir(mensaje, raiz):
    for i in mensaje:
        if i in tabla:
            buscar_letra(i, raiz[0], str())
        else:
            print(i, 'no es un caracter codificable')

def buscar_letra(letra, arbol, valor):
    if arbol != None:
        if arbol.valor != None:
            valor += arbol.valor

        if letra != arbol.letra:
            buscar_letra(letra, arbol.izq, valor)
            buscar_letra(letra, arbol.der, valor)
        else:
            print(valor)


def descomprimir(raiz, arbol, mensaje, i):
    if i <= len(mensaje)-1:
        if arbol.valor != None:
            if mensaje[i] == arbol.valor and arbol.der != None:
                descomprimir(raiz, arbol.izq, mensaje, i+1)
                descomprimir(raiz, arbol.der, mensaje, i+1)
            elif arbol.der == None and mensaje[i] == arbol.valor:
                print(arbol.letra)
                descomprimir(raiz, raiz, mensaje, i+1)
        else:
            descomprimir(raiz, arbol.izq, mensaje, i)
            descomprimir(raiz, arbol.der, mensaje, i)