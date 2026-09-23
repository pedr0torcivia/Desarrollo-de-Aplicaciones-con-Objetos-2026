from solucion import Pelicula, PeliculaEstandar, PeliculaEstreno

def main():
    archivo = open("peliculas.csv")
    peliculas = []
    importe_finalt1 = 0
    importe_finalt2 = 0
    importe_total = 0
    mas120 = 0
    dif_Gen = []
    first = True

    for linea in archivo.readlines():
        datos = linea.split(",")
        if first:
            first = False
            continue 

        tipo = int(datos[0])
        codigo = int(datos[1])
        titulo = datos[2]
        genero = datos[3]
        duracion = float(datos[4])
        precio = float(datos[5])

        if tipo == 1:
            pelicula = PeliculaEstandar(codigo, titulo, genero, duracion, precio)
            importe_finalt1 += pelicula.importe_final()

        if tipo == 2: 
            pelicula = PeliculaEstreno(codigo,titulo, genero, duracion, precio)
            importe_finalt2 += pelicula.importe_final()   

        importe_total += pelicula.importe_final()

        if duracion > 120: 
            mas120 +=1

        if genero not in dif_Gen:
            dif_Gen.append(genero)

        peliculas.append(pelicula)   
        print(pelicula)      
    archivo.close()

    print(importe_finalt1)
    print(importe_finalt2)
    print(importe_total)
    print(mas120)
    print(dif_Gen)
if __name__ == "__main__":
    main()