from abc import ABC, abstractmethod

class Comic(ABC):
    def __init__(self, codigo, titulo, editorial, cant_pags, precio_base):
        self.codigo = codigo
        self.titulo = titulo
        self.editorial = editorial
        self.cant_pags = cant_pags
        self.precio_base = precio_base

    def __str__(self):
        return f"Codigo: {self.codigo} - Titulo: {self.titulo} - Editorial: {self.editorial} - Cant Pags: {self.cant_pags} - P. Base: {self.precio_base}"

    @abstractmethod
    def precio_final(self):
        pass

class ComicRegular(Comic):
    def __init__(self, codigo, titulo, editorial, cant_pags, precio_base):
        super().__init__(codigo, titulo, editorial, cant_pags, precio_base)

    def precio_final(self):
        return self.precio_base

class ComicColeccion(Comic):
    def __init__(self, codigo, titulo, editorial, cant_pags, precio_base):
        super().__init__(codigo, titulo, editorial, cant_pags, precio_base)

    def precio_final(self):
        if self.cant_pags > 200:
            return (self.precio_base * 1.40) + 1500
        else:
            return self.precio_base * 1.40