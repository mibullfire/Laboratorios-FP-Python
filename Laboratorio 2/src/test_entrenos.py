from entrenos import *

def test_lee_entrenos(fichero):
    res = lee_entrenos(fichero)
    print(f'\nTest_lee_entrenos')
    print(f'Número de registros leídos: {len(res)}')
    print(f'Los dos primeros: {res[:2]}')
    print(f'Lod dos últimos: {res[-2:]}')

def test_filtra_por_tipo(fichero, tipo):
    lista = lee_entrenos(fichero)
    print(f'\nTest_filtra_por_tipo')
    print(f'Los etrenamoentos con el tipo {tipo} son: {filtra_por_tipo(lista, tipo)}')

def test_suma_de_calorias(fichero, tipo):
    lista = lee_entrenos(fichero)
    print('\nTest_suma_de_calorias')
    print(f'Los entrenamientos con el tipo {tipo} han consumido {suma_de_calorias(lista, tipo)} calorías.')

def main():
    fichero = './data/entrenos.csv'
    test_lee_entrenos(fichero)
    test_filtra_por_tipo(fichero, 'Remo')
    test_suma_de_calorias(fichero, 'Senderismo')

if __name__ == '__main__':
    main()