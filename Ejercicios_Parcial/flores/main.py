from floreria import Floreria
from solucion import Pedido, ArregloPremium, RamoSimple

def main():
    arch = open("flores.csv")
    tienda = Floreria()
    first = True

    for linea in arch.readlines():
        if first:
            first = False
            continue

        dato = linea.split(",")
        tipo = int(dato[0])
        codigo = int(dato[1])
        flor = dato[2]
        color = dato[3]
        cantidad = int(dato[4])
        precio = float(dato[5])

        if tipo == 1:
            ramo = RamoSimple(codigo, flor, color, cantidad, precio)
        elif tipo == 2:
            ramo = ArregloPremium(codigo, flor, color, cantidad, precio)

        tienda.add_pedido(ramo)

    tienda.mostrar_importes()
    print(tienda.total())
    print(tienda.imp_prom(1, 1500))
    print(tienda.al_menos_12())
    print(tienda.color_mayor())

if __name__ == "__main__":
    main()