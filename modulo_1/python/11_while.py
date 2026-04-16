print("Ciclo while")
contador=1
while contador <=5:
    print(contador)
    contador +=1

dato=""
while dato!="salir":
    dato=input("Ingrese un dato (escriba 'salir' para terminar): ")
    print("Dato ingresado:", dato)

cantidad= int(input("Ingrese la cantidad para el descuento: "))
total=0
contador=0
while contador <= cantidad:
    numero= float(input("Ingrese un numero: "))
    total += numero
    contador +=1
print("La suma total es:", total)
if total > 100:
    print("La suma es mayor a 100")
else:
    print("La suma es menor o igual a 100")