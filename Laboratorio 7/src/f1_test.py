from f1 import *
from config import *
from colorama import Fore

def test_leer_fichero(fichero):
    print(Fore.BLUE + '\ntest_leer_fichero')
    res = lee_carreras(fichero)
    print(f'Se han leído {len(res)} registros!')
    print('Mostrando los dos primeros registros:')
    for i in range(0,2):
        print(f'{i+1} ---> {res[i]}')

def test_media_tiempo_boxes(lista, ciudad, fecha=None):
    print(Fore.GREEN + '\ntest_media_tiempo_boxes')
    print(f'La media de tiempo en boxes en {ciudad} el día {fecha} es de {media_tiempo_boxes(lista, ciudad, fecha)}')

def test_pilotos_menor_tiempo_medio_vueltas_top(lista, n):
    print(Fore.YELLOW + '\ntest_pilotos_menor_tiempo_medio_vueltas_top')
    res = pilotos_menor_tiempo_medio_vueltas_top(lista, n)
    print(f'Los {n} pilotos con menor tiempo medio en vueltas top son:')
    for i in range(0,n):
        print(f'{i+1} ---> {res[i]}')

def test_ratio_tiempo_boxes_total(lista):
    print(Fore.MAGENTA + '\ntest_ratio_tiempo_boxes_total')
    res = ratio_tiempo_boxes_total(lista)
    print(f'Hay {len(res)} registros!')
    print('Los ratios de tiempo en boxes respecto al total son:')
    for i in range(0,4):
        print(f'{i+1} ---> {res[i]}')

def test_mejor_escuderia_año(lista, a):
    print(Fore.CYAN + '\ntest_mejor_escuderia_año')
    res = mejor_escuderia_año(lista, a)
    print(f'La mejor escudería del año {a} es {res}')

def test_puntos_piloto_años(lista):
    print(Fore.RED + '\ntest_puntos_piloto_años')
    res = puntos_piloto_años(lista)
    print(f'Hay {len(res)} registros!')
    print('Los puntos de los pilotos por año son:')
    print(res)

def main():
    test_leer_fichero(fichero)
    lista = lee_carreras(fichero)
    test_media_tiempo_boxes(lista, 'Barcelona')
    test_media_tiempo_boxes(lista, 'Barcelona', date(2023, 5, 7))
    test_media_tiempo_boxes(lista, 'Lepe')
    test_pilotos_menor_tiempo_medio_vueltas_top(lista, 4)
    test_ratio_tiempo_boxes_total(lista)
    test_mejor_escuderia_año(lista, 2022)
    test_puntos_piloto_años(lista)
    print(Fore.RESET)

if __name__ == '__main__':
    main()