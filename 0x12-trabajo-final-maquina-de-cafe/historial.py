import os

# 1. Obtenemos la ruta de la carpeta donde vive este script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

# 2. Unimos esa ruta con el nombre del archivo
ARCHIVO_PEDIDOS = os.path.join(DIRECTORIO_ACTUAL, "pedidos.txt")

def ver_historial():
    try:
        print("\n -- Historial de pedidos --")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                # print(pedidos) # ['Americano\n', 'Capuccino\n']
                for i, pedido in enumerate(pedidos, start=1):
                    print(f"{i} {pedido.strip()}")
                    # print(str(i) + "." + pedido.strip())
            else:
                print("Aún no hay ningún pedido!")
    except FileNotFoundError:
        print("\nTodavía no existe un historial de pedidos")


# Imprimir el historial sin indice, sin los numeros.
"""
def ver_historial():
    try:
        print("\n -- Historial de pedidos --")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                # print(pedidos) # ['Americano\n', 'Capuccino\n']
                for pedido in pedidos:
                    print(pedido.strip())
    except FileNotFoundError:
        print("\nTodavía no existe un historial de pedidos")
"""