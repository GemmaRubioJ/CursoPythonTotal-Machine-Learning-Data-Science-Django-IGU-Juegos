import os
import time
from pathlib import Path
from os import system
import logging



print("BIENVENIDX AL RECETARIO DE LA YAYA")
ruta = Path("C:\\Recetas")
print(f"Las recetas están en {ruta}")

num_recetas = sum(1 for archivo in ruta.rglob('*.txt'))

# Muestra el número total de recetas
print(f'Número total de recetas: {num_recetas}')

def mostrar_menu():
    menu = """
    1 --- LEER Receta
    2 --- CREAR Receta
    3 --- CREAR Categoria
    4 --- ELIMINAR Receta
    5 --- ELIMINAR Categoria
    6 --- SALIR
    """
    print(menu)


def elegir_categoria() :
    carpetas = [carpeta.name for carpeta in ruta.iterdir() if carpeta.is_dir()]

    # Muestra las carpetas al usuario
    print("Categorías de Recetas Disponibles:")
    for i, carpeta in enumerate(carpetas, 1):
        print(f"{i}. {carpeta}")

    # Solicita al usuario que elija una categoría
    eleccion = int(input("Elige una categoría: "))
    carpeta_elegida = carpetas[eleccion - 1]
    print(f"Has seleccionado la categoría: {carpeta_elegida}")
    logging.info(f"Categoría seleccionada: {carpeta_elegida}")
    return carpeta_elegida

def elegir_receta(carpeta_elegida) :
    ruta_carpeta_elegida = ruta / carpeta_elegida
    print(f"Listando recetas en: {ruta_carpeta_elegida}")
    recetas = [receta for receta in ruta_carpeta_elegida.iterdir() if receta.is_file()]
    print(f"Recetas disponibles en {carpeta_elegida}:")
    if not recetas:
        print("No hay recetas disponibles en esta categoría.")
        return None
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta.name}")

    eleccion_receta = int(input("Elige un número para ver los detalles de la receta: "))
    receta_elegida = recetas[eleccion_receta - 1]
    print(f"Has seleccionado la receta: {receta_elegida.name}")
    return receta_elegida

def leer_receta(receta_elegida) :
    with open(receta_elegida, 'r') as file:
        print(file.read())
    logging.info(f"Leyendo receta: {receta_elegida}")

def crear_receta(carpeta_elegida) :
    ruta_carpeta_elegida = ruta / carpeta_elegida
    nombre = input("Introduce el nombre de tu receta : ")
    ruta_completa = ruta_carpeta_elegida / f"{nombre}.txt"
    ruta_carpeta_elegida.mkdir(parents=True, exist_ok=True)
    logging.info(f"Intentando crear archivo en: {ruta_completa}")
    try:
        with open(ruta_completa, "x") as file:
            contenido_receta = input("Escribe tu receta: ")
            file.write(contenido_receta)
            logging.info(f"Receta creada con éxito en {ruta_completa}.")
            print(f"Receta creada con éxito {ruta_completa}..")
    except FileExistsError:
        print("Error: Ya existe un archivo con ese nombre.")
    except Exception as e:
        print(f"Se produjo un error al crear la receta: {e}")

def crear_categoria() :
    categoria = input("Ingresa el nombre de la nuega categoría : ")
    try:
        os.makedirs(ruta / categoria)
        print("Categoria creada correctamente")
    except Exception as e:
        print(f"Se produjo un error al crear la Categoria: {e}")


def eliminar_receta(carpeta_elegida) :
    ruta_carpeta_elegida = ruta / carpeta_elegida
    recetas = [receta for receta in ruta_carpeta_elegida.iterdir() if receta.is_file()]
    if not recetas:
        print("No hay recetas disponibles para eliminar en esta categoría.")
        return
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta.name}")

    eleccion_receta = int(input("Elige un número de receta para eliminar: "))
    receta_a_eliminar = recetas[eleccion_receta - 1]
    confirmacion = input(f"Estás seguro de que deseas eliminar {receta_a_eliminar.name}? (s/n): ")
    if confirmacion.lower() == 's':
        receta_a_eliminar.unlink()
        print(f"Receta {receta_a_eliminar.name} eliminada con éxito.")
    else:
        print("Eliminación cancelada.")


def eliminar_categoria(carpeta_elegida) :
    ruta_carpeta_elegida = ruta / carpeta_elegida
    try:
        os.rmdir(ruta_carpeta_elegida)
    except Exception as e:
        print(f"Se produjo un error al borrar la Categoria: {e}")


def main():
    while True:
        system("cls")
        mostrar_menu()
        opcion = input("Elige una opción: ")
        match opcion:
            case '1':
                carpeta_elegida = elegir_categoria()
                receta_elegida = elegir_receta(carpeta_elegida)
                if receta_elegida is not None:
                    leer_receta(receta_elegida)
                    time.sleep(2)
            case '2':
                carpeta_elegida = elegir_categoria()
                crear_receta(carpeta_elegida)
            case '3':
                crear_categoria()
            case '4':
                carpeta_elegida = elegir_categoria()
                eliminar_receta(carpeta_elegida)
            case '5':
                carpeta_elegida = elegir_categoria()
                eliminar_categoria(carpeta_elegida)
            case '6':
                print("Saliendo del programa...")
                break  # Salir del bucle
            case _:
                print("Opción no válida, por favor intenta de nuevo.")
                time.sleep(2)

if __name__ == "__main__":
    main()

