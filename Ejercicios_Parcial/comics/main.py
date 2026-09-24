from solucion import Comic, ComicColeccion, ComicRegular

def main():
    archivo = open("comics.csv")

    comics = []
    total = 0
    mas200 = 0
    tituloMayorPrecio = 0
    mayor = 0
    editoriales = []

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

        precio_final = comic.precio_final()
        comics.append(comic)
        print(comic)
        print(f"Precio Final: {precio_final}")    
        print()

        total += precio_final

        if paginas > 200:
            mas200 += 1

        if mayor < precio_final:
            tituloMayorPrecio = titulo
            mayor = precio_final

        if editorial not in editoriales:
            editoriales.append(editorial)

    archivo.close()

    print()
    print(f"Total: {total}")
    print(f"Mas 200 Pags: {mas200}")
    print(f"Titulo Mayor Precio: {tituloMayorPrecio} - {mayor}")
    print(f"Editoriales: {editoriales}")


if __name__ == "__main__":
    main()