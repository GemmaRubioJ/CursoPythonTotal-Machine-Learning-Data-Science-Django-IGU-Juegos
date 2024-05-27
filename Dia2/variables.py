## Calculador de comisiones del 13% para empleados de ventas

name = input("Nombre : ")
sales = input("Cuánto has ganado este mes :")
ganancia = float(sales)*13/100

print(f"Los beneficios del empleado {name } este mes son de {round(ganancia,2) + float(sales)} €")