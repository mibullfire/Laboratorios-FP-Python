from typing import *
from datetime import *
import csv

Video = NamedTuple('Video', 
[('id_video', str),
 ('fecha_trending', date),
 ('titulo',str),
 ('canal', str),
 ('categoria', str),
 ('visitas', int),
 ('likes', int),
 ('dislikes', int)
])

def parse_fecha(cadena:str)->date:
    return datetime.strptime(cadena, '%d/%m/%Y').date()


def lee_trending_videos(fichero:str)->list[Video]:
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for id,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            res.append(Video(id, parse_fecha(fecha_trending), titulo, canal, categoria, int(visitas), int(likes), int(dislikes)))
    return res

def media_visitas(lista:list[Video], fecha:date):
    visitas = [i.visitas for i in lista if i.fecha_trending == fecha]
    if not len(visitas):
        return 0
    else: return sum(visitas)/len(visitas)

def video_mayor_ratio_likes_dislikes(lista:list[Video], categoria:Optional[str]=None)->Video:
    filtrado = filter(lambda x: x.dislikes != 0 and (x.categoria == categoria or categoria == None), lista)
    return max(filtrado, key = lambda x: x.likes/x.dislikes)

def canales_top(lista:list[Video], n:int=3)->list[tuple]:
    dicc = {}
    for i in lista:
        if i.canal in dicc:
            dicc[i.canal] += 1
        else: dicc[i.canal] = 1
    return sorted(list(dicc.items()), key = lambda x: x[1], reverse = True)[:n]

def likeability(k:int, likes:int, dislikes:int, visitas:int)->float:
    return (k*likes-dislikes)/(k*visitas)

def video_mas_likeability_por_categoria(lista:list[Video], k:int=20):
    filtro = [(i.categoria, i.id_video, likeability(k, i.likes, i.dislikes, i.visitas)) for i in lista]
    dicc = {}

    for i in filtro:
        if i[0] not in dicc:
            dicc[i[0]] = sorted((x for x in filtro if x[0] ==i[0]), key = lambda x: x[2], reverse=True)[0][1]
    
    return list(dicc.items())

def incrementos_visitas(lista: list[Video], canal: str) -> list:
    # Filtrar videos del canal dado
    visitas = sorted([(x.fecha_trending, x.visitas) for x in lista if x.canal == canal], key=lambda x: x[0])
    
    if not visitas:
        return []

    # Obtener el rango de fechas
    inicio = visitas[0][0]
    final = visitas[-1][0]

    # Crear un diccionario de visitas por día
    visitas_por_dia = {}
    for fecha, visitas_dia in visitas:
        if fecha in visitas_por_dia:
            visitas_por_dia[fecha] += visitas_dia
        else:
            visitas_por_dia[fecha] = visitas_dia

    # Calcular incrementos considerando días sin datos
    incrementos = []
    visitas_anterior = 0

    fecha_cont = inicio
    while fecha_cont <= final:
        visitas_actual = visitas_por_dia.get(fecha_cont, 0)
        incremento = visitas_actual - visitas_anterior
        incrementos.append(incremento)
        visitas_anterior = visitas_actual
        fecha_cont += timedelta(days=1)

    return incrementos