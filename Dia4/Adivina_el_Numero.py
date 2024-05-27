##el programa le va a preguntar al usuario su nombre, y luego le va a decir
##algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
##para adivinar cuál crees que es el número”.
from random import *

nombre = input("Cuál es tu nombre :")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo 8 intentos para adivinar cuál crees que es el número")
num = randint(1,101)

for n in range(8):
    guess = int(input("Tu guess  : "))
    match guess:
        case _ if guess < num :
            print("El número es mayor")
        case _ if guess > num :
            print("El número es menor")
        case _ if guess == num :
            print(f"GANASTE! EL NÚMERO ES {num}")
        case _:
            print("Juega otra vez")




