from random import randint


def generar_id() -> int:
    return int(''.join([str(randint(1, 100)) for i in range(4)]))

def validar_fecha(fecha_de_nacimiento: str) -> bool:
    valido = True
    fecha = fecha_de_nacimiento.split('/')
    if len(fecha) == 3:
        dia = int(fecha[0])
        mes = int(fecha[1])
        valido = True if dia <= 31 and dia > 0 and mes > 0 and mes <= 12 else False
    else:
        valido = False
    return valido

def cantidad_minima(cantidad_c_u: int, cantidad_c_o: int) -> int:
    return cantidad_c_u if cantidad_c_u <= cantidad_c_o else cantidad_c_o
