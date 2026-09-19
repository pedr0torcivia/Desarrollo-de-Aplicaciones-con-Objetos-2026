class Paciente:
    def __init__(self, nombre, sintoma, habitual="false"):
        self.nombre = nombre
        self.sintoma = sintoma 
        self.habitual = habitual

    def set_nombre(self, nom):
        self.nombre = nom

    def set_sintoma(self, sint):
        if sint in [1, 2, 3]:
            self.sintoma = sint
        else:
            raise ValueError("Síntoma inválido")
    
    def set_habitual(self, es):
        self.habitual = es

    def esPacienteHabitual(self):
        return self.get_habitual()

    def get_nombre(self):
        return self.nombre

    def get_sintoma(self):
        return self.sintoma

    def get_habitual(self):
        return self.habitual

    def __str__(self):
        if self.sintoma == 1:
            sint = "corazon"
        elif self.sintoma == 2:
            sint = "pulmon"
        else:
            sint = "otras"

        return f"Nombre: {self.nombre} - Sintoma: {sint} - Es habitual: {self.habitual}"