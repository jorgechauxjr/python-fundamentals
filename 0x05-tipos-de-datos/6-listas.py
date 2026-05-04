# LISTAS: Las listas son ordenadas, modificables y permiten valores duplicados

# Índices:   0          1           2            3
frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print(frutas)
print(type(frutas))

frutas[1] = "Banana"

print(frutas[1])
print(frutas)
# ["Manzana", "Banana", "Mandarina", "Naranja"]

print()

# Lista permite diferentes tipos de datos
lista = ["Sergie Code", 5, True]
print(lista)
print(type(lista))

print()
print(len(lista))
print(len(frutas))

print(frutas[1:])

#saber si un elemento existo dentro de la lista
print()
if "Manzana" in frutas:
    print("La manzana está dentro de las frutas")

# Indices      0        1       2
vehiculos = ["Auto", "Moto", "Avión"]
print()
print(vehiculos)

# Métodos 
# Append (agregar un elemento al final de la lista)
vehiculos.append("Barco") # Indice 3
print("append: ", vehiculos)

# Insert 
vehiculos.insert(1, "Bicicleta")
print("insert en posicion 1 bici: ", vehiculos)
print()

# Remove
vehiculos.remove("Auto")
print("remove AUTO: ", vehiculos)
print()

# Pop remueve pasando el indice
vehiculos.pop(1)
print("remover usando pop posicion 1: ", vehiculos)
print()

# Sort
vehiculos.sort()
print("ordenar alfabeticamente con sort(): ", vehiculos)
print()

# Reverse
vehiculos.reverse()
print("reverse(): ", vehiculos)
print()

# Unir listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

print(f"Coleccion 1: { coleccion1 } Coleccion 2: { coleccion2 }")

coleccion3 = coleccion1 + coleccion2
print("Unir dos listas OPCION 1: Concatenar coleccion 1 + coleccion 2")
print(f"Lista unida de col1 + col2: { coleccion3 }")
print()

print("Unir dos listas OPCION 2: modificar una de las dos listas con .extend()")
coleccion1.extend(coleccion2)
print("Coleccion1.extend(coleccion2): ", coleccion1)