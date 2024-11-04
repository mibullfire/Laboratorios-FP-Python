from reservas import *
from colorama import Fore

def test_lee_fichero(fichero:str)->None:
    lista = lee_reservas(fichero)
    print(Fore.BLUE + '\ntest_lee_fichero')
    print(f'Se han leído {len(lista)} datos')
    print(f'Primer elemento {lista[0]}')

def test_total_facturado(lista:list[Reserva], fecha1=None, fecha2=None)->None:
    print(Fore.GREEN + '\ntest_total_facturado')
    print(f'Total facturado: {total_facturado(lista, fecha_inicial=fecha1, fecha_final=fecha2)}')

def test_servicios_adicionales(lista:list[Reserva])->None:
    print(Fore.YELLOW + '\ntest_servicios_adicionales')
    print(servicios_adicionales(lista))

def test_reserva_mas_larga(lista:list[Reserva], n:int)->None:
    print(Fore.MAGENTA + '\ntest_reserva_mas_larga')
    maximos = reserva_mas_larga(lista, n)
    for i in range(n):
        print(f'{i+1} --> {maximos[i]}')

def test_dni_por_tipo(lista:list[Reserva], tipo:str)->None:
    print(Fore.CYAN + '\ntest_dni_por_tipo')
    print(dni_por_tipo(lista, tipo))

def test_cliente_mayor_facturacion(lista:list[Reserva], servicios:Optional[list]=None)->None:
    print(Fore.RED + '\ntest_cliente_mayor_facturacion')
    print(cliente_mayor_facturacion(lista, servicios))

def main():
    fichero = './data/reservas.csv'
    test_lee_fichero(fichero)
    lista = lee_reservas(fichero)
    test_total_facturado(lista)
    test_total_facturado(lista, fecha1=parse_fecha('2022-02-01'), fecha2=parse_fecha('2022-02-28'))
    test_total_facturado(lista, fecha1=date(2022, 2, 1))
    test_total_facturado(lista, fecha2=date(2022, 2, 28)) 
    test_servicios_adicionales(lista)
    test_reserva_mas_larga(lista, 3)
    test_dni_por_tipo(lista, 'Piscina')
    test_cliente_mayor_facturacion(lista)
    test_cliente_mayor_facturacion(lista, ['Parking'])
    test_cliente_mayor_facturacion(lista, ['Parking', 'Spa'])

if __name__ == '__main__':
    main()