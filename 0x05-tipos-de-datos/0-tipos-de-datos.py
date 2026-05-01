# == Variables de tipo texto(string) ==
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = '''Comillas triples'''
# las triples tambien se pueden con las dobles

print(comillasSimples)
print(comillasDobles)
print(comillasTriples)

# == Variables de tipo numero ==
a = 1
#float
b = 3.14

c = 5 + 2j

print(a)
print(b)
print(c)

# == Variables de tipo List ==
# Mutable
lista  = [0, 1, 2, 3, 4, 5]
print(f"Lista: { lista }")

# == Variables de tipo Tupla ==
# Inmutable
tupla = ("a", "b", "c")
print(f"Tupla: { tupla }")

# Diccionario
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"Diccionario { diccionario }")

# Conjuntos - Sets
# colección desordenada, mutable y elementos únicos
# --> Los elementos repetidos se ignoran 

conjunto = { 1, 1, 2, 2, 3 } # Output: {1, 2, 3} 
print(f"Conjunto - Set: { conjunto }")

# Boolean
booleanoVerdadero = True
booleanoFalso = False