print("Calculo de salario del trabajador por horas")
print("Numero de horas trabajadas: ")
horastrabajadas = int(input())
print("Precio por hora: ")
preciohora = int(input())
print("Kilometros: ")
horasextra= 0
salario= 0 
salarioextra= 0
dieta= ""
retencion= ""
salariofinal = 0
kilometros = int(input())
if (horastrabajadas > 36):
    horasextra = horastrabajadas - 36
    salario = preciohora * 36
    salarioextra = horasextra * (preciohora + 2)
else:
    horasextra= 0 
    salario = preciohora * horastrabajadas
    salarioextra = 0
if (kilometros < 100):
    print("DIETAS LOCALES")
elif ((kilometros >= 100) and (kilometros <= 500)):
    print("DIETAS NACIONALES")
else:
    print ("DIETAS INTERNACIONALES")

salariofinal = salario + salarioextra
if (salariofinal <=250):
    print("NO TIENE RETENCIÓN")
elif ((salariofinal >= 251) and (salariofinal <= 800)):
    print("RETENCIÓN DEL 20%")
else:
    print("RETENCIÓN DEL 40%")
print("Salario base: " + str(salario))
print("Salario extra: " + str(salarioextra))
print("Salario final: " + str(salariofinal))
print("Fin de programa")
