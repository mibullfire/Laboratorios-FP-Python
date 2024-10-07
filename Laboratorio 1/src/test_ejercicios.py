from ejercicios import *

def test_calculo_imc(peso:float, estatura:float)->None:
  imc = calcula_imc(peso, estatura)
  print(f"Para un peso de {peso} y estatura {estatura} el IMC es: {imc}")

def test_calcula_estado_nutricional(peso:float, estatura:float)->None:
  respuesta = calcula_estado_nutricional(peso, estatura)
  print(f"Para un peso de {peso} y estatura {estatura} el IMC es: {respuesta}")

def test_trata_estados_nutriconales()->None:
  datos = [
    Datos_nutricionales(60.0, 1.6),
    Datos_nutricionales(75.4, 1.75),
    Datos_nutricionales(87.9, 1.69),
    Datos_nutricionales(45.1, 1.65),
    Datos_nutricionales(100.8, 1.80)
    ]
  datos_nutric = trata_estados_nutricionales(datos)
  for i in range(len(datos)):
    print(f'Para {datos[i]} el IMC es {datos_nutric[i][0]} y el estado nutricional es: {datos_nutric[i][1]}')

def test_producto_escalar(vector1:list, vector2:list)->None:
  res = producto_escalar(vector1, vector2)
  print(f'{vector1} x {vector2} es: {res}')

def test_calcula_promedio_edades_sexo(Edad, sexo)->None:
  promedio = calcula_promedio_edades_sexo(Edad, sexo)
  print(f'El promedio del sexo {sexo} es: {promedio}')

#El programa empieza a ejecutarse por aquí
if __name__=='__main__':
  test_calculo_imc(82, 1.89)
  test_calcula_estado_nutricional(82, 1.89)
  test_trata_estados_nutriconales() # En este caso los datos están dentro de la funciçon test.
  test_producto_escalar([2, 3, 1], [3, 4, 7])
  edades = [Edad(23,'M'),
    Edad(30,'M'),
    Edad(56,'H'),
    Edad(18,'H'),
    Edad(34,'M'),
    Edad(7,'M'),
    Edad(95,'H'),
    Edad(37,'M'),
    Edad(36,'H')]
  test_calcula_promedio_edades_sexo(edades, 'M')
  test_calcula_promedio_edades_sexo(edades, 'H')
  test_calcula_promedio_edades_sexo(edades, 'J')