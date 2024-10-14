from collections import namedtuple
from datetime import *
import csv

Viaje = namedtuple('Viaje', 'codigo, fec_sal, fec_reg, ciudades, numer_per, ppp, seguro')

def parse_date1(string: str) -> date:
    return datetime.strptime(string, '%d/%m/%y').date()

def parse_date2(string:str)->date:
    return datetime.strptime(string, '%Y-%m-%d').date()

def parse_lista(string:str)->list:
    string = string.replace('[', '')
    string = string.replace(']', '')
    #También se peude hacer con string = string.split('[]')
    return string.split(" - ")

def parse_float(string:str)->float:
    return float(string.replace(',', '.'))

def parse_bool(string:str)->bool:
    return string == 'true'

def lee_viajes(fichero):
    res = []

    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)

        for codigo, fec_sal, fec_reg, ciudades, numer_per, ppp, seguro in lector:
            res.append(Viaje(codigo, parse_date1(fec_sal), parse_date2(fec_reg), parse_lista(ciudades), int(numer_per), parse_float(ppp), parse_bool(seguro)))
    
    return res

def ciudades_distintas(lista:list)->set:
    res = set()
    for i in lista:
        for j in i.ciudades:
            res.add(j)
    return sorted(list(res))

'''
def ciudades_distintas(lista:list)->set:
    viajes_distintos = set()
    for viaje in lista:
        viajes_distintos.update(viaje.ciudades)
    return sorted(viajes_distintos)
'''

def viajes_visitan_en_fecha(lista: list, ciudad: str, fecha: date = None) -> list:
    res = []
    for viaje in lista:
        if ciudad in viaje.ciudades and (fecha is None or viaje.fec_sal <= fecha <= viaje.fec_reg):
            res.append(viaje)
    return res

def max_ciudades(lista: list) -> int:
    return max([len(i.ciudades) for i in lista])

def viajes_que_visitan_mas_ciudades(lista: list)->list:
    return [(i.codigo, i.fec_sal, i.fec_reg, i.ciudades) for i in lista if len(i.ciudades) == max_ciudades(lista)]

def dias_entre_fechas(fecha1: date, fecha2: date) -> int:
    return (fecha2 - fecha1).days

def n_viajes_mas_importe(lista: list, año: int, n: int) -> list:
    res = [(i.codigo, dias_entre_fechas(i.fec_sal, i.fec_reg), i.numer_per, i.ppp, i.numer_per*i.ppp) for i in lista if i.fec_sal.year == año]
    return sorted(res, key = lambda x: x[4], reverse = True)[:n]