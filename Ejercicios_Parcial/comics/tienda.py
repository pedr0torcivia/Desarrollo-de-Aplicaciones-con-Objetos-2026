from solucion import Comic, ComicColeccion, ComicRegular

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.comics = []

    def add_comic(self,comic):
        if  isinstance(comic, Comic):
            self.comics.append(comic)

    def mostrar_precios(self):
        for comic in self.comics:
            print(comic)
            print(f"Precio Final: {comic.precio_final()}")
            print()

    def total(self):
        total = 0
        for comic in self.comics:
            total += comic.precio_final()
        return total

    def mas_200(self):
        mas200 = 0
        for comic in self.comics:
            if isinstance(comic, ComicColeccion) and comic.cant_pags > 200:
                mas200 += 1
        return mas200

    def titulo_mayor(self):
        titulo = ""
        mayor = 0
        for comic in self.comics:
            if mayor < comic.precio_final():
                mayor = comic.precio_final()
                titulo = comic.titulo
        return titulo 

    def editoriales(self):
        edi = []
        for comic in self.comics:
            if comic.editorial not in edi:
                edi.append(comic.editorial)
        return edi
    