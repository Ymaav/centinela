import unicodedata

MV_POR_GRADO = 10
UMBRAL_ADVERTENCIA_C = 40
UMBRAL_CRITICO_C = 80
RESPUESTAS = ("sí", "si", "yes")

while True:
    lectura_mv = float(input("Lectura del sensor en mv: "))
    celsius_resultado = lectura_mv / MV_POR_GRADO
    if celsius_resultado < UMBRAL_ADVERTENCIA_C:
        estado = "Normal"

    elif UMBRAL_ADVERTENCIA_C <= celsius_resultado <= UMBRAL_CRITICO_C:
        estado = "Advertencia"

    else:
        estado = "Critico"

    print(f"Celsius: {celsius_resultado:.2f}°C\nEstado: {estado}")

    continuar = unicodedata.normalize(
        "NFC", input("¿Quiere continuar el programa? ").strip().lower()
    )
    if continuar not in RESPUESTAS:
        print("Hasta luego!")
        break
