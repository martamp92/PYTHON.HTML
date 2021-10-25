print("Ejemplo sumando números de String")
print ("Introduzca un texto de SOLO NUMEROS")
textonumeros = input()
#Necesitamos acceder caracter a caracter a cada numero del String
#Hay que recorrer toda la cadena de String para acceder a cada caracter
longitud = len(textonumeros)
suma = 0
#La variable la tenemos que declarar fuera del bucle! si no en algunos lenguajes no podriamos u
#usarla como en la línea 17
for i in range(longitud):
    #Recuperamos cada caracter
    caracter = textonumeros[i] 
    #Convertimos cada caracter a int
    numero = int(caracter)
    suma = suma + numero 
    #La suma solamente queremos dibujarla una ves. Por lo que la dibujamos fuera del bucle.
print ("La suma es " + str(suma))
print("Fin de programa")


