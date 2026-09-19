from casa import Casa
from departamento import Departamento

class Inmobiliaria:
    def __init__(self):
        self.inmuebles = []

    #Composición
    def agregar(self, inmueble):
        self.inmuebles.append(inmueble)

    def suma_alquileres(self):
        suma = 0
        for inm in self.inmuebles:
            suma += inm.alquiler()
        return suma

    def cantidad_casas_premium(self):
        cant = 0
        for inm in self.inmuebles:
            if isinstance(inm, Casa) and inm.superficie > 150 and inm.dormitorios > 2 and inm.pileta:
                    cant += 1 
        return cant
    
    def propietario_alquiler_mas_bajo(self):
        menor = None
        for inm in self.inmuebles:
            if isinstance(inm, Departamento):
                if menor is None or menor.alquiler() > inm.alquiler():
                    menor = inm

        if menor is None: return None
        return menor.propietario
             

# METODOS 

#Suma de alquileres: informe el total a recaudar en concepto de alquileres 
#si todos los inmuebles se encuentran alquilados.
#Cantidad de casas premium: informe la cantidad de casas de más de 150 
# metros cuadrados, más de 2 dormitorios y que posean pileta.
#Propietario del alquiler más bajo: informe el nombre del propietario 
# del departamento con el alquiler cuyo importe definitivo sea el más bajo