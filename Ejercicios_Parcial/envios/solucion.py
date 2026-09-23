from abc import ABC, abstractmethod

class Envio(ABC):
    def __init__(self, codigo, ciudad, peso, costo_base):
        self.codigo = codigo
        self.ciudad = ciudad
        self.peso = peso
        self.costo_base = costo_base

    def __str__(self):
        return f"Código: {self.codigo} - Ciudad: {self.ciudad} - Peso: {self.peso} - Costo base: {self.costo_base}"
    
    @abstractmethod
    def importe_final():
        pass 


class EnvioExpress(Envio):
    def __init__(self, codigo, ciudad, peso, costo_base):
        super().__init__(codigo, ciudad, peso, costo_base)

    def importe_final(self):
        return self.costo_base*1.3


class EnvioComun(Envio):
    def __init__(self, codigo, ciudad, peso, costo_base):
            super().__init__(codigo, ciudad, peso, costo_base)

    def importe_final(self):
         return self.costo_base
