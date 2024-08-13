print("TUPLAS ----------------------------------------------------------------")
#Las tuplas son útiles cuando se desea almacenar una colección de valores
#que no cambian, es decir,no se pueden agregar, eliminar o cambiar sus elementos
#Las identificamos porque se definen mediante  paréntesis ( )
# Algunos comandos con tuplas:
tupla1=(1, 'A', 'Hola', 3.1416, 2, False)
tupla2=('alfa', 'alfa', 100, "hoy es sábado",'alfa')

print("Los elementos de la tupla1 son:")
for elemento in tupla1:
  print (elemento) # ¡Debemos respetar la indentación o sufriremos!
print("El índice del valor 2, en la tupla 1 es:" ,tupla1.index(2))
print("El elemento en la posición 3 de tupla2 es:" ,tupla2[3])
print("Concatenando dos tuplas:")
tupla3=tupla1+tupla2
print(tupla3)
print("Duplicando la tupla1:",tupla1*2)
print("Contamos las repeticiones del elemento <alfa> en la tupla 2: " ,tupla2.count('alfa'))
print("El siguiente comando (comentado) genera un error:")
#tupla2[2]=5  

print("LISTAS ----------------------------------------------------------------")
#Similares a las tuplas, pero sí pueden cambiar su valores
#Las identificamos porque se definen mediante  corchetes [ ]
# Algunos comandos con listas
lista1= list(tupla1) #Es posible crearlas a partir de una tupla
lista2= list(tupla2)
lista3=[6,9,2,4,1,8]
print("lista1:", lista1)
print("lista2:", lista2)
print("lista3:", lista3)
print("Los elementos de la lista1 son:")
for elemento in lista1:
  print (elemento)

print("El elemento en la posición 3 de lista2 es:", lista2[3])
print("Concatenando dos listas:", lista1+lista2)
print("Duplicando la lista1:", lista1*2)
print("El índice del valor 2, en la lista 1 es:" ,lista1.index(2))
print("Contamos las repeticiones del elemento <alfa> en la lista 2:" ,lista2.count('alfa'))
print("Las listas sí se pueden modificar:")
lista2[2]=5
print(lista2)

print("Aplicamos el operador de pertenencia <in>:")
print("¿3.1416 in lista1?:",3.1416 in lista1) 
print("¿3.1417 in lista1?:",3.1417 in lista1) 
print("Agregamos un elemento adicional a la lista 1, denominado <nuevo>:")
lista1.append('nuevo') 
print(lista1)
print("Insertamos el  elemento <c> en la lista 2, en la posición 3:")
lista2.insert(3,'c')   
print(lista2)

print("Podemos obtener la cantidad de elementos de la lista2:", len(lista2)) 
print("Eliminamos el elemento en la posición 1 de la lista 2:")
del(lista2[1])  
print(lista2)

print("También podemos eliminar elementos por su contenido:")
lista2.remove('alfa')  
print(lista2)

print("Imprimimos la lista3: ", lista3)
print("La imprimos en forma ordenada:",sorted(lista3))  
print("Ahora en orden inverso:",sorted(lista3, reverse=True))

print("MATRICES ----------------------------------------------------------------")
# En Python, una matriz se puede definir utilizando una lista de listas.
# Cada lista interna representa una fila de la matriz y cada elemento de la lista
# representa un elemento de la fila.
matriz= [ [1,2,3], [4,5,6]]
print("matriz= ",matriz)
print("Accediento a l elemento matriz[0][1]:",matriz[0][1]) 

print("DICCIONARIOS ----------------------------------------------------------------")
# Son estructuras de datos que permite almacenar y acceder a pares de clave-valor
# Se definen utilizando llaves { } o la instrucción dict con paréntesis
# Los pares de clave-valor se separan con comas
# Cada clave debe ser única y los valores pueden ser de cualquier tipo de datos

# Algunos comandos con diccionarios

diccionario1={ 'a': 1, 'b': 2, 'c': 3}
diccionario2= dict(A=10,B=20,C=30)

print("diccionario1:",diccionario1)
print("diccionario2:",diccionario2)
# Obtengamos un valor:
print("diccionario1 ['c']:",diccionario1 ['c'])
# Modifiquemos un valor
diccionario1 ['b'] = 28
# agreguemos un valor
diccionario1 ['d'] = 45
print("diccionario1:",diccionario1)

print("Una forma más completa de imprimir un diccionario:")
for clave,valor in diccionario1.items():
  print("Clave={0}, valor={1}".format(clave,valor))

print("Imprimamos las claves del diccionario2:")
for clave in diccionario2.keys():
  print("Clave={0}".format(clave))

print("Imprimamos los valores del diccionario2:")
for valor in diccionario2.values():
  print("Valor={0}".format(valor))

#En el ejemplo siguiente, "estudiantes" es un diccionario que contiene cuatro pares
# clave-valor, donde cada clave es el nombre del estudiante y cada valor es otro 
# diccionario que contiene la edad y el promedio de calificaciones

estudiantes = {
    "Juan": {"edad": 22, "promedio": 9.5},
    "María": {"edad": 23, "promedio": 8.2},
    "Pedro": {"edad": 20, "promedio": 8.7},
    "Luisa": {"edad": 21, "promedio": 7.3}
}
print("estudiantes:", estudiantes)
#Podemos acceder a la información de un estudiante específico utilizando
#su nombre como clave:
print("estudiantes[\"Juan\"]:",estudiantes["Juan"]) 

#Accedamos ahora a la información específica de un estudiante
print("estudiantes[\"María\"][\"edad\"]: ",estudiantes["María"]["edad"])
print("estudiantes[\"Pedro\"][\"promedio\"]:",estudiantes["Pedro"]["promedio"])

print("CADENAS ----------------------------------------------------------------")
# Ejemplos de operaciones básicas con cadenas en Python

# Declaración de cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
print("cadena1: ", cadena1)
print("cadena2: ", cadena2)

# Concatenación de cadenas
concatenada = cadena1 + " " + cadena2
print("Concatenación:", concatenada)

# Longitud de la cadena
longitud = len(concatenada)
print("Longitud:", longitud)

# Acceso a caracteres individuales
primer_caracter = concatenada[0]
ultimo_caracter = concatenada[-1]
print("Primer carácter:", primer_caracter)
print("Último carácter:", ultimo_caracter)

# Subcadenas
subcadena = concatenada[1:4]  # Desde el índice 1 hasta el 3
print("Subcadena [1:4]:", subcadena)

# Conversión a mayúsculas y minúsculas
mayusculas = concatenada.upper()
minusculas = concatenada.lower()
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)

# Reemplazo de subcadenas
reemplazada = concatenada.replace("Mundo", "Python")
print("Reemplazo de 'Mundo' por 'Python':", reemplazada)

# Búsqueda de subcadenas
indice_mundo = concatenada.find("Mundo")
print("Índice de 'Mundo':", indice_mundo)

# División de cadenas
dividida = concatenada.split(" ")
print("División por espacio:", dividida)

# Unión de cadenas
unida = "-".join(dividida)
print("Unión con '-':", unida)

# Eliminación de espacios en blanco
cadena_con_espacios = "  Hola Mundo  "
sin_espacios = cadena_con_espacios.strip()
print("Sin espacios al inicio y al final:", sin_espacios)

# Verificación de prefijo y sufijo
empieza_con = concatenada.startswith("Hola")
termina_con = concatenada.endswith("Mundo")
print("¿Empieza con 'Hola'?:", empieza_con)
print("¿Termina con 'Mundo'?:", termina_con)

# Formateo de cadenas
nombre = "Juan"
edad = 22
formateada = f"Mi nombre es {nombre} y tengo {edad} años."
print("Formateo de cadena:", formateada)
