"""Diagnóstico semanal: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]

meta_centro = 640000
meta_norte = 700000

# Indicadores de la tienda Centro
total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)
menor_centro = min(ventas_centro)
mayor_centro = max(ventas_centro)
promedio_centro = total_centro / cantidad_centro
rango_centro = mayor_centro - menor_centro
diferencia_centro = total_centro - meta_centro
porcentaje_centro = total_centro * 100 / meta_centro

# Indicadores de la tienda Norte
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
menor_norte = min(ventas_norte)
mayor_norte = max(ventas_norte)
promedio_norte = total_norte / cantidad_norte
rango_norte = mayor_norte - menor_norte
diferencia_norte = total_norte - meta_norte
porcentaje_norte = total_norte * 100 / meta_norte

# Estado de cumplimiento de Centro
if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro == meta_centro:
    estado_centro = "meta alcanzada exactamente"
else:
    estado_centro = "meta NO alcanzada"

# Estado de cumplimiento de Norte
if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte = "meta alcanzada exactamente"
else:
    estado_norte = "meta NO alcanzada"

# Comparación de los totales
if total_centro > total_norte:
    tienda_gano = "Tienda Centro"
elif total_norte > total_centro:
    tienda_gano = "Tienda del Norte"
else:
    tienda_gano = "Ambas tiendas tienen el mismo total"

# Comparación de los rangos
if rango_centro < rango_norte:
    tienda_mas_estable = "Tienda Centro"
elif rango_norte < rango_centro:
    tienda_mas_estable = "Tienda del Norte"
else:
    tienda_mas_estable = "Ambas tiendas tienen el mismo rango"

# Reporte final
print("COMPARACION SEMANAL DE TIENDAS")
print("-" * 100)
print(
    f"Centro | total ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} "
    f"| cumplimiento {porcentaje_centro:.0f}%"
)
print(f"Centro logro: {estado_centro}")
print(
    f"Norte | total ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} "
    f"| cumplimiento {porcentaje_norte:.0f}%"
)
print(f"Norte logro: {estado_norte}")
print()
print(f"Tienda con mayor ventas: {tienda_gano}")
print("-" * 100)

# Tres conclusiones
print("CONCLUSIONES")
print(f"1. La tienda Centro vendió ₡{total_centro:,.2f} y {estado_centro}.")
print(f"2. La tienda Norte vendió ₡{total_norte:,.2f} y {estado_norte}.")
print(f"3. La tienda con menor variación semanal fue: {tienda_mas_estable}.")
