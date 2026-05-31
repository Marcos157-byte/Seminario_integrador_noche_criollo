print("Ciclos for")
print("for clasico")
for i in range(1, 6):
    print(f"Iteracion {i}")

print("for con lista")
ciudades = ["Quito", "Guayaquil", "Cuenca", "Loja"]
for ciudad in ciudades:
    print(ciudad)

print("control de iteracion")
for i in range(1, 10):
    if i == 3: continue
    if i == 8: break
    print(i)
else:
    print("Ciclo for terminado")

print("for con range step")
for i in range(0, 20, 4):
    print(i)

print("for regresivo")
for i in range(5, 0, -1):
    print(f"Cuenta regresiva: {i}")

print("for con enumerate")
frutas = ["Manzana", "Pera", "Mango", "Uva"]
for i, fruta in enumerate(frutas):
    print(f"Posicion: {i}, Fruta: {fruta}")

print("for con zip")
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [1200, 25, 45, 350]
for producto, precio in zip(productos, precios):
    print(f"Producto: {producto}, Precio: ${precio}")

print("for anidados")
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"fila: {fila}, columna: {columna}")
