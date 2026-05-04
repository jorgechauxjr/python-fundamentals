# Función: es un bloque de código que solo se ejecuta cuando la llamamos. Permiten organizar y modularizar el código (reutilización)

def saludar(nombre: str, nacionalidad: str ="Colombia"): # Argumentos
    """
    Saluda a una persona

    Args:
        nombre (string): El nombre de una persona.
        nacionalidad (string): El país donde nació.

    Returns:
        void
    """
    print(f"Hola {nombre} de {nacionalidad}")
    # print("Hola", nombre,"de", nacionalidad)

# para ver la info de la funcion. la info que escribi en los comentarios.
#print(help(saludar))

saludar("Pedro", "España") # Parámetros
saludar("María")
saludar("Ana")

# def sumar(a,b):
#     """
#     Suma dos números

#     Args:
#         a (int): El nombre de una persona.
#         b (int): El país donde nació.

#     Returns:
#         La suma de los dos numeros
#     """
#     return a + b


# resultado = sumar(2,3)
# print(resultado)

# def funcion():
#     pass

# def restar(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     return a/b