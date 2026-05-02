# Operadores aritméticos

x = 5
y = 12

print("numeros 5 y 12")

# Suma + 
print("Suma", x + y)

# Resta -
print("Resta", x - y)

# Multiplicación *
print("Multiplicación", x * y)

# División / (retorna un float)
print("División", y / x)

# Módulo %
print("Módulo(residuo)", y % x)

# Potencia **
print("Potencia", y ** x) # 10 * 10 * 10 *10 *10

# División entera //
print("División Entera", y // x)

# El modulo se puede usar para saber si un número es par
par = 7
print(par % 2 == 0)

# === Precedencia de operadores ===
"""
Orden en el que va a ser ejecutado por Python
- Paréntesis
- Exponentes
- Multiplicaciones, divisiones, divisiones enteras y residuos
- Sumas y restas
- Comparaciones de identidad y pertenncia
- Lógicos
"""