# Ejercicio 4: Validador de compra con descuento

try:
    nombre = input("Ingrese el nombre del cliente: ").strip()
    monto = float(input("Ingrese el monto de la compra: ₡"))
    respuesta = input("¿Es cliente frecuente? (si/no): ").strip().lower()

    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
    elif monto < 0:
        print("Error: el monto no puede ser negativo.")
    elif respuesta != "si" and respuesta != "sí" and respuesta != "no":
        print("Error: responda si o no.")
    else:
        if respuesta == "si" or respuesta == "sí":
            frecuente = True
        else:
            frecuente = False

        if frecuente and monto >= 50000:
            descuento_porcentaje = 10
        elif frecuente or monto >= 50000:
            descuento_porcentaje = 5
        else:
            descuento_porcentaje = 0

        descuento = monto * descuento_porcentaje / 100
        total_pagar = monto - descuento

        print(f"Cliente: {nombre.title()}")
        print(f"Descuento aplicado: {descuento_porcentaje}% (₡{descuento:.2f})")
        print(f"Total a pagar: ₡{total_pagar:.2f}")

except ValueError:
    print("Error: el monto debe ser un número válido.")
