from datetime import *

print('hola')

fecha1_str = '2023-10-01'
fecha2_str = '2023-10-15'

fecha1 = datetime.strptime(fecha1_str, '%Y-%m-%d').date()
fecha2 = datetime.strptime(fecha2_str, '%Y-%m-%d').date()

print(f'Fecha 1: {fecha1}')
print(f'Fecha 2: {fecha2}')

mayor_fecha = max(fecha1, fecha2)
print(f'La mayor fecha es: {mayor_fecha}')