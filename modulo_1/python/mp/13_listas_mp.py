print("Manipulacion de listas")
print("Crear listas")

vacia = []
print(vacia)
precios = [10.5, 25.0, 8.75, 99.99, 3.50]
print(precios)
colores = ["rojo", "azul", "verde", "amarillo"]
print(colores)
mixta = [1, "laptop", True, 3.14, None, "activo"]
print(mixta)
anidada = [1, 2, [3, 4], [5, 6, 7]]
print(anidada)

print("Acceder a elementos de la lista")
print(precios[0])
print(colores[-1])

print("Crud de listas")
colores.append("negro")
print("Despues de append:", colores)
colores.insert(1, "violeta")
print("Despues de insert en posicion 1:", colores)
colores.remove("azul")
print("Despues de remove 'azul':", colores)
print("Pop ultimo elemento:", colores.pop())
print("Lista final:", colores)
print("Longitud:", len(colores))
print("Esta 'rojo' en la lista?", "rojo" in colores)
colores.sort()
print("Ordenada:", colores)
