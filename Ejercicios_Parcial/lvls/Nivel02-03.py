class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.precio}"
    
    def precio_iva(self):
        precio = self.precio + (self.precio * 0.21)
        return precio 

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0: 
            raise ValueError("Invalido")
        self._precio = valor 


class Tienda:
    def __init__(self, productos):
        self.productos = []

    def __str__(self):
        texto = ""

        for producto, cantidad in self.productos:
            texto += f"{producto} - Cantidad: {cantidad}\n"

        return texto
        
    def agregar_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise TypeError("debe ingresar un objeto tipo producto")

        self.productos.append([producto, cantidad])



def main():
    producto1 = Producto("Pepsi", 10)
    producto2 = Producto("Hamburguesa", 100)
    producto = []

    tienda = Tienda(producto)
    tienda.agregar_producto(producto1, 2)
    tienda.agregar_producto(producto2, 1)

    print(tienda)

if __name__ == "__main__":
    main()