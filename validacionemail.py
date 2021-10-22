print("Validación de email")
print("Introduzca su mail: ")
email = input()
if (email.find("@") == -1):
    print("Email sin @")
elif (email.find(".") == -1):
    print("Email sin .")
    #Hasta aqúi quiere decir que el email tiene que tener @ y . 
elif (email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith(".")):
    print("Email finaliza o empieza con ./@")
    #Ahora le estamos diciendo que su email esá mal porque finaliza o empieza con . o @
elif (email.find ("@") != email.rfind("@")):
    print("Email con mas de una @")
    #Que el email tiene 2 @
    #Lo que lo estamos diciendo es que si no son iguales la posiciones es que hay más de una..
elif (email.find("@") > email.rfind(".")):
    print("El punto no puede estar antes de la @")
else:
    ultimopunto = email.rfind(".")
    dominio = email[ultimopunto+1:]
    longitud = len(dominio)
    if (longitud >= 2 and longitud <=4):
        print("Email correcto!!!")
    else:
        print("El dominio debe ser de 2 a 4 letras")



