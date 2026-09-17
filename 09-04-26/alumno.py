class Alumno:
    def __init__(self, legajo, nombre, nota1, nota2):
        self.legajo = legajo
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def __str__(self):
        return f"Legajo: {self.legajo}, Nombre: {self.nombre}, Nota 1: {self.nota1}, Nota 2: {self.nota2}"

    def promedio(self):
        return (self.nota1 + self.nota2) / 2
