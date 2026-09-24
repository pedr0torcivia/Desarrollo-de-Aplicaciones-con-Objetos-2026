from solucion import Comic, ComicColeccion, ComicRegular
from tienda import Tienda

def main():
    archivo = open("comics.csv")
    tienda = Tienda("nombre")

    primero = True

    for linea in archivo.readlines():
        if primero:
            primero = False
            continue

        datos = linea.split(",")
        tipo = int(datos[0])
        codigo = datos[1]
        titulo = datos[2]
        editorial = datos[3]
        paginas = int(datos[4])
        precio_base = float(datos[5])

        if tipo == 1:
            comic = ComicRegular(codigo, titulo, editorial, paginas, precio_base)
        elif tipo == 2:
            comic = ComicColeccion(codigo, titulo, editorial, paginas, precio_base)

        tienda.add_comic(comic)
    archivo.close()

    tienda.mostrar_precios()
    print(f"Total: {tienda.total()}")
    print(f"Mas 200 Pags: {tienda.mas_200()}")
    print(f"Titulo Mayor Precio: {tienda.titulo_mayor()}")
    print(f"Editoriales: {tienda.editoriales()}")


if __name__ == "__main__":
    main()