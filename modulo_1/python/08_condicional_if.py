print("Condicionales if")

print("if simple")
stock=3
if stock > 0:
    print("Producto disponible")
print("if else .+- dos cambios")
saldo= 25
if saldo > 0:
    print("Compra permitida")
else:
    print("Saldo insuficiente")
print("if multiples condicionales")

temepratura=32
if temepratura < 0:
    print("Temperatura bajo cero")
elif temepratura > 30:
    print("Temperatura alta")
else:
    print("Temperatura normal")

print("if condicionales anidados")
conexion= True
toke_valido= True
if conexion:
    if toke_valido:
        print("Acceso a Api")
    else:
        print("Token invalido")
else:
    print("Sin conexion")

print("if con operadores logicos")
documento=True
pafgo=True
if documento and pafgo:
    print("Inscripcion Confirmada")
es_vip=False
tiene_invitacion=True

if es_vip or tiene_invitacion:
    print("Puede entrar al evento")

bloqueado=False
if not bloqueado:
    print("Usuario desbloqueado")


