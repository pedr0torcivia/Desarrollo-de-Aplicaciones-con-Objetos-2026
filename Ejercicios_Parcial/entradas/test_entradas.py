import pytest
from solucion import Entrada,EntradaGeneral,EntradaVIP
def test_general():
 e=EntradaGeneral(1,"Ana","Campo",10000); assert isinstance(e,Entrada); assert e.precio_final()==pytest.approx(10000)
def test_vip():
 e=EntradaVIP(2,"Juan","Platea",10000); assert isinstance(e,Entrada); assert e.precio_final()==pytest.approx(12500)
