from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while(True):
        mostrar_menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            pedir_cafe()
            pass
        elif option == "2":
            ver_historial()
            pass
        elif option == "3":
            print("\n Muchas gracias por haber tomado nuestros cafés")
            break
        else:
            print("Opcion invalida, por favor indique una de las opciones sugeridas")

if __name__ == "__main__":
    main()