estado = input("Estado del pedido (pendiente/enviado/entregado/cancelado): ")

match estado:
    case "pendiente":
        print("El pedido esta en cola de procesamiento")
    case "enviado":
        print("El pedido ya fue despachado")
    case "entregado":
        print("El pedido fue recibido por el cliente")
    case "cancelado":
        print("El pedido fue cancelado")
    case _:
        print(f"Estado desconocido: {estado}")


print("Match con condicionales")

calificacion = int(input("Ingrese la calificacion (0-100): "))
match calificacion:
    case n if n < 0 or n > 100:
        print("Calificacion fuera de rango")
    case n if n < 51:
        print(f"Reprobado con {n}")
    case n if n < 71:
        print(f"Aprobado con {n}")
    case n if n < 91:
        print(f"Bueno con {n}")
    case n:
        print(f"Excelente con {n}")
