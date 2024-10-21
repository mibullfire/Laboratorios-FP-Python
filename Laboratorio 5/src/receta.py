import csv
from datetime import *
from typing import * # Cuando la NamedTuple está definida con mayúsculas, hay que importarla del typing, no de collections 

# Namedtuples dadas:
Ingrediente = NamedTuple("Ingrediente",
					     [("nombre",str),
						  ("cantidad",float),
						  ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominación", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", Optional[List[Ingrediente]]),
                     ("tiempo", int),
                     ("calorías", int),
                     ("fecha", date),
                     ("precio", float)])

def parse_fecha(cadena:str)->date:
    return datetime.strptime(cadena, '%d/%m/%Y').date()

def parse_float(cadena:str)->float:
    return float(cadena.replace(',', '.'))

def parse_ingredientes(cadena:str)->Optional[List[Ingrediente]]:
    if cadena == '':  
        return None
    else:
        ingredientes = cadena.split(',')
        res = []
        
        for i in ingredientes:
            # fresas-5-u
            nombre, cantidad, unidad = i.split('-')
            res.append(Ingrediente(nombre, float(cantidad), unidad)) 
        return res

def lee_recetas(fichero:str)->list[Receta]:
    res = []
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)

        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            res.append(Receta(denominacion, tipo, dificultad, parse_ingredientes(ingredientes), int(tiempo), int(calorias), parse_fecha(fecha), parse_float(precio)))
           
    return res

def diferentes_ingredientes(lista:List[Receta], unidad=None)->int:
    lista_ingredientes = [i.ingredientes for i in lista if i.ingredientes]
    res = set([ii.nombre for i in lista_ingredientes for ii in i if unidad == None or ii.unidad == unidad])
    ''' Prueba:
    res = set()
    for i in lista_ingredientes:
        for ii in i:
            if ii.unidad == unidad:
                res.add(ii.nombre)
    '''

    ''' Del profesor:
    ingredientes = set()
    for r in lista:
        if r.ingredientes != None:
            for i in r.ingredientes:
                if unidad == None or i.unidad == unidad:
                    res.add(i.nombre)
    return len(ingredientes)
    '''
    return len(res)

def recetas_con_ingredientes(lista:List[Receta], ingredientes:List[str])->Set[tuple]:
    res = set()
    for i in lista:
        if i.ingredientes:
            for ii in i.ingredientes:
                if ii.nombre in ingredientes:
                    res.add((i.denominación, i.calorías, i.precio))
    return res

def receta_mas_barata(lista:List[Receta], tipo:List, num:int=None)->list[Receta]:
    res = [i for i in lista if i.tipo in tipo]
    if num:
        res.sort(key = lambda x: x.calorías)
        res = res[:num]
        res.sort(key = lambda x: x.precio)
        return res[0]
    else:
        res.sort(key = lambda x: x.precio)
        return res[0] 