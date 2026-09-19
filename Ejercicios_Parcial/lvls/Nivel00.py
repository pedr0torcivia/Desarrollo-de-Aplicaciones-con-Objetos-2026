def descuento(precio, efectivo):
    precio = precio - (0.2 * precio)

    if efectivo == 1:
        precio = precio - (0.1 * precio)
    if efectivo == 2: 
        precio = precio + (0.2 * precio)
    return precio


def main():
    precio = int(input("Ingrese precio: "))
    registrado = input("Está Registrado? ")
    efectivo = input("Es con efectivo o tarjeta (1/2)? ")

    if registrado == "si":
        final = descuento(precio, efectivo)
    else:
        final = precio 

    print(f"El precio final es: {final}")
    print(f"El precio inicial era: {precio}")

    return

if __name__ == "__main__":
    main()