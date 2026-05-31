print("Ciclo while")
intentos = 1
while intentos <= 3:
    print(f"Intento numero {intentos}")
    intentos += 1

respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe un comando (escribe 'salir' para terminar): ")
    print("Comando recibido:", respuesta)

cantidad = int(input("Cuantos productos vas a registrar: "))
total = 0
contador = 0
while contador < cantidad:
    precio = float(input("Ingrese el precio del producto: "))
    total += precio
    contador += 1
print("El total de la compra es:", total)
if total > 500:
    print("Califica para envio gratis")
else:
    print("No califica para envio gratis")
