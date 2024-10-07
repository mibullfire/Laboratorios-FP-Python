from typing import NamedTuple,List,Tuple
from datetime import datetime, date, time
import csv

Entreno=NamedTuple("Entreno",[('tipo',str),('fechahora',date),('ubicación',str),('duración',int),
                              ('calorías',int),('distancia',float),('frecuencia',int),('compartido',bool),('peso_antes',float),('peso_despues',float)])

def parse_compartidos(cadena:str)->None:
    if cadena == 'S':
        return True
    else:
        return 

def parse_fechahora(cadena:str)->None:
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")
def parse_float(cadena:str)->None:
    return float(cadena.replace(',', '.'))
    
def lee_entrenos(fichero:str)->list[Entreno]:
    res = []

    with open(fichero, encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido, peso_antes, peso_despues in lector:
            fechahora = parse_fechahora(fechahora) # Se podría escribir directamente aquí sin hacer un parse
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = parse_float(distancia)
            frecuencia = int(frecuencia)
            compartido = parse_compartidos(compartido)
            # compartido = compartido == 'S' Es otra forma de escribirlo, para no tener que hacer una función auxiliar para parsear el valor.
            peso_antes = parse_float(peso_antes)
            peso_despues = parse_float(peso_despues)
            entreno = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido, peso_antes, peso_despues)
            res.append(entreno)
    
    return res

def promedio_perdida_peso(lista:list[Entreno], ubicacion:str)->float:
    caja = [i.peso_antes - i.peso_despues for i in lista if i.ubicación == ubicacion]
    return sum(caja)/len(caja)

def cuenta_distintos_tipos(lista:list[Entreno])->int:
    res = set(i.tipo for i in lista)
    return len(res)

def obtiene_horas_mas_perdida_de_peso(lista:list[Entreno], peso_minimo:float)->list:
    res = [i.fechahora.time() for i in lista if i.peso_antes - i.peso_despues > peso_minimo]
    return res