def ejercicio1():
    lista = []
    cant = 10
    suma = 0

    while cant <= 10 and cant > 0:
        lista.append(cant - 1)
        print(cant)
        cant -= 1

    for i in lista:
        suma += i

    print(lista)
    print(suma)
    return 

def ejercicio2():
    max = int(input("Max: "))
    min = int(input("Min: "))
    n = min
    suma = 0
    cant = 0

    while min <= n <=max: 
        suma += n
        n += 1
        cant +=1

    if cant != 0:
        promedio = suma/cant
    else:
        promedio = 0

    print(f"Promedio: {promedio}")

    return


def main():
    ejercicio1()
    ejercicio2()



if __name__ == "__main__":
    main()