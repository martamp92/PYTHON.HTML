#Le pedimos al usuario que introduzca un número y si mete una letra le decimos que no es número...
print("Introduzca un número: ")
aux = input()
if (aux.isdigit()):
    print("Es un numero")
else:
    print("No es un numero")
print("Fin de programa")