#MOSTRAR LOS NUMEROS PAR:
print("Número inicial: ")
inicio = int(input())
print("Número final: ")
fin = int(input())
for i in range (inicio, fin + 1): 
    if (i % 2 == 0):
        print(i)
