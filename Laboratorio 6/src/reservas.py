import csv
from typing import *
from datetime import *

Fecha_Estancia = NamedTuple('Fecha_Estancia', [('fecha_entrada', date), ('fecha_salida', date)])
Reserva = NamedTuple('Reserva', [
    ('nombre', str),
    ('dni', str),
    ('fechas', Fecha_Estancia),
    ('tipo_habitación', str),
    ('num_personas', int),
    ('precio_noche', float),
    ('servicios_adicionales', list)
])

def parse_servicios(cadena: str) -> list:
    if cadena:
        cadena = cadena.strip('"')
        return cadena.split(',')
    else:
        return []

def parse_fecha(cadena:str) -> date:
    return datetime.strptime(cadena, '%Y-%m-%d').date()

def lee_reservas(fichero:str)->list[Reserva]:
    res = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_entrada, fecha_salida, tipo, num, precio, servicios in lector:
            fechas = Fecha_Estancia(parse_fecha(fecha_entrada), parse_fecha(fecha_salida))
            res.append(Reserva(nombre, dni, fechas, tipo, int(num), float(precio), parse_servicios(servicios)))
    return res

def total_facturado(lista:list[Reserva], fecha_inicial:Optional[date]=None, fecha_final:Optional[date]=None)->float:
    '''
    Devuelve el total facturado por las reservas que se han realizado.
    Creando una lista vacía para guardar la respuesta de cada dato del fichero.
    Recorremos la lista de reservas y si la fecha inicial es None o la fecha de entrada es mayor o igual a la fecha inicial y la fecha final es None o la fecha de salida es menor o igual a la fecha final, añadimos a la lista el precio por noche multiplicado por el número de días de estancia.
    Devolvemos la suma de la lista.
    '''
    total = 0
    for i in lista:
        # Si la fecha inicial es None o la fecha de entrada es mayor o igual a la fecha inicial y la fecha final es None o la fecha de salida es menor o igual a la fecha final
        if (fecha_inicial == None or fecha_inicial <= i.fechas.fecha_entrada) \
            and (fecha_final == None or i.fechas.fecha_entrada <= fecha_final):
            total += i.precio_noche * (i.fechas.fecha_salida - i.fechas.fecha_entrada).days
    return total
    # Otra forma de hacerlo: (está mal hay que solucionarlo)
    #return sum([i.precio_noche * calculo_dias(i.fechas.fecha_entrada, i.fechas.fecha_salida) for i in lista if (fecha_inicial == None or i.fechas.fecha_entrada >= fecha_inicial) and (fecha_final == None or i.fechas.fecha_salida <= fecha_final)])

def servicios_adicionales(lista:list[Reserva])->list:
    '''
    Devuelve una lista con los servicios adicionales que se han contratado.
    Creando un conjunto vacío para guardar los servicios adicionales.
    Recorremos la lista de reservas y para cada reserva recorremos la lista de servicios adicionales.
    '''
    tupla = set()
    for i in lista:
        for j in i.servicios_adicionales:
            tupla.add(j)
    return sorted(list(tupla))

def reserva_mas_larga(lista:list[Reserva], n:int)->tuple[int, Reserva]:
    '''
    Devuelve una lista con las n reservas más largas.
    Creando una lista vacía para guardar el nombre, fecha de entrada, número de días de estancia y precio por noche de cada reserva.
    Ordenamos la lista de reservas por el número de días de estancia de forma descendente.
    Devolvemos las n primeras reservas.
    '''
    res = []
    for i in lista:
        res.append((i.nombre, i.fechas.fecha_entrada, (i.fechas.fecha_salida - i.fechas.fecha_entrada).days, i.precio_noche))

    maximos = sorted(res, key= lambda x:x[2], reverse=True)
    return maximos[:n]

def dni_por_tipo(lista:list[Reserva], servicio_adicional:str)->dict:
    '''
    Devuelve un diccionario con los DNI de las personas que han contratado un servicio adicional.
    Creando un diccionario vacío para guardar el tipo de habitación y el DNI de las personas que han contratado un servicio adicional.
    Recorremos la lista de reservas y si el servicio adicional está en la lista de servicios adicionales de la reserva, añadimos al diccionario el tipo de habitación y el DNI de la persona.
    Devolvemos el diccionario.
    '''
    diccionario = {}
    for i in lista:
        if servicio_adicional in i.servicios_adicionales:
            if i.tipo_habitación not in diccionario:
                diccionario[i.tipo_habitación] = []
            diccionario[i.tipo_habitación].append(i.dni)
    return diccionario

Tupla = NamedTuple('Tupla',
                   [('dni', str),
                   ('total_facturado', float)])

def cliente_mayor_facturacion(lista:list[Reserva], servicios:Optional[list]=None)->tuple[Tupla]:
    '''
    Devuelve el DNI del cliente que ha tenido una mayor facturación.
    Creando un diccionario vacío para guardar el DNI de las personas y el total facturado.
    Recorremos la lista de reservas y si los servicios son None o todos los servicios adicionales están en la lista de servicios adicionales de la reserva, añadimos al diccionario el DNI de la persona y el total facturado.
    Devolvemos el DNI de la persona con mayor facturación.
    '''
    diccionario = {}
    for i in lista:
        if servicios == None or all(servicio in i.servicios_adicionales for servicio in servicios):
            if i.dni not in diccionario:
                diccionario[i.dni] = 0
            diccionario[i.dni] += i.precio_noche * (i.fechas.fecha_salida - i.fechas.fecha_entrada).days
    dni, factura = max(diccionario.items(), key=lambda x:x[1])
    return Tupla(dni, factura)
