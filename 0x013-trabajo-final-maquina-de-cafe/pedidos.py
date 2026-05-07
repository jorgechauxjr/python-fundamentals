ARCHIVO_PEDIDOS = "pedidoss.txt"

def pedir_cafe():
    print("\nElige el café que prefieras: ")
    print("1 Espresso")
    print("2 Capuccino")
    print("3 Latte")
    print("4 Americano")

    opcion = input("Opción: ")

    cafes = {
        "1": "Espresso",
        "2": "Capuccino",
        "3": "Latte",
        "4": "Americano"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print(f"===== Has pedido un { cafe_elegido }. Preparando tu café! =====")
        
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("===== La opción no es valida. Por favor intenta de nuevo. =====")