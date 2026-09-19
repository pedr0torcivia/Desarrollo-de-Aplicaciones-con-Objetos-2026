#  ven incrementado su importe base en $20.000 si se encuentran 
# en un piso inferior al tercero y se les incorpora el importe de 
# las expensas.
from inmueble import Inmueble
from abc import ABC, abstractmethod 

class Departamento(Inmueble):
    def __init__(self, codigo, propietario, superficie, importe_base,expensas, piso):
        super().__init__(codigo, propietario, superficie, importe_base)
        self.piso = piso
        self.expensas = expensas

    @abstractmethod
    def alquiler(self):
        importe_piso = 0
        if self.piso < 3: importe_piso = 20000
        return self.importe_base+ importe_piso + self.expensas
    