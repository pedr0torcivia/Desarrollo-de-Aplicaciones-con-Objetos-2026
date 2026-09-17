class Libro: 
    def __init__(self, titulo, autor, paginas, estado):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}, Estado: {self.estado}"

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible para prestar."

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' no estaba prestado."




def main():
    libro1 = Libro("Polinizar", "Geronimo \"Momo\"", 417, "disponible")
    libro2 = Libro("1984", "George Orwell", 328, "prestado")

    print(libro1)
    print(libro2)

    print(libro1.prestar())
    print(libro1.prestar())
    print(libro1.devolver())
    print(libro2.devolver())


if __name__ == "__main__":
    main()
