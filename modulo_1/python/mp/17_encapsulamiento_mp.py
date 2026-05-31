class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.__productos = {}
        self.__movimientos = []
        self.__registrar(f"Inventario creado para {nombre_tienda}")

    @property
    def productos(self):
        return dict(self.__productos)

    @property
    def movimientos(self):
        return list(self.__movimientos)

    def agregar_producto(self, nombre, cantidad, precio):
        if cantidad < 0 or precio < 0:
            raise ValueError("Cantidad y precio deben ser positivos")
        self.__productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.__registrar(f"Agregado: {nombre} x{cantidad} a ${precio}")
        return self

    def vender(self, nombre, cantidad):
        if nombre not in self.__productos:
            raise ValueError(f"Producto '{nombre}' no existe")
        if self.__productos[nombre]["cantidad"] < cantidad:
            raise ValueError(f"Stock insuficiente de {nombre}")
        self.__productos[nombre]["cantidad"] -= cantidad
        total = cantidad * self.__productos[nombre]["precio"]
        self.__registrar(f"Venta: {nombre} x{cantidad} = ${total:.2f}")
        return total

    def __registrar(self, operacion):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M:%S")
        self.__movimientos.append(f"[{hora}] {operacion}")

    def __str__(self):
        return f"Inventario({self.nombre_tienda}: {len(self.__productos)} productos)"


tienda = InventarioTienda("TechStore")
tienda.agregar_producto("Laptop", 10, 1200).agregar_producto("Mouse", 50, 25)

ganancia = tienda.vender("Mouse", 5)
print(f"Ganancia por venta: ${ganancia:.2f}")
print(tienda)

for mov in tienda.movimientos:
    print(f"  {mov}")
