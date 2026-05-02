v = True
f = False 

print(v)
print(f)

print()
print(f"5 > 3: { 5 > 3 }") # Verdadero
print(f"3 > 5: { 3 > 5 }") # Falso
print()

# Type
print(f"Type true: { type(v) }")
print()

# === Casting ===
print("casting 'Hola Mundo' a bool():", bool("Hola Mundo"))
print(bool("")) # Como este string NO tiene contenido da 'false'
print()

# True
# strings, numeros y listas dan true al castear

print("strings, numeros y listas dan true al castear")

print(f"bool(abc): {bool("abc")}")
print("bool(123): ", bool(123))
print('bool(["Manzana", "Pera"]): ', bool(["Manzana", "Pera"]))
print()

# False
print("datos que dan 'false' al castear")
print("bool(''): ", bool(""))
print("bool(0): ", bool(0))
print("bool([]): ", bool([]))
print("bool(None): ", bool(None))

x = 123.5
print(f"Muiestra si { x } is instance of int: { isinstance(x, int) }")