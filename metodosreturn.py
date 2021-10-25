def convertirTexto(texto):
    #Devolvemos el texto en mayúsculas
    print("Estoy en el  metodo!!")
    return texto.upper()
def sumarNumeros(num1, num2):
    suma= num1 + num2
    return suma
#programa principal:
print("Metodos return")
#Aquí enviamos un texto en minúsculas
#Debemos tener una variable para almacenar el valor devuelto para el método
valor = convertirTexto("soy un texto en minúsculas")
print(valor)
print("Introduzca un número1")
numero1= int(input())
print("Introduzca un número2")
numero2= int(input())
resultado = sumarNumeros (numero1, numero2)
print("La suma es: " + str(resultado))
print("Fin de programa")
