x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

positivo = 5
negativo = -5

imaginario = 5 + 1j

# Casting
#obliga a x a comportarse como float

xf = float(x)

print("=========")
print(f"X: {x}")
print(f"tipo: {type(x)}")
print()
print(f"xf: {xf}")
print(f"tipo: {type(xf)}")

# float a int

ye = int(y)

print("=================")
print(f"y: {y}")
print(f"tipo: {type(y)}")
print()
print(f"ye: {ye}")
print(f"tipo: {type(ye)}")

# entero y float a complex

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print("=================")
print(f"entero complejo: {enteroComplejo}")
print(f"tipo: {type(enteroComplejo)}")
print()
print(f"Flotante complejo: {flotanteComplejo}")
print(f"tipo: {type(flotanteComplejo)}")

# Numeros Aleatorios

import random

print()
print(random.randrange(1, 10)) # Output random number between 1 and 10