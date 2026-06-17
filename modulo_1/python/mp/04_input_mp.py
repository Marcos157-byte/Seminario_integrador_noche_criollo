producto = input("Ingrese el nombre del producto: ")
print(f"Producto registrado: {producto}")

precio_str = input("Ingrese el precio del producto: ")
print(f"El precio es: {precio_str}")
precio_float = float(precio_str)
print(f"Con IVA (12%): {precio_float * 1.12:.2f}")
