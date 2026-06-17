print("Diccionarios")

vacio = {}
print(vacio)

producto = {"nombre": "Laptop", "precio": 1299.99, "stock": 10, "disponible": True}
print(producto)

config = dict(servidor="192.168.1.1", puerto=3306, base_datos="ventas_db")
print(config)

print("Acceder a valores")
print(producto["nombre"])
print(producto.get("precio"))
print(producto.get("categoria", "Sin categoria"))

print("Modificar y agregar")
producto["precio"] = 1199.99
producto["categoria"] = "Electronica"
print(producto)

print("Recorrer diccionario")
for clave, valor in producto.items():
    print(f"  {clave}: {valor}")

print("Claves y valores")
print(list(producto.keys()))
print(list(producto.values()))

print("Eliminar clave")
del producto["disponible"]
print(producto)
