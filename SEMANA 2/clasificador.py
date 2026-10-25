#Excelente | Bueno | Aprobado | Reprobado
#Analizar una nota y clasificar en una categoría
#Nota iguales o mayores a 90 Exc, Igual o mayor a 80 Bueno
#Igual o mayor a 70 Aprobado y menor a 70 Reprodado
nota = float(input("Por favor, ingrese su nota (0-100): "))
if nota <0 or nota >100:
    print("Error, debe ingresar un numero entre 0 y 100")
else:
 if nota >= 90:
    print("Excelente!")
 elif nota>=80:
    print("Muy bien!")
 elif nota>=70 and nota>= 0:
    print("Aprobado")
 elif nota<70:
    print("Reprobado")
 else:
    print("Nota invalida,debe ser entre 0-100")