from math import trunc
print("Programa día nacimiento")
print("Introduzca su día de nacimiento: ")
dia = int(input())
print("Introduzca su mes de nacimiento: ")
mes = int(input())
print("Introduzca su año de nacimiento: ")
ayo = int(input())
if (mes == 1):
    mes = 13
    ayo = ayo - 1 
elif (mes == 2):
    mes = 14
    ayo = ayo - 1
operacion1= trunc (((mes+1)*3)/5)
operacion2= trunc ((ayo/4))
operacion3=trunc((ayo/100))
operacion4=trunc(ayo/400)
operacion5=trunc(dia+(mes*2)+ayo+operacion1+operacion2-operacion3+operacion4+2)
operacion6= trunc(operacion5/7)
resultado= trunc(operacion5-(operacion6*7))
if (resultado == 0):
    print("SABADO")
elif (resultado == 1):
    print ("DOMINGO")
elif (resultado == 2):
    print ("LUNES")
elif (resultado == 3):
    print ("MARTES")
elif (resultado == 4):
    print ("MIERCOLES")
elif (resultado == 5):
    print ("JUEVES")
elif (resultado == 6):
    print ("VIERNES")
print("Fin de programa")