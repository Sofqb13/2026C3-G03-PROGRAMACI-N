"""Caso 4: análisis de registros de soporte universitario."""
from incidencias import incidencias

total_minutos = 0
conteo_categorias = {"Acceso": 0, "Equipo": 0, "Red": 0}
pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = (None, 0)

for incidencia in incidencias:
    minutos = incidencia["minutos_atencion"]
    total_minutos += minutos
    categoria = incidencia["categoria"]
    conteo_categorias[categoria] += 1

    if not incidencia["resuelto"]:
        pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])
        if minutos >= 60:
            casos_urgentes.append((incidencia["id"], minutos))

    if minutos > caso_mas_largo[1]:
        caso_mas_largo = (incidencia["id"], minutos)

promedio_minutos = total_minutos / len(incidencias)
print("Total de casos:", len(incidencias))
print("Total de minutos:", total_minutos)
print("Promedio de minutos:", promedio_minutos)
print("Casos por categoría:", conteo_categorias)
print("Casos pendientes:", pendientes)
print("Provincias con pendientes:", sorted(provincias_pendientes))
print("Cantidad de provincias con pendientes:", len(provincias_pendientes))
print("Casos urgentes:", casos_urgentes)
print("Caso más largo:", caso_mas_largo)
print("¿Hay pendientes en San Jose?:", "San Jose" in provincias_pendientes)
