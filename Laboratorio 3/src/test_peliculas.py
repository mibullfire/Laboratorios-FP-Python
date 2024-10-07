from peliculas import *

def test_lee_peliculas(fichero):
    res = lee_peliculas(fichero)
    print('\ntest_lee_peliculas')
    print('Numero de peliculas:', len(res))
    print(f'Las dos primeras son: {res[:2]}')
    print(f'Las dos ultimas son: {res[-2:]}')

def test_pelicula_mas_cara(fichero):
    res = lee_peliculas(fichero)
    print('\ntest_pelicula_mas_cara')
    print('La pelicula mas cara es:', pelicula_mas_cara(res))

def test_pelicula_menos_beneficio(fichero):
    res = lee_peliculas(fichero)
    print('\ntest_pelicula_menos_beneficio')
    print('La pelicula con menos beneficio es:', pelicula_menos_beneficio(res))

def test_n_peliculas_mas_largas(fichero, n):
    lista = lee_peliculas(fichero)
    res = n_peliculas_mas_largas(lista, n)
    print('\ntest_n_peliculas_mas_largas')
    print(f'Las {n} peliculas mas largas son:')
    for i in res:
        print(f'\n---> {i}')

def main():
    fichero = './data/peliculas.csv'
    test_lee_peliculas(fichero)
    test_pelicula_mas_cara(fichero)
    test_pelicula_menos_beneficio(fichero)
    test_n_peliculas_mas_largas(fichero, 5)

if __name__ == '__main__':
    main()