## software de sistema de turnos para una farmacia

import numeros

# Generadores para cada área
turnos_farmacia = numeros.generador_turnos("F")
turnos_perfumeria = numeros.generador_turnos("P")
turnos_cosmetica = numeros.generador_turnos("C")

@numeros.decorador_mensaje
def obtener_turno(generador):
    return next(generador)


def menu():
    while True:
        print("\nÁreas de atención:")
        print("1. Farmacia")
        print("2. Perfumería")
        print("3. Cosméticos")
        print("4. Salir")

        opcion = input("Seleccione el área a la que desea dirigirse o Salir: ")

        if opcion == '1':
            print(obtener_turno(turnos_farmacia))
        elif opcion == '2':
            print(obtener_turno(turnos_perfumeria))
        elif opcion == '3':
            print(obtener_turno(turnos_cosmetica))
        elif opcion == '4':
            print("Gracias por visitarnos. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    print("Bienvenido a la farmacia")
    menu()