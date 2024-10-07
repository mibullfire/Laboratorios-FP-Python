from collections import namedtuple
import csv
from datetime import *
Pelicula = namedtuple('Pelicula', 'fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto')

def parse_fecha(string:str)->datetime:
    return datetime.strptime(string, '%d-%M-%Y')

def parse_tiempo(string:str)->datetime:
    return datetime.strptime(string, '%H:%M')

def parse_generos(string:str)->list:
    return string.split('#')

def parse_float(string:str)->float:
    return float(string.replace(',', '.'))

def lee_peliculas(fichero:str)->list:

    res = []

    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)

        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = parse_fecha(fecha_estreno)
            generos = parse_generos(generos)
            duracion = parse_tiempo(duracion)
            presupuesto = parse_float(presupuesto)
            recaudacion = parse_float(recaudacion)
            reparto = reparto.split('-')

            res.append(Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto))

    return res

def pelicula_mas_cara(lista:list)->Pelicula:
    return max(lista, key = lambda x: x.presupuesto)

def pelicula_menos_beneficio(lista:list)->tuple:
    pelicula = min(lista, key = lambda x: x.recaudacion - x.presupuesto)
    beneficio = pelicula.recaudacion - pelicula.presupuesto
    return (pelicula.titulo, beneficio)

def n_peliculas_mas_largas(lista:list, n:int)->list:
    return sorted(lista, key = lambda x: x.duracion, reverse = True)[:n]