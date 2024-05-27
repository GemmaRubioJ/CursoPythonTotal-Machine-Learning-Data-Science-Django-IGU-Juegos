##Analizador de Datos. El usuario ingresa un texto y 3 letras a su elección y  el programa hace 5 análisis.
##Cuántas veces aparece cada una de las letras
##Cuántas palabras hay en el texto
##Primera  y última letra del texto
##Texto invertido
##Buscar la palabra "Python" en el texto


texto = input("Introduzca su texto aquí : ").lower()
letras = []
letras.append(input("Introduzca la 1ª letra : "))
letras.append(input("Introduzca la 2ª letra : "))
letras.append(input("Introduzca la 3ª letra : "))

##primera comprobación

contador = texto.count(letras[0])
contador += texto.count(letras[1])
contador += texto.count(letras[2])
print(f"Tus letras {letras[0]} , {letras[1]} , {letras[2]} aparecen un total de {contador} veces")
print("\n")

##segunda comprobación
lista_texto = texto.split()
print(f"Tu texto tiene un total de {len(lista_texto)} palabras")
print("\n")

##tercera comprobacion
print(f"La primera palabra es {lista_texto[0]} y la última es {lista_texto[-1]} ")
print("\n")

##cuarta comprobacion
print(f"El texto invertido es : {texto[::-1]} ")
print("\n")

##quinta comprobacion
control = "python" in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python'  {dic[control]} se encuentra en el texto")







