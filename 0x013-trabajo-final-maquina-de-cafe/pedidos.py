def pedir_cafe():
    print("\n Elige el café que prefieras: ")
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