from carga import Carga

class Caja(Carga):
    def __init__(self, contenido, producto,peso):
        super().__init__(contenido)
        self.producto = producto
        self.peso = peso

    def __str__(self):
        return f"{super().__str__()} Producto: {self.producto} - Peso: {self.peso}"

    def peso(self):
        return self.peso