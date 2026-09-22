from carga import Carga

class Camion:
    def __init__(self, patente, estado, carga_maxima):
        self.patente = patente
        self.estado = estado
        self.carga_maxima = carga_maxima
        self.cargas = []

    def __str__(self):
        str = f"Patente: {self.patente} - Estado: {self.estado} - Carga Max: {self.carga_maxima}"
        cargas = ""

        for carg in self.cargas:
            cargas += carg.__str__()
        return str + cargas

    def cantidad_cargas(self): 
        cant = 0
        for carg in self.cargas:
            cant+=1
        return cant

    def subir_carga(self, carga):
        self.cargas.append(carga)

    def bajar_carga(self, carga):
        for carg in self.cargas:
            if carg == carga: 
                self.cargas.remove(carg)

    def peso_cargas(self):
        peso = 0
        for carg in self.cargas:
            peso += carg.peso()
        return peso

    def a_reparacion(self):
        self.estado = "A Reparación"

    def sale_reparado(self):
        self.estado = "Reparado"

    def en_viaje(self):
        self.estado = "En Viaje"

    def listo_para_salir(self):
        if self.estado == "Disponible" and self.peso_cargas() < (0.75 * self.carga_maxima):
            self.estado = "Listo para salir"

