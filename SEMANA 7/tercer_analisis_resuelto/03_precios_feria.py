"""Caso 3: comparación de precios de un producto en cinco ferias."""
producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

indice = 0
sobre_promedio = 0
while indice < len(precios):
    if precios[indice] > promedio:
        sobre_promedio += 1
    indice += 1

if rango >= 300:
    clasificacion = "Variación alta"
elif rango >= 150:
    clasificacion = "Variación moderada"
else:
    clasificacion = "Variación baja"

print("Producto:", producto)
print("Precio promedio: ₡", promedio)
print("Precio mínimo: ₡", minimo)
print("Precio máximo: ₡", maximo)
print("Rango de precios: ₡", rango)
print("Precios sobre el promedio:", sobre_promedio)
print("Clasificación:", clasificacion)
