from atencion import Atencion, AtencionMedica, AtencionFarmacia

class Hospital: 
    def __init__(self, razonSocial):
        self.razonSocial = razonSocial
        self.atencionesRealizadas = []

    def addAtencion(self, atencion):
        if isinstance(atencion, Atencion):
            self.atencionesRealizadas.append(atencion)

    def importe_total_atencion_consulta(self):
        suma = 0
        for at in self.atencionesRealizadas: 
            if isinstance(at, AtencionMedica):
                suma += at.importe
        return suma

    def importe_promedio_atenciones(self, v1, v2):
        suma = 0
        cant = 0

        for at in self.atencionesRealizadas: 
            if isinstance(at, AtencionMedica):
                imp = at.importeACobrar()
                if v1 < imp < v2:
                    suma += imp 
                    cant += 1

        if cant > 0:
            return suma/cant
        else:
            return 0

    def codigo_primera_atencion_habitual(self):
        for at in self.atencionesRealizadas:
            if isinstance(at, AtencionMedica):
                paciente = at.get_paciente()
                if paciente.esPacienteHabitual():
                    return at.codigo

        return 0