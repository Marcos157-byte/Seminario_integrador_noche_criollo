print("Funciones en python")
print("funcion basica")
def saludar():
    print("Hola desde Ute")
saludar()

print("Funcion con parametros")

def saludarConNombre(nombre):
    print(f"Hola: {nombre}, Que tal?")

saludarConNombre("John")
saludarConNombre("Maria")

print("Funcion que devuelve con return")

def sumar(a, b):
    return a + b
print(sumar(5,1))

print("Funcion po posicion por nombre")

def presentar(nombre, edad,ciudad):
    print(f"Señor(a): {nombre, edad: {edad}, ciudad: {ciudad}}")

presentar("Maria",26,"Quito")
presentar("Carla",30,"Guayaquil")
presentar(edad=22, ciudad="Cuenca", nombre="Luis")

print("Funcion con valores de parametros por defecto")

def  saludo_con_valores(nombre, saludo="Hola", puntiacion="!"):
    print(f"{saludo} {nombre}{puntiacion}")
saludo_con_valores("Pedro", "Buenas noches", "...")
saludo_con_valores("Juan", puntiacion="...")


print("Funcion con parametros posicionales")
print("Devolver diccionario en el caso de muchos valores")

def analizar(numeros):
    total = sum(numeros)
    n=len(numeros)
    return{
        "total": total,
        "media": total/n if n>0 else 0,
        "maximo": max(numeros) if numeros else None,
        "minimo": min(numeros) if numeros else None
    }

datos =[12,334,2,3,4453,3,2,3]
stats = analizar(datos)
print("Total:", stats["total"])
print("Media:", stats["media"])
print("Máximo:", stats["maximo"])
print("Mínimo:", stats["minimo"])