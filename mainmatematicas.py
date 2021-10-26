import metodosexternosmatematicas
print("Programa de matemáticas")
print("Introduzca número1")
numero1 = int(input())
print("Introduzca número2")
numero2 = int(input())
opcion = -1
while (opcion != 0):
    metodosexternosmatematicas.mostrarMenu()
    opcion = int(input())
    if opcion == 1:
        resultado = metodosexternosmatematicas.sumarNumero(numero1, numero2)
        print("La suma es: " +str(resultado))
    elif opcion ==2:
        resultado = metodosexternosmatematicas.restarNumeros(numero1, numero2)
        print("La resta es: " + str(resultado))
    elif opcion == 3:
        resultado = metodosexternosmatematicas.multiplicarNumeros(numero1, numero2)
        print("El resultado es: " + str(resultado))
    elif opcion == 4:
        resultado = metodosexternosmatematicas.dividirNumeros(numero1, numero2)
        print("El restulado es: " + str(resultado))
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción incorrecta")
    print("¿Desea introducir otro números? (s/n)")
    respuesta = input()
    if (respuesta == "s"):
        print("Introduzca número1")
        numero1 = int(input())
        print("Introduzca número2")
        numero2 = int(input())
    else:
        break
print("Fin de programa")