from limpiar import limpiar

df = limpiar()

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

def crear_pokemons(df):
    pokemons = []
    for i in range(len(df)):
        pokemons.append(Pokemon(df.iloc[i]['#'], df.iloc[i]['Name'], df.iloc[i]['Type'], df.iloc[i]['Debilidad 1'], df.iloc[i]['Debilidad 2'], df.iloc[i]['Debilidad 3'], df.iloc[i]['Debilidad 4'], df.iloc[i]['Debilidad 5']))
    return pokemons
