print("Ejemplo Tabla de multiplicar")
print("Escriba un número: ")
numero = int(input())
for i in range (1, 11):
    resultado = numero * i 
    print(str(numero) + " * " + str(i) + " = " + str(resultado))
