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
    a = -1
    nodo = crear_nodo(atributo, None, None, None)
    for i in nodos:
        a += 1
        nodo = agregar(nodo, i, a)
    return nodo

def agregar(nodo, pokemon, a):
    if nodo != None:
        if a == 0:
            nodo.izq = pokemon
        else:
            if nodo.izq == None:
                nodo.izq = pokemon
            elif nodo.der == None:
                nodo.der = pokemon
            else:
                if a%2 == 1:
                    agregar(nodo.izq, pokemon, a)
                else:
                    agregar(nodo.der, pokemon, a)
    return nodo

def buscar_numero(arbol, numero):
    if numero < 1 or numero > 721:
        print('Ese numero no corresponde a ningun pokemon')
    else: 
        if arbol != None:
            if numero != arbol.numero:
                buscar_numero(arbol.izq, numero)
                buscar_numero(arbol.der, numero)
            else:
                pokemon = arbol.pokemon
                print('Numero: ', pokemon.numero)
                print('Nombre: ', pokemon.nombre)
                print('Tipo: ', pokemon.tipo, '\n')

def buscar_nombre(arbol, nombre):
    if arbol != None:
        if arbol.nombre != None:
            arbol.nombre = arbol.nombre.lower()
            if nombre in arbol.nombre:
                pokemon = arbol.pokemon
                print('Numero: ', pokemon.numero)
                print('Nombre: ', pokemon.nombre)
                print('Tipo: ', pokemon.tipo, '\n')
                buscar_nombre(arbol.izq, nombre)
                buscar_nombre(arbol.der, nombre)
            else:
                buscar_nombre(arbol.izq, nombre)
                buscar_nombre(arbol.der, nombre)
        else:
            buscar_nombre(arbol.izq, nombre)
            buscar_nombre(arbol.der, nombre)

def buscar_tipo(arbol, tipo):
    tipo = tipo.capitalize()
    if arbol != None:
        if tipo != arbol.tipo:
            buscar_tipo(arbol.izq, tipo)
            buscar_tipo(arbol.der, tipo)
        else:
            pokemon = arbol.pokemon
            print('Numero: ', pokemon.numero)
            print('Nombre: ', pokemon.nombre)
            print('Tipo: ', pokemon.tipo, '\n')
            buscar_tipo(arbol.izq, tipo)
            buscar_tipo(arbol.der, tipo)

def listado_ascendente(raiz, arbol, i):
    if arbol != None:
        if arbol.numero != i:
            listado_ascendente(raiz, arbol.izq, i)
            listado_ascendente(raiz, arbol.der, i)
        else:
            pokemon = arbol.pokemon
            print('Numero: ', pokemon.numero)
            print('Nombre: ', pokemon.nombre)
            print('Tipo: ', pokemon.tipo, '\n')
            listado_ascendente(raiz, raiz, i+1)

arbol_nombre = arbol('Name')
arbol_numero = arbol('#')
arbol_tipo = arbol('Type')

'''
buscar_numero(arbol_numero, int(input('Escriba el numero del pokemon que desea encontrar: ')))
buscar_nombre(arbol_nombre, input('Escriba el nombre del pokemon que desea encontrar: '))
buscar_tipo(arbol_tipo, input('Escriba el tipo de los pokemons que desea encontrar: '))
'''
try:
    listado_ascendente(arbol_numero, arbol_numero, 1)
except RecursionError:
    print('No se puede seguir con el listado, hay demasiados pokemons. RecursionError: maximum recursion depth exceeded. ')