from ejercicio2.limpiar import limpiar
from ejercicio2.ejr2 import *

def main2():
    df = limpiar('ejercicio2/pokemon.csv')
    arbol_nombre = arbol('Name', df)
    arbol_numero = arbol('#', df)
    arbol_tipo = arbol('Type', df)
    buscar_numero(arbol_numero, int(input('Escriba el numero del pokemon que desea encontrar: ')))
    buscar_nombre(arbol_nombre, input('Escriba el nombre del pokemon que desea encontrar: '))
    buscar_tipo(arbol_tipo, input('Escriba el tipo de los pokemons que desea encontrar: '))
    input('Pulse intro para seguir con el siguiente apartado ')
    try:
        listado_ascendente(arbol_numero, arbol_numero, 1)
    except RecursionError:
        print('No se puede seguir con el listado, hay demasiados pokemons. RecursionError: maximum recursion depth exceeded. ')
    input('Pulse intro para seguir con el siguiente apartado ')
    buscar_nombre(arbol_nombre, 'lycanroc')
    buscar_nombre(arbol_nombre, 'jolteon')
    buscar_nombre(arbol_nombre, 'tyrantrum')
    print('Utilizando la funcion "buscar_nombre(), vemos que Lycanroc no esta en este dataset, que Jolteon es tipo "Electric", y que "Tyrantrum" es tipo "Rock.')
    input('Pulse intro para buscar los pokemons debiles frente a Jolteon ')
    buscar_deb(arbol_tipo, 'Electric')
    input('Pulse intro para buscar los pokemons debiles frente a Tyrantrum ')
    buscar_deb(arbol_tipo, 'Rock')