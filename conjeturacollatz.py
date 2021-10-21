print("Introduca su número: ")
numero = int(input())
#Mientras que l número sea distinto de 1...
while (numero != 1):
    if (numero % 2 ==0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 +1
    print(numero)
print("Fin de programa")