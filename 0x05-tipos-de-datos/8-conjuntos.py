# Conjunto (set): Colección no ordenada de elementos únicos (no se puede accede por índice)

# No se permiten elementos repetidos.
frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print(len(frutas)) # 3 no cutro porque naranja esta repetido y no se cuenta.

print("Manzana" in frutas)
print("Pera" not in frutas)
print()

# Puede tener distintos tipos de datos
deTodo = {"Python", 15, True}
print("Un set puede tener distintos tipos de datos: ", deTodo)
print(type(deTodo))

# Recorrer un conjunto
print("Recorrer un set") # El print se muestra en diferente orden
for item in deTodo:
    print(item)

# Agregar
# Add
print()
print("agregar pera")
frutas.add("Pera")
print(frutas)
print()

# Update
frutasTropicales = { "Piña", "Mango"} 
frutas.update(frutasTropicales) # Agregar listas, tuplas, conjuntos
print("Agregar varios elementos, en este caso otro Set de piña mango con .update()")
print(frutas)
print()

# Eliminarlos
#Remove
frutas.remove("Mango")
print("REMOVE Mango")
print(frutas)

#Discard
frutas.discard("Banana")
print(frutas)
# Pop
frutas.pop()
print()
print("POP")
print(frutas)
# Clear
frutas.clear()
print("CLEAR")
print(frutas)

# conjuntos = {"Python", 156, True}
# print(conjuntos)
# print(type(conjuntos))

# for item in conjuntos:
#     print(item)

print()
print("--------------")

# OPERACIONES ENTRE CONJUNTOS (SETS)
a = {"a", "b", "c"}
b = {"c", "d", "e"}
print(f"Conjunto A {a} Conjunto B {b}")

c = a.union(b)
print("UNION ", c)
print()

i = a.intersection(b)
print("INTERSECCIÓN ", i)
print()

d = a.difference(b)

print("DIFERENCIA ", d)