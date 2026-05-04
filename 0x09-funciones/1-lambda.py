# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero sólo una expresión

# Sintaxis.
# La palabra 'lambda', los argumentos, dos puntos : y la expresión 
# lambda args: expresión

# x = lambda a : a + 10
# print(x(5)) # 15

# x = lambda a, b : a + b

# print(x(2,3)) # 5

"""
Una de las funciones mas importantes de esta función 
es la de Fabricar funciones
"""

def mifuncion(n):
    return lambda a : a * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

# print(duplicador(5)) # 10
# print(triplicador(5)) # 15

print(duplicador)