LECTURAS_MV_POSITIVAS = [253.7, 550.0, 812.3, 190.5, 402.1, 905.6, 380.0, 811.9]
LECTURAS_MV_NEGATIVIAS = [-150.0, -180.5, -95.2, -210.8, -175.3]
MV_POR_GRADO = 10
UMBRAL_CRITICO_C = 80
while True:
    def quelista_desea():
        print("¿Qué lista desea utilizar?")
        print("1. Lista de lecturas positivas")
        print("2. Lista de lecturas negativas")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            return LECTURAS_MV_POSITIVAS
        elif opcion == "2":
            return LECTURAS_MV_NEGATIVIAS
        else:
            print("Opción inválida. Por favor, ingrese 1 o 2.")
            return quelista_desea()
    lista_seleccionada = quelista_desea()
    def suma_lecturas(lista):
        suma = 0
        for lectura_mv in lista:
            suma += lectura_mv
        return suma
    def mi_maximo(lista):
        maximo = lista[0]
        for elemento in lista:
            if elemento > maximo:
                maximo = elemento
        return maximo
    def lecturas_criticas(lista):
        criticas = []
        for elemento in lista:
            if elemento > UMBRAL_CRITICO_C * MV_POR_GRADO:
                criticas.append(elemento)
        return criticas
    def porcentaje_criticas(lista):
        criticas = lecturas_criticas(lista)
        return len(criticas) / len(lista) * 100

    print(f"Numero de lecturas: {len(lista_seleccionada)}")
    print(f"Promedio de lecturas: {suma_lecturas(lista_seleccionada)/len(lista_seleccionada):.2f}°C")
    print(f"Maximo de lecturas: {mi_maximo(lista_seleccionada):.2f}°C")
    print(f"Lecturas críticas: {lecturas_criticas(lista_seleccionada)}")
    print(f"Porcentaje de lecturas críticas: {porcentaje_criticas(lista_seleccionada):.2f}%")

    continuar = input("¿Desea realizar otra operación? (sí/no): ").strip().lower()
    if continuar not in ("sí", "si", "yes"):
        print("Hasta luego!")
        break