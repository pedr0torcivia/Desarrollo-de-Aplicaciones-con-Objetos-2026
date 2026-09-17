class Producto:
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def hay_stock(self):
        if self.stock > 0:
            return "Hay stock disponible"
        else:
            return "No hay stock disponible"

    def valor_stock(self):
        return self.precio * self.stock

    def __str__(self):
        return f"Código: {self.codigo}, Descripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock}"



def main():
    p1 = Producto("001", "Producto A", 10.0, 5)
    p2 = Producto("002", "Producto B", 15.0, 0)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()