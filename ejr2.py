import random
from limpiar import limpiar

df = limpiar('pokemon.csv')

class Pokemon:
    def __init__(self, numero, nombre, tipo, deb1, deb2, deb3, deb4, deb5):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.deb1 = deb1
        self.deb2 = deb2
        self.deb3 = deb3
        self.deb4 = deb4
        self.deb5 = deb5

class NodoName:
    def __init__(self, izq, der, nombre, pokemon):
        self.izq = izq
        self.der = der
        self.nombre = nombre
        self.pokemon = pokemon

class NodoNumero:
    def __init__(self, izq, der, numero, pokemon):
        self.izq = izq
        self.der = der
        self.numero = numero
        self.pokemon = pokemon

class NodoTipo:
    def __init__(self, izq, der, tipo, pokemon):
        self.izq = izq
        self.der = der
        self.tipo = tipo
        self.pokemon = pokemon

def crear_pokemons(df):
    pokemons = []
    for i in range(len(df)):
        pokemons.append(Pokemon(df.iloc[i]['#'], df.iloc[i]['Name'], df.iloc[i]['Type'], df.iloc[i]['Debilidad 1'], df.iloc[i]['Debilidad 2'], df.iloc[i]['Debilidad 3'], df.iloc[i]['Debilidad 4'], df.iloc[i]['Debilidad 5']))
    random.shuffle(pokemons)
    # Esto lo hago porque el ejercicio dice que los pokemons están desordenados
    return pokemons

def crear_nodo(atributo, izq, der, pokemon):
    if pokemon == None:
        atr = None
    elif pokemon != None and atributo == 'Name':
        atr = pokemon.nombre
    elif pokemon != None and atributo == '#':
        atr = pokemon.numero
    elif pokemon != None and atributo == 'Type':
        atr = pokemon.tipo

    if atributo == 'Name':
        nodo = NodoName(izq, der, atr , pokemon)
    elif atributo == '#':
        nodo = NodoNumero(izq, der, atr, pokemon)
    elif atributo == 'Type':
        nodo = NodoTipo(izq, der, atr, pokemon)
    return nodo

def arbol(atributo):
    lista = crear_pokemons(df)
    nodos = []
    for i in lista:
        nodos.append(crear_nodo(atributo, None, None, i))
    while len(nodos) > 1:
        a = 0
        if len(nodos) == 2:
            izq = nodos.pop(a)
            der = nodos.pop(a)
            raiz = crear_nodo(atributo, izq, der, None)
            nodos.append(raiz)
        else:
            while a <= len(nodos)-3:
                izq = nodos.pop(a)
                der = nodos.pop(a)
                nodos[a].izq = izq
                nodos[a].der = der
                a += 1
    return nodos

arbol_nombre = arbol('Name')
arbol_numero = arbol('#')
arbol_tipo = arbol('Type')