
#programar el Sistema de Aprobación de Visas
#Entrada
print ("|||BIENVENIDO A NUESTRO FORMULARIO DE APROBACIÓN DE VISAS|||")
print ("")
print("Por favor, ingrese los datos personales que se le solicitan a continuación:")
print ("")
print ("En caso de no tener respuesta por favor click en tecla enter.")
print ("")
print ("Por favor, recuerde siempre ingresar sus respuestas con minusculas y mayusculas según corresponda.")
print ("")
monto = int(input("Por favor, ingrese el monto disponible en su cuenta bancaria ($)"))
antecedentes = input("¿Tiene antecedentes penales? (Si/No): ")
profesion = input("Por favor, ingrese su profesión: ")
print ("")


#CASO 1 (Visa Dorada):
if (monto >=50000 and antecedentes == "No" or profesion == "Diplomatico"):
    print("APROBADO: VISA DORADA.")
    
#Caso 2 CASO 2 (Visa Estándar):
elif (monto >= 20000 and antecedentes == "No" or profesion == ""):
    print("APROBADO: VISA ESTANDAR.")

# CASO 3 (Revisión Especial):
elif(monto < 20000 and profesion == "Estudiante" or profesion == "Jubilado"):
    print("PENDIENTE:Requiere entrevista.")

#CASO 4 (Rechazo):
else:
    print ("Su VISA ha sido denegada.")

print ("")
print ("|||GRACIAS POR USAR NUESTRO SISTEMA.|||")