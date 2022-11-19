tabla = {'A':0.2, 'F':0.17, '1':0.13, '3':0.21, '0':0.05, 'M':0.09, 'T':0.15}

class Nodo:
    def __init__(self, info, der, izq):
        self.info = info
        self.der = der
        self.izq = izq

class Letra:
    def __init__(self, letra, freq):
        self.letra = letra
        self.freq = freq

    
letras = []
for i in tabla.keys():
    letras.append(Letra(i, tabla[i]))

def coctel(lista):
    for i in range(len(lista) - 1, 0, -1):
        control = False
        for j in range(i, 0, -1):
            if lista[j].freq < lista[j - 1].freq:
                lista[j].freq, lista[j - 1].freq = lista[j - 1].freq, lista[j].freq
                control = True
        for j in range(i):
            if lista[j].freq > lista[j + 1].freq:
                lista[j].freq, lista[j + 1].freq = lista[j + 1].freq, lista[j].freq
                control = True
        if control == False:
            break
    return lista

coctel(letras)