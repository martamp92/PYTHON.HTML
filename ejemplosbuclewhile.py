print("Ejemplo bucles")
print("While: ")
contador = 0 
#NECESITAMOS PRIMERO UNA VARIABLE
while (contador <= 5):
    #SIEMPRE LE DEBEMOS PONER UNA CONDICIÓN:
    contador +=1
    if (contador == 3):
        break
    contador +=1
    print("Contador: " + str(contador))
    #break: si el bucle llega a 3 que salga! 
    # Si pongo "continue" (en vez de break, vuelve el inicio) Con continue tengo que poner la condición arriba...
       