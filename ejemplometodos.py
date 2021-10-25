#CODIGO DE FUNCIONES
def ejemploMetodo1():
    print("Soy el metodo 1...")
def ejemploMetodo2():
    print("Soy el método 2...")
    ejemploMetodo3()
def ejemploMetodo3():
    print("Soy el método 3...")

#CODIGO PRINCIPAL
print("Ejemplo de metodos")
print("Programa pincipal")
#si realizamos la llamada, dará un salto para leer el contido de método1
numero = 1
if (numero == 1):
    ejemploMetodo1
else:
    ejemploMetodo2
print("Fin de programa")

