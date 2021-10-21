print("Ejemplo con métodos de string")
texto = "primero python"
#Vamos a escribir lo métodos y vemos qué devuelve...
print("Mayusculas: " + texto.upper ())
print("Replace o-@: " + texto.replace("o", "@"))
print("Primera letra: " + texto[0])
print("longitud texto: " + str(len(texto)))
print("Buscar letra P: " + str(texto.find("P")))
print("Buscar letra p: " + str(texto.find("p")))
#Busca a partir de la p (no inclusiva):
print("Buscar siguientes letra p: " + str(texto.find("p", 1)))
#Buscamos letra p a partir de la pimera letra p:
posicion = texto.find("p")
#Buscamos letra p desde la posición inicial:
print("Buscar siguiente letra p: " + str(texto.find("p", posicion + 1 )))
#Busca desde el final la letra:
print("Letra p con RFIND: " + str(texto.rfind("p")))
print("Texto finalizando con n: " + str(texto.startswith("A")))
print("Texto números: " + str(texto.isdigit()))
#Isdigit: Nos dice si son números...
print("Texto letras: " + str(texto.isalpha()))
#Isalpha: Nos dice si son letras...
print("Texto iniciando con A: " + str(texto.startswith("A")))
print("Texto finalizando con n: " + str(texto.endswith("n")))
#Desde la posición dos en adelante:
#Subcadena/Vamos a ver Slicing: 
subcadena1 = texto[2:]
#Lo que indicamos en la subacadena 1 es 
# que queresmos desde la posicón 2 en adelante, es decir, desdes "imero Python"
print("Posición 2 en adelante: " + subcadena1)
subcadena2 = texto[2:5]
#Nos devolvería: "imero"
print="Posición 2 a la 5: " + subcadena2


