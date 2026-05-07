# Tupla: Colección ordenada e inmutable de elementos que permiten duplicados

# Indice         0           1           2      3
tecnologias = ("Python", "Javascript", "Go", "Python")

print(tecnologias)
print(tecnologias[1])

print(len(tecnologias))

print(type(tecnologias))
print()

# OJO: Una tupla de un solo elemento debe llevar coma, al final
#o sino lo toma como string en lugar de tupla
fruta = ("Manzana",)

print(type(fruta))
print()

# Tupla con distintos tipos de datos
tupla = ("Python", 5, True)

print("Tupla con distintos tipos de datos: ", tupla)
print(type(tupla))
print()


# Unpacking o desempaquetado de tuplas
x, y, z = tupla
print(x)
print(y)
print(z)
print()

tupla1 = (1,2,3)
tupla2 = (3,4,5)
print(f"tupla1: {tupla1} Tupla2: {tupla2}")
tupla3 = tupla1 + tupla2

print("Tupla3 = Tupla 1 + tupla2: ", tupla3)
print()

# Duplicar los datos de una tupla
tupla = ("Python", 5, True)
print(tupla * 2)
print()

for item in tupla:
    print(item)

print()
print("---------------")
print("Modificar una tupla")
print("""Como no se puede una sugerencia:
    1. Convertirla a lista (cast list())
    2. Modificar la lista (casttuple())
    3. Converetirla de nuevo en tupla""")

tuplaAModificar = ("Python", "Javascript", "Go")
print(f"Tupla: { tuplaAModificar }")
listaComodin = list(tuplaAModificar)
listaComodin.append("ReactJS")
print("Lista: ", listaComodin)
tuplaAModificar = tuple(listaComodin)

print("tupla modificada: ", tuplaAModificar)
print(type(listaComodin))
print(type(tuplaAModificar))