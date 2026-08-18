LECTURAS_MV_POSITIVAS = [253.7, 550.0, 812.3, 190.5, 402.1, 905.6, 380.0, 811.9]
LECTURAS_MV_NEGATIVAS = [-150.0, -180.5, -95.2, -210.8, -175.3]

MV_POR_GRADO = 10
UMBRAL_CRITICO_C = 80  # Está en Celsius.


def pedir_lista():

    print("¿Qué lista desea utilizar?")
    print("1. Lista de lecturas positivas")
    print("2. Lista de lecturas negativas")

    decision = input("Ingrese el número de la opción deseada: ")

    if decision == "1":
        return LECTURAS_MV_POSITIVAS

    elif decision == "2":
        return LECTURAS_MV_NEGATIVAS

    else:
        print("\nOpción inválida. Por favor, ingrese 1 o 2.\n")
        return pedir_lista()


def mv_a_celsius(lectura_mv):

    lista_a_celsius = []

    for elemento in lectura_mv:
        temp_c = elemento / MV_POR_GRADO
        lista_a_celsius.append(temp_c)

    return lista_a_celsius


def analizar_lecturas(lecturas_mv):

    # Primero convertimos las lecturas de mV a Celsius
    temperaturas_c = mv_a_celsius(lecturas_mv)

    suma = 0
    maximo = temperaturas_c[0]
    criticas = []

    for elemento in temperaturas_c:

        # Suma
        suma += elemento

        # Máximo
        if elemento > maximo:
            maximo = elemento

        # Lecturas críticas
        if elemento > UMBRAL_CRITICO_C:
            criticas.append(elemento)

    porcentaje = len(criticas) / len(temperaturas_c) * 100

    return suma, maximo, criticas, porcentaje


def mostrar_reporte(reporte):

    suma, maximo, criticas, porcentaje = reporte

    print(f"\nSuma de lecturas: {suma:.2f} °C")
    print(f"Promedio de lecturas: {suma / len(criticas):.2f} °C")
    print(f"Máximo de lecturas: {maximo:.2f} °C")
    print(f"Lecturas críticas: {criticas}")
    print(f"Porcentaje de lecturas críticas: {porcentaje:.2f}%")


while True:

    lecturas_mv = pedir_lista()

    temperaturas_c = mv_a_celsius(lecturas_mv)

    resultados = analizar_lecturas(lecturas_mv)

    print(analizar_lecturas(LECTURAS_MV_POSITIVAS))

    mostrar_reporte(resultados)

    continuar = input("\n¿Desea realizar otra operación? (sí/no): ").strip().lower()

    if continuar not in ("sí", "si", "yes"):
        break