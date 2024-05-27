##un código que le permite a
##una persona realizar operaciones en su cuenta bancaria

import random


class Persona :
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido,  numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = int(balance)

    def __str__(self):
        return f"El cliente {self.nombre} {self.apellido} con cuenta {self.numero_cuenta} tiene {self.balance} €"

    def depositar(self, cantidad):
        self.balance += int(cantidad)
        print("Cantidad depositada")

    def retirar(self, cantidad):
        if self.balance >= int(cantidad):
            self.balance -= int(cantidad)
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


def mostrar_menu():
    menu = """
    1 . Depositar
    2 . Retirar 
    3 . Salir """
    print(menu)


def depositar(cliente):
    cantidad = input("Cuanto quiere ingresar : ")
    cliente.depositar(cantidad)
    print(str(cliente))
    print("********************************")


def retirar(cliente) :
    cantidad = input("Cuanto quiere retirar : ")
    cliente.retirar(cantidad)
    print(str(cliente))
    print("********************************")


def crear_cliente() :
    nombre = input("Introduzca su nombre : ")
    apellido = input("Introduzca su apellido : ")
    numero_cuenta = random.randint(1000000000, 9999999999)
    balance = input("Introduzca la cantidad con la que quiere abrir su cuenta : ")
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    print(str(cliente))
    print("********************************")
    return cliente


def main():
    print("BIENVENIDX A SU BANCA ONLINE")
    cliente = crear_cliente()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        match opcion:
            case '1':
                depositar(cliente)
            case '2':
                retirar(cliente)
            case '3':
                print("Saliendo ... Adiós!")
                break


if __name__ == "__main__":
    main()

