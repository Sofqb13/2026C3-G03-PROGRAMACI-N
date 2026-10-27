# Reto integrador: control de ingreso al Anfiteatro del CENAC
# Estudiante: Britany Sofia Quirós Barahona

capacidad_maxima = 700
ocupacion_actual = 0

grupos_aceptados = []
grupos_rechazados = []

print("=== CONTROL DE AFORO CENAC ===")
entrada = input("Ingrese la cantidad de personas del grupo (o fin): ")

while entrada != "fin":
    try:
        grupo = int(entrada)
        
        if grupo <= 0:
            print("Error: El número debe ser mayor a cero.")
        else:
            # Revisar si cabe en el aforo
            if ocupacion_actual + grupo <= capacidad_maxima:
                ocupacion_actual = ocupacion_actual + grupo
                grupos_aceptados.append(grupo)
                print("Grupo aceptado: ingresan", grupo, "personas.")
            else:
                grupos_rechazados.append(grupo)
                print("Grupo rechazado: no hay espacio para", grupo, "personas.")
            
            # Mostrar ocupación y espacios
            espacios_disponibles = capacidad_maxima - ocupacion_actual
            print("Ocupación actual:", ocupacion_actual)
            print("Espacios disponibles:", espacios_disponibles)
            print("")
            
    except ValueError:
        print("Error: Entrada inválida. Ingrese un número o escriba fin.")
    
    entrada = input("Ingrese la cantidad de personas del grupo (o fin): ")

# Calcular total admitido usando for
total_admitido = 0
for g in grupos_aceptados:
    total_admitido = total_admitido + g

espacios_finales = capacidad_maxima - total_admitido

# Reporte final
print("")
print("REPORTE FINAL")
print("Grupos aceptados:", len(grupos_aceptados))
print("Grupos rechazados:", len(grupos_rechazados))
print("Personas admitidas:", total_admitido)
print("Capacidad máxima:", capacidad_maxima)
print("Espacios disponibles:", espacios_finales)