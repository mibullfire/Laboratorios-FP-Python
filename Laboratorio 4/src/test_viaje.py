from viaje import *

def test_lee_viajes(fichero):
    res = lee_viajes(fichero)
    print(f'El número de viajes leídos es: {len(res)}')
    print(f'Los dos primeros: {res[:2]}')

def test_ciudades_distintas(lista):
    res = ciudades_distintas(lista)
    print('\ntest_ciudades_distintas:')
    print(f'Las distintas ciudades para viajar son: {res}')

def test_viajes_visitan_en_fecha(lista):
    res = viajes_visitan_en_fecha(lista, 'Roma', date(2024, 8, 15)) 
    print('\ntest_viajes_visitan_en_fecha:')
    print(f'Los viajes que visitan Roma el 15/08/2024 son: {res}')

def test_viajes_que_visitan_mas_ciudades(lista):
    res = viajes_que_visitan_mas_ciudades(lista)
    print('\ntest_viajes_que_visitan_mas_ciudades:')
    for tupla in res:
        print(f'--> {tupla}')

def test_n_viajes_mas_importe(lista, año, n):
    res = n_viajes_mas_importe(lista, año, n)
    print('\ntest_n_viajes_mas_importe:')
    print(f'Los {n} viajes con mayor importe en el año {año} son:')
    for tupla in res:
        print(f'--> {tupla}')

def main():
    fichero = './data/viajes.csv'
    test_lee_viajes(fichero)
    lista = lee_viajes(fichero)
    test_ciudades_distintas(lista)
    test_viajes_visitan_en_fecha(lista)
    test_viajes_que_visitan_mas_ciudades(lista)
    test_n_viajes_mas_importe(lista, 2024, 5)

if __name__ == '__main__':
    main()