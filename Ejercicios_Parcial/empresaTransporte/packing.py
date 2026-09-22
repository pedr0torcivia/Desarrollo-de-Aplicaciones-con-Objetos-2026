from carga import Carga

class Packing(Carga):
    def __init__(self, contenido, producto, peso, cantidad, estructura): 
        super().__init__(contenido)
        self.producto = producto
        self.peso = peso
        self.cantidad = cantidad
        self.estructura = estructura

    def __str__(self):
        return f"{super().__str__()} Producto: {self.producto} - Peso: {self.peso} - Cantidad: {self.cantidad} - Estructura: {self.estructura}"

    def peso(self):
        return self.peso * self.cantidad