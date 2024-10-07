from typing import NamedTuple, List, Tuple

def calcula_imc(peso:float, estatura:float)->None:
    return peso/estatura**2

def calcula_estado_nutricional(peso:float, estatura:float)->None:
    imc = calcula_imc(peso, estatura)
    if imc < 18.5:
        respuesta = "Bajo Peso"
    elif 18.5 <= imc < 25:
        respuesta = "Normal"
    elif 25 <= imc < 30:
        respuesta = "Sobrepeso"
    else:
        respuesta = "Obesidad"
    return respuesta

# Es importante definir las variables haciendo un typing, y haciendo uso de las namedtuple.
Datos_nutricionales = NamedTuple("Datos_nutricionales", [('peso',float), ('estatura',float)])
def trata_estados_nutricionales(datos:List[Datos_nutricionales])->None:
    res = []
    for Datos_nutricionales in datos:
        imc = calcula_imc(Datos_nutricionales.peso, Datos_nutricionales.estatura)
        estado = calcula_estado_nutricional(Datos_nutricionales.peso, Datos_nutricionales.estatura)
        tupla = (imc, estado)
        res.append(tupla)
    if len(res) > 0:
        return res

def producto_escalar(vector1:list, vector2:list)->None:
    if len(vector1) == len(vector2):
        n:int = 0
        respuesta:list = []
        while n < len(vector1):
            respuesta.append(vector1[n]*vector2[n])
            n=n+1
        return sum(respuesta)

Edad = NamedTuple('Edad', [('edad', int), ('sexo', str)])
def calcula_promedio_edades_sexo(edades:list[Edad], sexo:str)->None:
    res:list = []
    for elemento in edades:
        if elemento.sexo == sexo:
            res.append(elemento.edad)
    if len(res) > 0:
        return sum(res)/len(res)