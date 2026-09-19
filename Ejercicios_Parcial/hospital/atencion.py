from paciente import Paciente
from abc import ABC, abstractmethod

class Atencion(ABC):
    def __init__(self, codigo, tipoDeCobroDeCobro):
        self.codigo = codigo
        self.tipoDeCobro = tipoDeCobroDeCobro

    def get_codigo(self):
        return self.codigo

    def get_tipoDeCobro(self):
        return self.tipoDeCobroDeCobro

    def set_codigo(self, cod):
        self.codigo = cod
    
    def set_tipoDeCobro(self, tip):
        self.tipoDeCobroDeCobro = tip

    def __str__(self):
        return f"Codigo: {self.codigo} - tipoDeCobro: {self.tipoDeCobro} - "

    @abstractmethod
    def importeACobrar(self):
        pass


class AtencionMedica(Atencion):
    def __init__(self, codigo, tipoDeCobro, paciente, importe):
        super().__init__(codigo, tipoDeCobro)
        self.paciente = paciente
        self.importe = importe

    def get_paciente(self):
        return self.paciente

    def get_importe(self):
        return self.importe

    def set_paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.paciente = paciente
        else:
            print("Debe ser un obj paciente")

    def get_importe(self):
        return self.importe

    def __str__(self):
        return f"{super().__str__()}Paciente Atendido:{self.paciente} - importe: {self.importe}"

    def importeACobrar(self):
        imp = self.importe
        if self.paciente.get_habitual():
            imp = imp * 0.75
        if self.tipoDeCobro == 1:
            imp = imp * 0.9
        elif self.tipoDeCobro == 2:
            imp = imp * 1.2
        return imp 


class AtencionFarmacia(Atencion):
    def __init__(self, codigo, tipoDeCobro, importeTotal, descuento):
        super().__init__(codigo, tipoDeCobro)
        self.importeTotal = importeTotal
        self.descuento = descuento 

    def get_importeTotal(self):
        return self.importeTotal

    def get_descuento(self):
        return self.descuento

    def set_importeTotal(self, imp):
        self.importeTotal = imp

    def set_descuento(self, desc):
        if desc >= 0:
            self.descuento = desc

    def importeACobrar(self):
        imp = self.importeTotal
        imp = imp - self.descuento

        if self.tipoDeCobro == 2:
            imp = imp * 1.3
        elif self.tipoDeCobro == 1: 
            imp = imp * 0.95
        return imp 
    