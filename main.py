class Producto:
    def __init__(self, nombre, precio, stock):
        if precio < 0 or stock < 0:
            raise ValueError("el precio y el stock deben ser mayores o iguales a 0")
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def agregar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("el porcentaje debe estar entre un 0% y 100%")
        descuento = self._precio * (porcentaje/100)
        self._precio -= descuento

    def comprobar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            return False
        self.stock +cantidad
        return True
            

    
