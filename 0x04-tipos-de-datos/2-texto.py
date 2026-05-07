print("Hola 'mundo'")

ingles = "I'm Juan"

multiplesLineas = """Hola
mundo
desde
las
comillas
triples"""

print(ingles)
print(multiplesLineas)

# método len

palabra = "murcielago"
print("==============")
print("metodo len()")
print(f"La palabra { palabra } tiene { len(palabra) } caracteres.")

# metodo in text para saber si una palabra está incluida
# Diferencia mayusculas de minusculas

texto="'Curso de fundamentos de Python'"
palabra = "Python"
estaIncluida = palabra in texto
print()
print("metodo 'in'")
print(f"La palabra '{ palabra }' está incluida en { texto }?: { estaIncluida }")

# No está incluida
noEstaIncluida = "JavaScript" not in texto
print(noEstaIncluida)

# mayuscula o minuscula
mayuscula = texto.upper()
print("Mayuscula: ", mayuscula)

minuscula = texto.lower()
print("minuscula", minuscula)

# Espacios al comienzo y final del texto
espacios = "        Este es el texto con espacios    "
print(f"Espacios: { espacios }")

sinEspacios = espacios.strip()
print(f"Ignorar espacios: '{ sinEspacios }' SIN ESPACIOS")

# Se puede usar para usuario y contraseña
# donde los usuarios pueden dejar espacios sin querer