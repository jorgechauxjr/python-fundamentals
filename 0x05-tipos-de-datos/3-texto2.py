"""
Slicing - Replace - Split
Para manipular strings en Python
"""

# indice 01234
texto = "Este es un texto"

print(texto[4])

# === Slicing ====

#Este
print("Este es un texto")
print("Slicing [0:3]")
print(texto[0:3])

# === Replace ====
curso = "Este curso es de Javascript"
print()
print(curso)
print("replace: 'Javascript' for 'Python'")
print(f"Resultado despues de replace: { curso.replace("Javascript", "Python") }")

# === Split ===

print()
tx1 = "Buenos dias a todo el mundo"
print(f"Texto normal: { tx1 }")

textoDividido = tx1.split(" ")
print(f"Dividido usando split: { textoDividido }")

# === Normalización ===

texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print()
print(f"Texto original: { texto2 }")

print("mayusculas" in texto2.lower())