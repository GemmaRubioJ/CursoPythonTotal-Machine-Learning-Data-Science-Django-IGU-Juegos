
def generador_turnos(prefijo):
    n = 1
    while True:
        yield f"{prefijo}-{n}"
        n += 1


def decorador_mensaje(func):
    def envoltura(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return f"Su turno es {resultado}. Aguarde y será atendido."
    return envoltura
