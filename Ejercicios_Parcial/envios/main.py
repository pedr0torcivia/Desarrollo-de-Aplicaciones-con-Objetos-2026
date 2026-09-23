from solucion import Envio, EnvioComun, EnvioExpress


def main():
    archivo = open("envios.csv")
    envios = []
    importe_final_t1 = 0
    importe_final_t2 = 0
    total_recaudar = 0
    mas10 = 0
    ciudades = []
    primer = True 

    for linea in archivo.readlines():
        if primer:
            primer = False
            continue 

        dato = linea.split(",")
        tipo = int(dato[0])
        codigo = int(dato[1])
        ciudad = dato[2]
        peso = float(dato[3])
        costo_base = float(dato[4])

        if tipo == 1:
            envio = EnvioComun(codigo, ciudad, peso, costo_base)
            importe_final_t1 += envio.importe_final()

        elif tipo == 2:
            envio = EnvioExpress(codigo, ciudad, peso, costo_base)
            importe_final_t2 += envio.importe_final()

        total_recaudar += envio.importe_final()

        if peso > 10:
            mas10 += 1

        if ciudad not in ciudades: 
            ciudades.append(ciudad)

        envios.append(envio)

    archivo.close()

    for envio in envios:
        print(envio)

    print(importe_final_t1)
    print(importe_final_t2)
    print(total_recaudar)
    print(mas10)
    print(ciudades)

if __name__ == "__main__":
    main()