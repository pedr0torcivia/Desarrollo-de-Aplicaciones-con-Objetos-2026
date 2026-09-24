from solucion import Pedido, ArregloPremium, RamoSimple

class Floreria:
    def __init__(self):
        self.pedidos = []

    def add_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            self.pedidos.append(pedido)

    def mostrar_importes(self):
        for pedido in self.pedidos:
            print(pedido)
            print(f"Precio final: {pedido.importe_final()}")

    def total(self):
        tot = 0
        for ped in self.pedidos:
            tot += ped.importe_final()
        return tot

    def imp_prom(self, v1, v2):
        tot = 0
        cant = 0

        for ped in self.pedidos:
            imp = ped.importe_final()
            if v1 <= imp <= v2:
                tot += imp
                cant += 1

        if cant > 0: return tot/cant
        else: return 0

    def al_menos_12(self):
        for ped in self.pedidos:
            if ped.cantidad >= 12:
                return ped
        return None

    def color_mayor(self):
        cant_x_color = {}

        for ped in self.pedidos: 
            if ped.color not in cant_x_color:
                cant_x_color[ped.color] = 0
            cant_x_color[ped.color] += ped.cantidad

        mayor = 0
        col = ""
        for color in cant_x_color:
            if mayor < cant_x_color[color]:
                mayor = cant_x_color[color]
                col = color 
        return color


     
