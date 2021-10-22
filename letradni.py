from math import trunc
#DEBEMOS USAR LA LIBRERIA MATH PARA USAR ENTERO (TRUNCAR)
print("Programa para validar DNI")
print("Introduzca su número de dni")
aux = input()
if (aux.isdigit() == False):
    print("Debe introducir NUMEROS SOLAMENTE")
else:
    numerodni = int(aux)
    resultado = (numerodni - (trunc(numerodni / 23) * 23))
    print(resultado)
    tabladni = "TRWAGMYFPDXBNJZSQVHLCKET"
    letra = tabladni[resultado]
    print("Su letra es: " + letra)
 