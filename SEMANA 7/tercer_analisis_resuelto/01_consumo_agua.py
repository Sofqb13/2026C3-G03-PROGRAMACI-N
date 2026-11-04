"""Caso 1: cambio del consumo diario de agua."""
consumos_litros = [120, 115, 108, 102, 96]

total = sum(consumos_litros)
promedio = total / len(consumos_litros)
ahorro = consumos_litros[0] - consumos_litros[-1]
reduccion = (ahorro / consumos_litros[0]) * 100 if consumos_litros[0] != 0 else 0

if reduccion >= 15:
    clasificacion = "Reducción alta"
elif reduccion > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"

print("Consumo total:", total, "L")
print("Promedio diario:", promedio, "L")
print("Litros ahorrados:", ahorro, "L")
print("Porcentaje de reducción:", reduccion, "%")
print("Clasificación:", clasificacion)
