from abc import ABC, abstractmethod

class Pedido(ABC):
    def __init__(self,codigo,flor,color,cantidad,precio_unitario):
        self.codigo = codigo
        self.flor = flor
        self.color = color
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"codigo: {self.codigo}, flor: {self.flor}, color: {self.color}, cantidad: {self.cantidad}, precio_unitario: {self.precio_unitario}"

    @abstractmethod
    def importe_final(self):
        pass


class RamoSimple(Pedido):
    def __init__(self,codigo,flor,color,cantidad,precio_unitario):
        super().__init__(codigo,flor,color,cantidad,precio_unitario)

    def importe_final(self):
        return self.precio_unitario * self.cantidad


class ArregloPremium(Pedido):
    def __init__(self,codigo,flor,color,cantidad,precio_unitario):
        super().__init__(codigo,flor,color,cantidad,precio_unitario)

    def importe_final(self):
        if self.cantidad >= 12:
            return ((self.precio_unitario * self.cantidad) * 1.35) * 0.9
        else:
            return ((self.precio_unitario * self.cantidad) * 1.35)
