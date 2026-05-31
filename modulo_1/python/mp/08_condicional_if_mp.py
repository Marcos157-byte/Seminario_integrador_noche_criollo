print("Condicionales if")

print("if simple")
bateria = 15
if bateria < 20:
    print("Bateria baja, conecta el cargador")

print("if else")
credito = 0
if credito > 0:
    print("Llamada permitida")
else:
    print("Sin credito disponible")

print("if multiples condicionales")
velocidad = 85
if velocidad < 0:
    print("Velocidad invalida")
elif velocidad > 120:
    print("Exceso de velocidad")
elif velocidad > 80:
    print("Velocidad elevada, precaucion")
else:
    print("Velocidad dentro del limite")

print("if condicionales anidados")
autenticado = True
rol_admin = False
if autenticado:
    if rol_admin:
        print("Acceso al panel de administracion")
    else:
        print("Acceso solo a modulos de usuario")
else:
    print("Debe iniciar sesion")

print("if con operadores logicos")
mayor_edad = True
tiene_dni = True
if mayor_edad and tiene_dni:
    print("Puede registrarse")

es_premium = False
tiene_cupon = True
if es_premium or tiene_cupon:
    print("Descuento aplicado")

suspendido = False
if not suspendido:
    print("Cuenta activa")
