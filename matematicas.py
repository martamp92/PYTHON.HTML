print("Ejemplo matematicas")
numero1 = 8
numero2 = 18
suma = numero1 + numero2
multiplicacion = numero1*numero2
#Para dividir, el tipo de dato es un FLOAT. 
division = numero1 / numero2
cociente = numero1 // numero2
resto = numero1 % numero2
print("Resto: ", resto)
print("Cociente: ", cociente)
print("Suma: ", suma) 
print("Multiplicación: ", multiplicacion)
print("División: ", division)

texto1 = "hola"
texto2 = " mundo"
print(texto1 + texto2)

#Para unir texto y numero (concatenar) no podemos sumar texto y letra, tenemos que usar "funciones de conversión"
#str(variable): convierte una variable en String
#float(variable): convierte una variable en decimal
#int(variable): convierte una variable en entero
print("suma: " + str (suma))