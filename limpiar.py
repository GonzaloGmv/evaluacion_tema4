import pandas as pd

def limpiar():
    df = pd.read_csv('pokemon.csv')
    df.rename(columns={'Type 1':'Type'}, inplace=True)
    del([df['Type 2'], df['Total'], df['HP'], df['Attack'], df['Defense'], df['Sp. Atk'], df['Sp. Def'], df['Speed'], df['Generation'], df['Legendary']])
    deb1 = []
    deb2 = []
    deb3 = []
    deb4 = []
    deb5 = []

    for i in df['Type']:
        if i == 'Grass':
            deb1.append('Ice')
            deb2.append('Flying')
            deb3.append('Bug')
            deb4.append('Poison')
            deb5.append(0)
        elif i == 'Fire':
            deb1.append('Water')
            deb2.append('Ground')
            deb3.append('Rock')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Water':
            deb1.append('Grass')
            deb2.append('Electric')
            deb3.append(0)
            deb4.append(0)
            deb5.append(0)
        elif i == 'Bug':
            deb1.append('Flying')
            deb2.append('Fire')
            deb3.append('Rock')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Normal':
            deb1.append('Fighting')
            deb2.append(0)
            deb3.append(0)
            deb4.append(0)
            deb5.append(0)
        elif i == 'Poison':
            deb1.append('Ground')
            deb2.append('Psychic')
            deb3.append(0)
            deb4.append(0)
            deb5.append(0)
        elif i == 'Electric':
            deb1.append('Ground')
            deb2.append(0)
            deb3.append(0)
            deb4.append(0)
            deb5.append(0)
        elif i == 'Ground':
            deb1.append('Ice')
            deb2.append('Water')
            deb3.append('Grass')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Fairy':
            deb1.append('Poison')
            deb2.append('Steel')
            deb3.append(0)
            deb4.append(0)
            deb5.append(0)
        elif i == 'Fighting':
            deb1.append('Flying')
            deb2.append('Fairy')
            deb3.append('Psychic')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Psychic':
            deb1.append('Bug')
            deb2.append('Ghost')
            deb3.append('Dark')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Rock':
            deb1.append('Water')
            deb2.append('Grass')
            deb3.append('Ground')
            deb4.append('Steel')
            deb5.append('Fighting')
        elif i == 'Ghost':
            deb1.append('Ghost')
            deb2.append('Dark')
            deb3.append(0)
            deb4.append(0)
            deb5.append(0)
        elif i == 'Ice':
            deb1.append('Ground')
            deb2.append('Fire')
            deb3.append('Fighting')
            deb4.append('Steel')
            deb5.append(0)
        elif i == 'Dragon':
            deb1.append('Ice')
            deb2.append('Fairy')
            deb3.append('Dragon')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Dark':
            deb1.append('Bug')
            deb2.append('Fighting')
            deb3.append('Psychic')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Steel':
            deb1.append('Ground')
            deb2.append('Fire')
            deb3.append('Fighting')
            deb4.append(0)
            deb5.append(0)
        elif i == 'Flying':
            deb1.append('Ice')
            deb2.append('Electric')
            deb3.append('Rock')
            deb4.append(0)
            deb5.append(0)

    df['Debilidad 1'] = pd.DataFrame(deb1)
    df['Debilidad 2'] = pd.DataFrame(deb2)
    df['Debilidad 3'] = pd.DataFrame(deb3)
    df['Debilidad 4'] = pd.DataFrame(deb4)
    df['Debilidad 5'] = pd.DataFrame(deb5)
    return df