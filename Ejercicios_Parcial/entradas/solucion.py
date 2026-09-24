from abc import ABC, abstractmethod

class Entrada(ABC):
    def __init__(self,numero, comprador, sector, precio_base):
        self.numero = numero
        self.comprador = comprador
        self.sector = sector
        self.precio_base = precio_base

    @abstractmethod
    def precio_final():
        pass

    def __str__(self):
        return f"Numero: {self.numero} - Comprador: {self.comprador} - Sector: {self.sector} - Precio Base: {self.precio_base}"


class EntradaGeneral(Entrada):
    def __init__(self,numero, comprador, sector, precio_base):
        super().__init__(numero, comprador, sector, precio_base)

    def precio_final(self):
        return self.precio_base

class EntradaVIP(Entrada):
    def __init__(self,numero, comprador, sector, precio_base):
        super().__init__(numero, comprador, sector, precio_base)

    def precio_final(self):
        return self.precio_base * 1.25

    
