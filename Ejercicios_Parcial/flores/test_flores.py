import pytest

from solucion import Pedido, RamoSimple, ArregloPremium


def test_ramo_simple_calcula_cantidad_por_precio_unitario():
    pedido = RamoSimple(
        1,
        "Rosa",
        "Rojo",
        5,
        1000.0
    )

    assert isinstance(pedido, PedidoFlor)
    assert pedido.importe_final() == pytest.approx(5000.0)


def test_arreglo_premium_menor_a_12_aplica_solo_recargo_del_35_por_ciento():
    pedido = ArregloPremium(
        2,
        "Orquidea",
        "Violeta",
        10,
        1000.0
    )

    assert isinstance(pedido, PedidoFlor)
    assert pedido.importe_final() == pytest.approx(13500.0)


def test_arreglo_premium_con_12_o_mas_aplica_recargo_y_luego_descuento():
    pedido = ArregloPremium(
        3,
        "Lirio",
        "Blanco",
        12,
        1000.0
    )

    # 12 * 1000 = 12000; +35% = 16200; -10% = 14580
    assert pedido.importe_final() == pytest.approx(14580.0)
