# Coleccion de pares clave calor (Ordenado a partir de Python 3.7)

carro = {
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}

print(carro)
print(carro["marca"])
print(carro.get("marca"))
print()

print("==KEYS AND VALUES==")
print(carro.keys())
print(carro.values())
print()

if "marca" in carro:
    print("Marca es una de las propiedades de este diccionario")

print()
print("MODIFICAR INFO")

carro["año"] = 2020
print(carro)

carro["color"] = "Verde"
print(carro)

print()
print("Modificar con update")

carro.update({"año": 2022, "puertas": 4})
print(carro)
print()

# carro.pop("puertas")
# print("POP PUERTAS===")
# print(carro)
# print()

# carro.popitem() # Elimina ultimo eleento del diccionario
# print("POP ITEM elimina el ultimo elemento del diccionario")
# print(carro)
# print()

# carro.clear() # Vaciar el diccionario
# print("CLEAR, vaciar el diccionario")
# print(carro)
# print()

print()
print("==== Recorrer carro e imprimir keys")

for k in carro: # keys
    print(k)

print("---------------------------")
print("Recorrer carro e imprimir values")
for v in carro.values(): # values
    print(v)

print("-------")
print("Recorrer carro e imprimir keys y values")
for k,v in carro.items(): # keys, value
    print(f"Key: {k} - Value: {v}")

# Diccionarios Anidados

familia = {
    "hijo1" : { 
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2" : { 
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3" : { 
        "nombre": "Marcelo",
        "edad": 6
    }
}

print()
print("==== Diccionarios anidados ====")
print(familia)
print()
print("Acceder a un valor interno del diccionario")
print(familia["hijo1"]["nombre"])
