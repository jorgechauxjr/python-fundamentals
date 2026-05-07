# open(nombre, modo)

# R (read) Lectura 
# W (write) Escritura 
# X (Crea archivo nuevo)
# A append

# Esta forma se abre y cierra el archivo.
"""
try:
    f = open("archivo.txt", "r")
    print(f.readline)
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo") 
"""

# Abre y cierra automaticamente con with.
# f de la abreviatura de file

#Leer un archivo
# En el except se crea el archivo si no existe.
# Luego pasa por el codigo de # Escritura

#Comentar L32 para ver otros casos de uso

try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("No se ha encontrado el archivo")

# Escritura

try:
    with open("archivo.txt", "a") as f:
        f.write("\n")
        f.write("Hola mundo desde el VS CODE")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")