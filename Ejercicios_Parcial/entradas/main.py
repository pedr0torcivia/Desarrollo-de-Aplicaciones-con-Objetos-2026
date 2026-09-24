from solucion import Entrada, EntradaGeneral, EntradaVIP


def main():
    archivo = open("entradas.csv")
    entradas = []
    total_recaudado = 0
    cant = 0
    precio_promedio = 0
    cant_campo = 0

    primer = True 

    for linea in archivo.readlines(): 
        if primer:
            primer = False
            continue 
        
        datos = linea.split(",")
        tipo = int(datos[0])
        numero = int(datos[1])
        comprador = datos[2]
        sector = datos[3]
        precio_base = float(datos[4])

        if tipo == 1:
            entrada = EntradaGeneral(numero, comprador, sector, precio_base)
        elif tipo == 2: 
            entrada = EntradaVIP(numero, comprador, sector, precio_base)

        entradas.append(entrada)
        precio_final = entrada.precio_final()
        print(entrada)
        print(f"Precio Final: {precio_final}")
        print()

        total_recaudado += precio_final
        cant += 1

        if sector == "Campo":
            cant_campo += 1 

    archivo.close()

    if cant != 0:
        precio_promedio = total_recaudado / cant
    else:
        precio_promedio = 0

    print(f"Total: {total_recaudado}")
    print(f"Precio Promedio: {precio_promedio}")
    print(f"Cantidad Campo: {cant_campo}")



if __name__ == "__main__":
    main()