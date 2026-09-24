import pytest

from solucion import Comic, ComicRegular, ComicColeccion


def test_comic_regular_conserva_precio_base():
    comic = ComicRegular(
        1,
        "Batman Year One",
        "Marvel",
        144,
        10000.0
    )

    assert isinstance(comic, Comic)
    assert comic.precio_final() == pytest.approx(10000.0)


def test_comic_coleccion_aplica_recargo_del_40_por_ciento():
    comic = ComicColeccion(
        2,
        "The Infinity Gauntlet",
        "Planeta",
        198,
        10000.0
    )

    assert isinstance(comic, Comic)
    assert comic.precio_final() == pytest.approx(14000.0)


def test_comic_coleccion_mas_de_200_paginas_agrega_recargo_fijo():
    comic = ComicColeccion(
        3,
        "Civil War",
        "Marvel",
        248,
        10000.0
    )

    assert comic.precio_final() == pytest.approx(15500.0)
