from abc import ABC, abstractmethod

class Pelicula(ABC):
    def __init__(self, codigo, titulo, genero, duracion, precio_base):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.precio_base = precio_base

    def __str__(self):
        return f"Codigo: {self.codigo} - Titulo: {self.titulo} - genero: {self.genero} - Duracion: {self.duracion} - Precio: {self.precio_base}"

    @abstractmethod
    def importe_final(self):
        pass 

class PeliculaEstreno(Pelicula):
    def __init__(self, codigo, titulo, genero, duracion, precio_base):
        super().__init__(codigo, titulo, genero, duracion, precio_base)

    def importe_final(self):
        return self.precio_base * 1.25

class PeliculaEstandar(Pelicula):
    def __init__(self, codigo, titulo, genero, duracion, precio_base):
        super().__init__(codigo, titulo, genero, duracion, precio_base)

    def importe_final(self):
        return self.precio_base

