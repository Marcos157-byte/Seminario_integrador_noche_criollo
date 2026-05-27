comando= input("Comando iniciar/parar/reiniciar: ")

match comando:
    case "iniciar":
        print("Iniciando el sistema")
    case "parar":
        print("Parando el sistema")
    case "reiniciar":
        print("Reiniciando el sistema")
    case _:
        print(f"Comando no reconocido: {comando}")


print("Match con condicionales")

numero= int(input("Ingrese un numero: "))
match numero:
    case n if n<0:
        print("Numero negativo")
    case 0:
        print("Numero cero")
    case n if n%2==0:
        print(f"el numero {n} es positivo y par")
    case n:
        print(f"el numero {n} es positivo e impar")