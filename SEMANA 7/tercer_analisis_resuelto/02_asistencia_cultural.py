"""Caso 2: asistencia por bloques."""
asistencias = [120, 180, 210, 250, 230]
capacidad = 300

total = 0
bloques_superiores = 0
for asistentes in asistencias:
    total += asistentes
    if asistentes > capacidad * 0.70:
        bloques_superiores += 1

promedio = total / len(asistencias)
porcentaje_ocupacion = promedio / capacidad * 100
if porcentaje_ocupacion >= 80:
    estado = "Ocupación alta"
elif porcentaje_ocupacion >= 50:
    estado = "Ocupación media"
else:
    estado = "Ocupación baja"

print("Asistencia total:", total)
print("Promedio de asistencia:", promedio)
print("Porcentaje de ocupación:", porcentaje_ocupacion, "%")
print("Bloques que superan el 70 %:", bloques_superiores)
print("Estado:", estado)
