#CON FOR PODEMOS... recorrer todos los caracteres de texto!
texto = "primer python"
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print(str(i) + ": " + letra)
print("Fin de programa")