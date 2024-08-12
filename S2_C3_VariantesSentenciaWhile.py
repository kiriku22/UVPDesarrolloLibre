  
# Iterar sobre una lista:
print("Iterar sobre una lista:")
lista = [1, 2, 3, 4, 5]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

# Iterar sobre un rango de números:
print("Iterar sobre un rango de números:")
rango = range(1, 6)
i = 0
while i < len(rango):
    print(rango[i])
    i += 1

# Iterar sobre una cadena:
print("Iterar sobre una cadena:")
cadena = "Hola mundo"
i = 0
while i < len(cadena):
    print(cadena[i])
    i += 1

# Iterar sobre un diccionario:
print("Iterar sobre un diccionario:")
diccionario = {"a": 1, "b": 2, "c": 3}
claves = list(diccionario.keys())
valores = list(diccionario.values())
i = 0
while i < len(claves):
    print(claves[i], valores[i])
    i += 1

# Iterar sobre una lista y obtener el índice y el valor:
print("Iterar sobre una lista y obtener el índice y el valor:")
i = 0
while i < len(lista):
    print("Índice", i, ":", lista[i])
    i += 1
