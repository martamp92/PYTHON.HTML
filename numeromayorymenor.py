print("App que te dice: numero mayor, numero menor y la suma de los tres")
print("Escriba el numero 1")
numero1 =  int(input())
print("Escriba el numero 2")
numero2 = int(input())
print("Escriba el numero 3")
numero3 = int(input())
mayor = 0
menor = 0
suma = 0
intermedio = 0
if ((numero1 >= numero2) and (numero1 >= numero3)):
    mayor = numero1
elif ((numero2 >= numero1) and (numero1 >= numero3)):
   mayor = numero2
else:
    menor = numero3
if ((numero1 <= numero2) and (numero1 <= numero3)):
    menor = numero1
elif ((numero2 <= numero1) and (numero2 <= numero3)):
    menor = numero2
else:
    menor = numero3

suma = numero1 + numero2 + numero3
intermedio = suma - mayor - menor
print("Numero mayor: " + str(mayor))
print("Numero menor: " + str(menor))
print("Suma: " + str(suma))
print("Intermedio: " + str(intermedio))