print("Ciclos for")
print("for clasico")
for i in range(1,6):
    print(i)

print("for con lista")
nombres= ["Marcos", "Lucia", "Sofia", "Matias"]
for nombre in nombres:
    print(nombre)
print("control de interacion")
for i in range(1,10):
    if i==2: continue
    if i==7: break
    print(i)
else:
    print("Terminado el ciclo for")

print("for con range step")
for i in range(1,10,2):
    print(i)

print("for regresivo")
for i in range(10,0,-1):
    print(i)

print("for con enumerate")
nombres = ["Marcos", "Lucia", "Sofia", "Matias"]
for i, nombre in enumerate(nombres):
    print(f"Índice: {i}, Nombre: {nombre}")

print("for con zip")
nombres = ["Marcos", "Lucia", "Sofia", "Matias"]
edades = [25, 30, 22, 28]
for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad}")

print("for anidados")
for i in range(1,4):
    for j in range(1,4):
        print(f"i: {i}, j: {j}")