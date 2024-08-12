print("Iterar sobre una lista: ----")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)


print("Iterar sobre un rango de números:----")
rango=range(1,6)
print("rango: ", rango)
rango=list(rango)
print("rango: ", rango)
for i in range(1, 6):
    print(i)

for i in range(0,5):
    print("Índice ",i,": ",lista[i])

print("Iterar sobre una cadena:----")
cadena = "Hola mundo"
for caracter in cadena:
    print(caracter)


print("Iterar sobre un diccionario:----")

diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(clave, valor)

print("Iterar sobre una lista y obtener el índice y el valor:----")

lista = ["a", "b", "c", "d", "e"]
for indice, valor in enumerate(lista):
    print(indice, valor)
