LECTURAS_MV_POSITIVAS = [253.7, 550.0, 812.3, 190.5, 402.1, 905.6, 380.0, 811.9]
LECTURAS_MV_NEGATIVAS = [-150.0, -180.5, -95.2, -210.8, -175.3]
MV_POR_GRADO = 10
UMBRAL_CRITICO_C = 80  # Esta en celsius.


def pedir_lista():

    print(
        "Que lista desea utilizar? \n1.Lista de lecturas positivas \n2.Lista de lecturas negativas"
    )
    decision = input("Ingrese el numero de la opcion deseada: ")
    if decision == "1":
        return LECTURAS_MV_POSITIVAS
    elif decision == "2":
        return LECTURAS_MV_NEGATIVAS
    else:
        print("\nOpcion ivalida. Por favor, ingrese 1 o 2.\n")
        return pedir_lista()


def mv_a_celsius(lecturas_mv):
    return [elemento / MV_POR_GRADO for elemento in lecturas_mv]


def analizar_lecturas(temperaturas_c):
    if not temperaturas_c:
        raise ValueError("No hay lecturas que analizar: la lista esta vacia")
    suma = sum(temperaturas_c)
    maximo = max(temperaturas_c)
    criticas = [elemento for elemento in temperaturas_c if elemento > UMBRAL_CRITICO_C]
    porcentaje = len(criticas) / len(temperaturas_c) * 100

    return suma, maximo, criticas, porcentaje


def mostrar_reporte(reporte, temp_c):

    suma, maximo, criticas, porcentaje = reporte

    print(f"\nNumero de lecturas: {len(temp_c)}")
    print(f"Suma de lecturas: {suma:.2f} °C")
    print(f"Promedio de lecturas: {suma / len(temp_c):.2f} °C")
    print(f"Maximo de lecturas: {maximo:.2f} °C")
    print(f"Lecturas críticas: {criticas}")
    print(f"Porcentaje de lecturas críticas: {porcentaje:.2f}%")


def main():
    while True:
        lecturas_mv = pedir_lista()
        temperaturas_c = mv_a_celsius(lecturas_mv)
        resultados = analizar_lecturas(temperaturas_c)
        mostrar_reporte(resultados, temperaturas_c)

        continuar = input("\n¿Desea realizar otra operación? (sí/no): ").strip().lower()
        if continuar not in ("sí", "si", "yes"):
            break


if __name__ == "__main__":
    main()
    print(analizar_lecturas(mv_a_celsius(LECTURAS_MV_POSITIVAS)))
