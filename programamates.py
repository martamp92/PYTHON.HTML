def mostrarMenu():
    print("0.-Salir")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Dividir")
    print("4.-Multiplicar")
    print("Selecciones una de las opciones: ")
def sumarNumero(num1, num2):
    suma = num1 + num2
    return suma
def restarNumeros(num1, num2):
    resta = num1 - num2
    return resta
def dividirNumeros(num1, num2):
    division = num1 / num2
    return division
def multiplicarNumeros(num1, num2):
    multiplicar = num1 * num2
    return multiplicar
    
#Programa principal
print("Programa de matemáticas")
print("Introduzca número1")
numero1 = int(input())
print("Introduzca número2")
numero2 = int(input())
mostrarMenu()
opcion = int(input())
if opcion == 1:
    resultado = sumarNumero(numero1, numero2)
    print("La suma es: " +str(resultado))
elif opcion ==2:
    resultado = restarNumeros(numero1, numero2)
    print("La resta es: " + str(resultado))
elif opcion == 3:
    resultado = multiplicarNumeros(numero1, numero2)
    print("El resultado es: " + str(resultado))
elif opcion == 4:
    resultado = dividirNumeros(numero1, numero2)
    print("El restulado es: " + str(resultado))
else:
    print("Fin de programa")


