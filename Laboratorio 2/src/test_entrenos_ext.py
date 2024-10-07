from entrenos_ext import *

def test_lee_entrenos(fichero):
    res = lee_entrenos(fichero)
    print(f'Se han leido {len(res)} entrenos.')
    print(f'El primer elementos es: {res[0]}')

def test_promedio_perdida_peso(fichero, ubicacion):
    lista = lee_entrenos(fichero)
    promedio = promedio_perdida_peso(lista, ubicacion)
    print('\ntest_promedio_peso')
    print(f'El promedio de perdida de peso en {ubicacion} es: {promedio}')

def test_cuenta_distintos_tipos(fichero):
    lista = lee_entrenos(fichero)
    numero = cuenta_distintos_tipos(lista)
    print('\ntest_cuenta_distintos_tipos')
    print(f'El número de tipos distintos es {numero}')

def test_obtiene_horas_mas_perdida_de_peso(fichero, peso_minimo):
    lista = lee_entrenos(fichero)
    res = obtiene_horas_mas_perdida_de_peso(lista, peso_minimo)
    print(f'Las horas con más pérdida de peso que {peso_minimo} son: {res}')

def main():
    fichero = './data/entrenos_extendido.csv'
    test_lee_entrenos(fichero)
    test_promedio_perdida_peso(fichero, 'Sevilla')
    test_cuenta_distintos_tipos(fichero)
    test_obtiene_horas_mas_perdida_de_peso(fichero, 4.9)

if __name__ == '__main__':
    main()