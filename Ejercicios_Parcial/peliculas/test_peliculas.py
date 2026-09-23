import pytest

from solucion import Pelicula, PeliculaEstandar, PeliculaEstreno


def test_pelicula_estandar_conserva_precio_base():
    pelicula = PeliculaEstandar(
        1,
        "The Godfather",
        "Drama",
        105,
        4000.0
    )

    assert isinstance(pelicula, Pelicula)
    assert pelicula.importe_final() == pytest.approx(4000.0)


def test_pelicula_estreno_aplica_recargo_del_25_por_ciento():
    pelicula = PeliculaEstreno(
        2,
        "Oppenheimer",
        "Accion",
        128,
        4000.0
    )

    assert isinstance(pelicula, Pelicula)
    assert pelicula.importe_final() == pytest.approx(5000.0)
