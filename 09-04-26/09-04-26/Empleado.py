## Crear una clase Empleado con legajo, nombre, sueldo y antigüedad en años. Implementar el constructor y __str__().
##Agregar un método aumentar_sueldo(porcentaje) y otro método es_antiguo() que retorne True cuando el empleado
##tenga 10 años o más de antigüedad. Crear al menos dos empleados y probar los métodos.

class Empleado:
    def __init__(self, legajo, nombre, sueldo, antiguedad):
        self.legajo = legajo
        self.nombre = nombre
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def __str__(self):
        return f"Legajo: {self.legajo}, Nombre: {self.nombre}, Sueldo: {self.sueldo}, Antigüedad: {self.antiguedad} años"

    def aumentar_sueldo(self, porcentaje):
        aumento = self.sueldo * (porcentaje / 100)
        self.sueldo += aumento
        return f"Sueldo aumentado en {porcentaje}%. Nuevo sueldo: {self.sueldo}"

    def es_antiguo(self):
        return self.antiguedad >= 10


def main():
    empleado1 = Empleado("001", "Juan Perez", 50000, 12)
    empleado2 = Empleado("002", "Maria Lopez", 45000, 8)

    print(empleado1)
    print(empleado2)

    print(empleado1.aumentar_sueldo(10))
    print(empleado2.aumentar_sueldo(5))

    print(f"¿{empleado1.nombre} es antiguo? {empleado1.es_antiguo()}")
    print(f"¿{empleado2.nombre} es antiguo? {empleado2.es_antiguo()}")  


if __name__ == "__main__":
    main()