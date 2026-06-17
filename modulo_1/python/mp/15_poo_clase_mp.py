class Producto:
    categoria_default = "General"

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f}"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * porcentaje / 100
        print(f"Descuento del {porcentaje}% aplicado. Nuevo precio: ${self.precio:.2f}")

    def __str__(self):
        return f"Producto({self.nombre}, ${self.precio:.2f})"

    def __repr__(self):
        return f"Producto(nombre={self.nombre!r}, precio={self.precio!r})"


laptop = Producto("Laptop Pro", 1200.00)
mouse = Producto("Mouse Inalambrico", 35.00)

print(laptop.mostrar())
print(mouse.mostrar())
laptop.aplicar_descuento(10)
print(str(laptop))
print(repr(mouse))
print(Producto.categoria_default)
