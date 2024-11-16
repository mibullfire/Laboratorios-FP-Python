from collections import namedtuple
import csv
from datetime import *
from typing import *

carrera = namedtuple('Carrera', 'nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, posicion_final, ciudad, top_6_vueltas, tiempo_boxes, nivel_liquido')

def parse_vueltas(cadena:str)->list[Union[int, float]]:
    res = []
    cadena = cadena.strip('[] ')
    cadena = cadena.split('/')
    for i in cadena:
        if i == ' -':
            res.append(0)
        else:
            res.append(float(i))
    return res

def lee_carreras(fichero:str)->list[carrera]:
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for nombre, escuderia, fecha_carrera, temperatura_min, vel_max, duracion, posicion_final, ciudad, top_6_vueltas, tiempo_boxes, nivel_liquido in lector:
            res.append(carrera(nombre, escuderia, datetime.strptime(fecha_carrera, '%d-%m-%y').date(), int(temperatura_min), float(vel_max), float(duracion), int(posicion_final), ciudad, parse_vueltas(top_6_vueltas), float(tiempo_boxes), nivel_liquido==1))
    return res

def media_tiempo_boxes(lista:list[carrera], ciudad:str, fecha:Optional[date]=None)->Union[int,float]:
    res = [i.tiempo_boxes for i in lista if ciudad == i.ciudad and (fecha == None or fecha == i.fecha_carrera)]
    if res:
        return sum(res)/len(res)
    else: return 0

def pilotos_menor_tiempo_medio_vueltas_top(lista:list[carrera], n:int)->list[tuple[str, date]]:
    filtro6 = [(i.nombre, i.fecha_carrera, sum(i.top_6_vueltas)/len(i.top_6_vueltas)) for i in lista if 0 not in i.top_6_vueltas]
    tuplas = sorted(filtro6, key = lambda x: x[2])
    return [(i[0], i[1]) for i in tuplas][:n]

def aux_dict_ratios(lista:list[carrera])->dict:
    dicc = {}
    for i in lista:
        if i.fecha_carrera not in dicc:
            dicc[i.fecha_carrera] = []
        dicc[i.fecha_carrera].append(i.tiempo_boxes)
    for key in dicc:
        dicc[key] = sum(dicc[key])
    return dicc

def ratio_tiempo_boxes_total(lista:list[carrera])->list[tuple[str, date, float]]:
    ratios = aux_dict_ratios(lista)
    res = []

    for i in lista:
        ratio_total = ratios[i.fecha_carrera]
        ratio = i.tiempo_boxes / ratio_total
        res.append((i.nombre, str(i.fecha_carrera), round(ratio, 3)))
    return sorted(res, key = lambda x: x[2], reverse=True)

def mejor_escuderia_año(lista:list[carrera], a:date.year)->str:
    filtro = filter(lambda x: x.fecha_carrera.year == a, lista)
    dicc = {}
    for i in filtro:
        if i.posicion_final == 1:
            if i.escuderia not in dicc:
                dicc[i.escuderia] = 1
            else: dicc[i.escuderia] =+ 1
    if not dicc:
        raise ValueError("No hay escuderías con victorias en el año especificado")
    else: 
        maximo = max(dicc.items(), key = lambda x: x[1])
        return maximo[0]

def aux_puntos(puesto:int)->int:
    if puesto == 1:
        return 50
    if puesto == 2:
        return 25
    if puesto == 3:
        return 10
    else: return 0
    
def puntos_piloto_años(lista:list[carrera])->dict:
    '''
    Nota: para esta última función falta dividir los puntos del final en años, ya que se muestran todos juntos...
    '''
    dc = {}
    # años = (i.fecha_carrera.year for i in lista)
    for i in lista:
        if i.nombre not in dc:
            dc[i.nombre] = aux_puntos(i.posicion_final)
        else: dc[i.nombre] += aux_puntos(i.posicion_final)
    return [dc.items()]

