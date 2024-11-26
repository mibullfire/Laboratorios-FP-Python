from youtube import *
from colorama import Fore

def test_lee_trending_videos(fichero:str)->None:
    lista = lee_trending_videos(fichero)
    print(Fore.BLUE + '\ntest_lee_trending_videos')
    print(f'Registros leídos: {len(lista)}')
    print('Los tres primeros son:')
    for i in range (0,3):
        print(f'---> {lista[i]}')

def test_media_visitas(lista:list[Video], fecha:date)->None:
    print(Fore.GREEN + '\ntest_media_visitas')
    print(f'La media de visitas del día: {fecha} es {media_visitas(lista, fecha)}')

def test_video_mayor_ratio_likes_dislikes(lista:list[Video], categoria:Optional[str]=None)->None:
    print(Fore.CYAN + '\ntest_video_mayor_ratio_likes_dislikes')
    print(f'El video con mayor ratio de la categoria {categoria} es: \n{video_mayor_ratio_likes_dislikes(lista, categoria)}')

def test_canales_top(lista:list[Video], n:int=3)->None:
    print(Fore.YELLOW + '\ntest_canales_top')
    print(f'El top-{n} canales es:')
    print(canales_top(lista, n))

def test_video_mas_likeability_por_categoria(lista:list[Video], k:int=20)->None:
    print(Fore.RED + '\ntest_videos_mas_likeability_por_categoria')
    for i in video_mas_likeability_por_categoria(lista):
        print(f'{i[0]} ---> {i[1]}')

def test_incrementos_visitas(lista:list[Video], canal:str)->None:
    print(Fore.MAGENTA + '\ntest_incrementos_visitas')
    print(f'Incrementos de visitas del canal {canal}')
    print(incrementos_visitas(lista, canal))

def main():
    fichero = './data/MX_Youtube_2017_utf8.csv'
    lista = lee_trending_videos(fichero)
    test_lee_trending_videos(fichero)
    test_media_visitas(lista, parse_fecha('15/11/2017'))
    test_video_mayor_ratio_likes_dislikes(lista, 'Education')
    test_canales_top(lista, 3)
    test_video_mas_likeability_por_categoria(lista)
    test_incrementos_visitas(lista, 'Exatlón')


    Fore.RESET

if __name__ == '__main__':
    main()