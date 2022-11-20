import sys
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

raiz = huffman(tabla)

def func(mensaje):
    for i in mensaje:
        leer(i, raiz[0], str())

def leer(letra, arbol, valor):
    if arbol != None:
        if arbol.valor != None:
            valor += arbol.valor

        if letra != arbol.letra:
            leer(letra, arbol.izq, valor)
            leer(letra, arbol.der, valor)
        else:
            sol = valor
            if sol != None:
                print(sol)
            
        
func('AF')


