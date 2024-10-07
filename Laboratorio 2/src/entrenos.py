from typing import NamedTuple,List,Tuple
from datetime import datetime, date, time
import csv

Entreno=NamedTuple("Entreno",[('tipo',str),('fechahora',date),('ubicación',str),('duración',int),
                              ('calorías',int),('distancia',float),('frecuencia',int),('compartido',bool)])

def parse_compartidos(cadena:str)->None:
    if cadena == 'S':
        return True
    else:
        return 

def parse_fechahora(cadena:str)->None:
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")
    
def lee_entrenos(fichero:str)->list[Entreno]:
    res = []

    with open(fichero, encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = parse_fechahora(fechahora) # Se podría escribir directamente aquí sin hacer un parse
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = parse_compartidos(compartido) 
            # compartido = compartido == 'S' Es otra forma de escribirlo, para no tener que hacer una función auxiliar para parsear el valor.
            entreno = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            res.append(entreno)
    
    return res

def filtra_por_tipo(lista:list, tipo:str)->list:
    res = [(i.ubicación, i.distancia) for i in lista if i.tipo == tipo]
    return res

def suma_de_calorias(lista:list, tipo:str)->int:
    res = [i.calorías for i in lista if i.tipo == tipo]
    return sum(res)