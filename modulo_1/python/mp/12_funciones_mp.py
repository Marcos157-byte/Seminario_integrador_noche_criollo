print("Funciones en python")
print("funcion basica")

def mostrar_bienvenida():
    print("Bienvenido al sistema de ventas")

mostrar_bienvenida()

print("Funcion con parametros")

def mostrar_producto(nombre):
    print(f"Producto disponible: {nombre}")

mostrar_producto("Laptop")
mostrar_producto("Smartphone")

print("Funcion que devuelve con return")

def calcular_total(precio, cantidad):
    return precio * cantidad

print(calcular_total(15.50, 3))

print("Funcion por posicion y por nombre")

def registrar_venta(cliente, producto, monto):
    print(f"Cliente: {cliente} | Producto: {producto} | Monto: ${monto}")

registrar_venta("Ana Torres", "Mouse", 25)
registrar_venta("Luis Gomez", "Teclado", 45)
registrar_venta(monto=350, producto="Monitor", cliente="Sofia Ruiz")

print("Funcion con valores por defecto")

def enviar_mensaje(destinatario, asunto="Sin asunto", prioridad="normal"):
    print(f"Para: {destinatario} | Asunto: {asunto} | Prioridad: {prioridad}")

enviar_mensaje("carlos@mail.com", "Factura pendiente", "alta")
enviar_mensaje("ana@mail.com", prioridad="baja")

print("Funcion que devuelve diccionario")

def resumen_ventas(montos):
    total = sum(montos)
    n = len(montos)
    return {
        "total": total,
        "promedio": total / n if n > 0 else 0,
        "mayor_venta": max(montos) if montos else None,
        "menor_venta": min(montos) if montos else None
    }

ventas = [120, 450, 30, 780, 95]
reporte = resumen_ventas(ventas)
print("Total:", reporte["total"])
print("Promedio:", reporte["promedio"])
print("Mayor venta:", reporte["mayor_venta"])
print("Menor venta:", reporte["menor_venta"])
