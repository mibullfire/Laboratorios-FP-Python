from peliculas_ext import *

def test_lee_peliculas(fichero):
    res = lee_peliculas(fichero)
    print('\ntest_lee_peliculas')
    print('Numero de peliculas:', len(res))
    print(f'Las dos primeras son: {res[:2]}')
    print(f'Las dos ultimas son: {res[-2:]}')

def test_ultima_pelicula_premiada(fichero):
    res = lee_peliculas(fichero)
    print('\ntest_ultima_pelicula_premiada')
    print('La ultima pelicula premiada es:', ultima_pelicula_premiada(res))

def test_n_premiadas_mayor_recaudacion(fichero, condicion, n):
    res = lee_peliculas(fichero)
    print('\ntest_n_premiadas_mayor_recaudacion')
    print(f'Las {n} peliculas premiadas con mayor recaudacion son:')
    for i in n_premiadas_mayor_recaudacion(res, condicion, n):
        print(f'\n---> {i}')

def main():
    fichero = './data/peliculas_ext.csv'
    test_lee_peliculas(fichero)
    test_ultima_pelicula_premiada(fichero)
    test_n_premiadas_mayor_recaudacion(fichero, 'SI', 3)

if __name__ == '__main__':
    main()