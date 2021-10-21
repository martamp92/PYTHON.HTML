print("Evaluar número while")
respuesta = "s"
while (respuesta == "s"):
    print("Introduzca un número")
    numero = int(input())
    if (numero > 0):
        print("POSITIVO")
    elif (numero < 0):
        print("NEGATIVO")
    else:
        print("ZERO")
    print("Desea continuar? (s/n)")
    respuesta = input()
    
