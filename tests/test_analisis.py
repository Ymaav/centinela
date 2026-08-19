import pytest

from centinela.analisis import LECTURAS_MV_POSITIVAS, analizar_lecturas, mv_a_celsius


def test_maximo_del_turno_positivo():
    temperaturas_c = mv_a_celsius(LECTURAS_MV_POSITIVAS)
    suma, maximo, criticas, porcentaje = analizar_lecturas(temperaturas_c)

    assert maximo == 90.56


def test_porcentaje_de_criticas():
    temperaturas_c = mv_a_celsius(LECTURAS_MV_POSITIVAS)
    suma, maximo, criticas, porcentaje = analizar_lecturas(temperaturas_c)

    assert porcentaje == 37.5

def test_conversion_de_una_lectura():
    assert mv_a_celsius([253.7]) == pytest.approx([25.37])