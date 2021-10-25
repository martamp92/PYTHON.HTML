print("Introduce un número ISBN")
isbn = input()
#Capturamos la longitud 
longitud = len(isbn)
#Comprobamos que todos sean números
suma = 0
if (isbn.isdigit() == False):
    print("Debe introducir solo números")
elif (longitud != 10):
    print("Debe tener 10 carácteres")
else:
    #Aquí ya empieza el código...
    for i in range(longitud):
        #Capturamos cada letra
        letra = isbn[i]
        #Convertimos la letra a número
        numero = int(letra)
        #Ncesitamos la posicion real de cada caracter
        posición= i + 1
        #Ahora multiplicamos el número por la posición
        multi = numero * posición
        #Necesitamos una variable "suma" para guardar cada resultado de la multiplación... 
        #La vamos a declarar fuera del "bucle"
        suma = suma + multi
if (suma % 11 == 0):
    print("ISBN correcto")
else:
    print("ISBN incorrecto")
print("Fin del programa")