import csv
from datetime import *
from typing import *  # Cuando la NamedTuple está definida con mayúsculas, hay que importarla del typing, no de collections 

# Definición de NamedTuples:
Ingrediente = NamedTuple("Ingrediente",
                         [("nombre", str),  # Nombre del ingrediente
                          ("cantidad", float),  # Cantidad del ingrediente
                          ("unidad", str)])  # Unidad de medida del ingrediente

Receta = NamedTuple("Receta",
                    [("denominación", str),  # Nombre de la receta
                     ("tipo", str),  # Tipo de receta (ej. postre, plato principal)
                     ("dificultad", str),  # Dificultad de la receta
                     ("ingredientes", Optional[List[Ingrediente]]),  # Lista de ingredientes (puede ser None)
                     ("tiempo", int),  # Tiempo de preparación en minutos
                     ("calorías", int),  # Calorías de la receta
                     ("fecha", date),  # Fecha de creación de la receta
                     ("precio", float)])  # Precio de la receta

# Función para parsear una fecha desde una cadena
def parse_fecha(cadena: str) -> date:
    return datetime.strptime(cadena, '%d/%m/%Y').date()

# Función para parsear un número flotante desde una cadena
def parse_float(cadena: str) -> float:
    return float(cadena.replace(',', '.'))

# Función para parsear una lista de ingredientes desde una cadena
def parse_ingredientes(cadena: str) -> Optional[List[Ingrediente]]:
    if cadena == '':  
        return None  # Si la cadena está vacía, retorna None
    else:
        ingredientes = cadena.split(',')  # Divide la cadena por comas
        res = []
        
        for i in ingredientes:
            # Ejemplo de formato: fresas-5-u
            nombre, cantidad, unidad = i.split('-')
            res.append(Ingrediente(nombre, float(cantidad), unidad))  # Crea un objeto Ingrediente y lo añade a la lista
        return res

# Función para leer recetas desde un fichero CSV
def lee_recetas(fichero: str) -> list[Receta]:
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)  # Salta la cabecera del CSV

        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            res.append(Receta(denominacion, tipo, dificultad, parse_ingredientes(ingredientes), int(tiempo), int(calorias), parse_fecha(fecha), parse_float(precio)))
           
    return res

# Función para contar el número de ingredientes diferentes en una lista de recetas
def diferentes_ingredientes(lista: List[Receta], unidad=None) -> int:
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

# Función para obtener recetas que contienen ciertos ingredientes
def recetas_con_ingredientes(lista: List[Receta], ingredientes: List[str]) -> Set[tuple]:
    res = set()
    for i in lista:
        if i.ingredientes:
            for ii in i.ingredientes:
                if ii.nombre in ingredientes:
                    res.add((i.denominación, i.calorías, i.precio))
    return res

# Función para obtener la receta más barata de un cierto tipo
def receta_mas_barata(lista: List[Receta], tipo: List, num: int = None) -> list[Receta]:
    res = [i for i in lista if i.tipo in tipo]
    if num:
        res.sort(key=lambda x: x.calorías)  # Ordena por calorías
        res = res[:num]  # Toma las primeras 'num' recetas
        res.sort(key=lambda x: x.precio)  # Ordena por precio
        return res[0]  # Retorna la receta más barata
    else:
        res.sort(key=lambda x: x.precio)  # Ordena por precio
        return res[0]  # Retorna la receta más barata