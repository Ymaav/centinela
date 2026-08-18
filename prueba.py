LECTURAS_MV_POSITIVAS = [253.7, 550.0, 812.3, 190.5, 402.1, 905.6, 380.0, 811.9]
LECTURAS_MV_NEGATIVAS = [-150.0, -180.5, -95.2, -210.8, -175.3]

MV_POR_GRADO = 10
UMBRAL_CRITICO_C = 80

def quelista_desea():
    print("¿Qué lista desea utilizar?")
    print("1. Lista de lecturas positivas")
    print("2. Lista de lecturas negativas")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        return LECTURAS_MV_POSITIVAS
    elif opcion == "2":
        return LECTURAS_MV_NEGATIVAS
    else:
        print("Opción inválida. Por favor, ingrese 1 o 2.")
        return quelista_desea()

def mv_a_celsius(lectura_mv):
    lectura_mv = quelista_desea()
    lecturas_celsius = []
    for elemento in lectura_mv:
        temp_c = elemento / MV_POR_GRADO
        lecturas_celsius.append(temp_c)
    return lectura_mv

def analizar_lecturas(lecturas_mv):
    lecturas_celsius = lista
    lista = lecturas_celsius
    suma = 0
    maximo = lista[0]
    criticas = []
    
    for elemento in lista:
        # Suma
        suma += mv_a_celsius

        # Máximo
        if mv_a_celsius > maximo:
            maximo = mv_a_celsius

        # Lecturas críticas
        if mv_a_celsius > UMBRAL_CRITICO_C:
            criticas.append(mv_a_celsius)

    porcentaje = len(criticas) / len(lista) * 100

    return suma, maximo, criticas, porcentaje


while True:

    lista_seleccionada = quelista_desea()

    suma, maximo, criticas, porcentaje = analizar_lecturas(lista_seleccionada)

    print(f"\nNumero de lecturas: {len(lista_seleccionada)}")
    print(f"Suma de lecturas: {suma:.2f} °C")
    print(f"Promedio de lecturas: {suma / len(lista_seleccionada):.2f} °C")
    print(f"Maximo de lecturas: {maximo:.2f} °C")
    print(f"Lecturas críticas: {criticas}")
    print(f"Porcentaje de lecturas críticas: {porcentaje:.2f}%")

    continuar = input("\n¿Desea realizar otra operación? (sí/no): ").strip().lower()

    if continuar not in ("sí", "si", "yes"):
        print("Hasta luego!")
        break