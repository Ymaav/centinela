# Analizador de lecturas de un sensor de temperatura

## ¿Qué es?

Analizador de lecturas de un sensor de temperatura LM35 que convierte lecturas en milivolts a grados Celsius y permite identificar temperaturas críticas. También puede analizar múltiples lecturas y generar estadísticas como promedio, máximo y porcentaje de lecturas críticas.

## 1. ¿Cómo se usa?

El proyecto contiene dos programas.

### Centinela — análisis de series de lecturas

Instala las dependencias y ejecútalo:

```bash
uv sync
uv run centinela
```

El programa pide elegir una de las dos listas de lecturas en mV (opción 1 o 2) y muestra el reporte del turno.

### Sensor — lectura individual

Es un programa independiente que se ejecuta directamente:

```bash
python3 sensor.py
```

Pide una lectura del sensor en milivolts y devuelve la temperatura y su estado.

## 2. ¿Qué hace por dentro?

El programa convierte las lecturas de milivolts a grados Celsius utilizando:

`°C = mV / 10`

Después clasifica las temperaturas de acuerdo con los umbrales establecidos:

* Menos de `40 °C`: Normal.
* Entre `40 °C` y `80 °C`: Advertencia.
* Más de `80 °C`: Crítico.

En el analizador de múltiples lecturas también calcula estadísticas del conjunto de datos, como:

* Número de lecturas.
* Suma de temperaturas.
* Promedio.
* Temperatura máxima.
* Lecturas críticas.
* Porcentaje de lecturas críticas.

El proyecto utiliza funciones como `pedir_lista()`, `mv_a_celsius()`, `analizar_lecturas()` y `mostrar_reporte()` para separar las diferentes partes del procesamiento.
