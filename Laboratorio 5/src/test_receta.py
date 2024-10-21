from receta import *
from config import *
from colorama import Fore

def test_lee_receta(fichero):
    lista = lee_recetas(fichero)
    print(Fore.RED, '\ntest_lee_receta')
    print(f'Hay {len(lista)} recetas')
    print(lista)

def test_diferentes_ingredientes(fichero, unidad=None):
    lista = lee_recetas(fichero)
    print(Fore.GREEN, '\ntest_diferentes_ingredientes')
    if unidad:
        print(f'Hay {diferentes_ingredientes(lista, unidad)} ingredientes diferentes de la unidad {unidad}')
    else:
        print(f'Hay {diferentes_ingredientes(lista)} ingredientes diferentes')

def test_recetas_con_ingredientes(fichero, lista_ingredientes):
    lista = lee_recetas(fichero)
    print(Fore.BLUE, '\ntest_recetas_con_ingredientes')
    print(f'Hay {recetas_con_ingredientes(lista, lista_ingredientes)} recetas con los ingredientes {lista_ingredientes}')

def test_receta_mas_barata(fichero, tipo, num=None):
    lista = lee_recetas(fichero)
    print(Fore.YELLOW, '\ntest_receta_mas_barata')
    if num:
        print(f'Las {num} recetas más baratas de tipo {tipo} son:')
        print (receta_mas_barata(lista, tipo, num))
    else:
        print(f'La receta más barata de tipo {tipo} es:')
        print(receta_mas_barata(lista, tipo))

def main():
    test_lee_receta(fichero)
    test_diferentes_ingredientes(fichero)
    test_diferentes_ingredientes(fichero, 'gr')
    test_diferentes_ingredientes(fichero, 'cl')
    test_recetas_con_ingredientes(fichero, ['harina', 'azúcar'])
    test_receta_mas_barata(fichero, ['Entrante','Postre'])
    test_receta_mas_barata(fichero, ['Plato Principal','Postre'], 5)
    Fore.RESET

if __name__ == '__main__':
    main()