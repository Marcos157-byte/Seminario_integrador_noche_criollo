cadena_string = "Python", "es", "un", "lenguaje", "poderoso"
print(cadena_string)
print("Python", "es", "un", "lenguaje", "poderoso")
print("Python", "es", "un", "lenguaje", "poderoso", sep=",")
print("Python", "es", "un", "lenguaje", "poderoso", sep=" | ")
print("Rojo", "Verde", "Azul", sep="-")
print("Rojo", "Verde", "Azul", end="")
print("Rojo", "Verde", "Azul", sep=" - ")
print("Rojo", "Verde", "Azul", end=" >> ")
print("Rojo", "Verde", "Azul", end=" >> ")

producto = "Laptop Pro"
precio = 1299.99
print(producto, precio)
print(f"Producto: {producto}, Precio: ${precio}")
print(f"Con descuento 10%: ${precio * 0.90:.2f}")
print(f"{'Laptop':>10}")

temperatura = 36.6789

print(f"{temperatura:.1f}")
print(f"{5000000:,}")
