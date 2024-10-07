from collections import namedtuple
import csv
from datetime import *
Pelicula = namedtuple('Pelicula', 'fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto, premiada')

def parse_fecha(string:str)->datetime:
    return datetime.strptime(string, '%d-%m-%Y').date()

def parse_tiempo(string:str)->datetime:
    return datetime.strptime(string, '%H:%M').time()

def parse_generos(string:str)->list:
    return string.split('#')

def parse_float(string:str)->float:
    return float(string.replace(',', '.'))

def lee_peliculas(fichero:str)->list:

    res = []

    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)

        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto, premiada in lector:
            fecha_estreno = parse_fecha(fecha_estreno)
            generos = parse_generos(generos)
            duracion = parse_tiempo(duracion)
            presupuesto = float(presupuesto)
            recaudacion = parse_float(recaudacion)
            reparto = reparto.split('-')
            premiada = premiada == 'true'

            res.append(Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto, premiada))

    return res

# Ejercicio 3
# Da error, no da la fecha maxima
def ultima_pelicula_premiada(lista:list)->Pelicula:
    res = max(filter(lambda x: x.premiada, lista), key = lambda x: x.fecha_estreno)
    return (res.titulo, res.fecha_estreno, res.duracion, res.generos)

# Ejercicio 4
def n_premiadas_mayor_recaudacion(lista:list, condicion:str, n:int)->list:
    if condicion == 'SI':
        res = sorted(filter(lambda x: x.premiada, lista), key = lambda x: x.recaudacion, reverse = True)[:n]
    else:
        res = sorted(filter(lambda x: not x.premiada, lista), key = lambda x: x.recaudacion, reverse = True)[:n]
    return [(i.titulo, i.recaudacion, i.director) for i in res]