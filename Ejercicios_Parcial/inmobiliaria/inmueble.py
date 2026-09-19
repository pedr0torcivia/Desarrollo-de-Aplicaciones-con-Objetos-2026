from abc import ABC, abstractmethod


class Inmueble:
    def __init__(self, codigo, propietario, superficie, importe_base):
        self.codigo = codigo;
        self.propietario = propietario
        self.superficie = superficie
        self.importe_base = importe_base

    def __str__(self):
        return f""

    @abstractmethod
    def alquiler(self):
        pass


# METODOS
#Suma de alquileres: informe el total a recaudar en concepto de alquileres 
#si todos los inmuebles se encuentran alquilados.
#Cantidad de casas premium: informe la cantidad de casas de más de 150 
# metros cuadrados, más de 2 dormitorios y que posean pileta.
#Propietario del alquiler más bajo: informe el nombre del propietario 
# del departamento con el alquiler cuyo importe definitivo sea el más bajo

