"""Microreto: el portero del café."""

energia = int(input("Cuanta enería tienes de 0-100: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == "si"

mensaje = "Completa las reglas del portero."

if energia < 30 and not (trae_cafe):
    print("No puede pasar!")
elif energia >= 30 or trae_cafe :
    print("Bienvenido, puede pasar!")
else:
    mensaje= "Portero confundido!, revisar las respuestas."



