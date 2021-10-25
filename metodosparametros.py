#Declaracion de metodo
def saludo(nombre):
    print("Bienvenido, " + nombre)
def despedida(nombre, dia):
    print("Adiós " + dia + ", " + nombre)

#PROGRAMA PRINCIPAL
print("Ejemplo métodos con parametros")
print("Tu nombre")
nombre = input()
#En la llamada, enviamos un valor
saludo(nombre)
print("¿Qué día es hoy de la semana?")
dia = input()
#ejemplo de un metodo que me devuelve un valor. upper(). 
#me va a devolver la palabra jueves en MAYUSC.
dia = dia.upper()
valor = despedida(dia, nombre)
#Por aquí realizamos una acción...
print("Fin de programa")
