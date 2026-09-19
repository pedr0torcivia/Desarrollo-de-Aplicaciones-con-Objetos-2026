from inmobiliaria import Inmobiliaria
from inmueble import Inmueble
from casa import Casa
from departamento import Departamento 


def main():
    inmb = Inmobiliaria()
    arch = open("inmuebles.csv")
    for linea in arch.readlines():
        
        dato = linea.split(",")
        tipo = int(dato[0])
        codigo = int(dato[1])
        propietario = dato[2]
        alquiler_base = float(dato[3])
        superficie = int(dato[4])

        if tipo == 1:
            dormitorios = int(dato[5])
            pileta = bool(int(dato[6]))
            casa = Casa(codigo, propietario, superficie, alquiler_base, dormitorios, pileta)
            inmb.agregar(casa)

        else:
            expensas = float(dato[5])
            piso = int(dato[6])
            dpto = Departamento(codigo, propietario, superficie, alquiler_base, expensas, piso)
            inmb.agregar(dpto)
    arch.close()

    #Suma de alquileres
    print(inmb.suma_alquileres())
    print(inmb.cantidad_casas_premium())
    print(inmb.propietario_alquiler_mas_bajo())

    return



if __name__ == "__main__":
    main()
