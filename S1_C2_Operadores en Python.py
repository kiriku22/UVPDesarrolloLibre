#En este script se presentan los tipos de operadores en Python.


#Operadores aritméticos: se utilizan para realizar operaciones matemáticas,
# suma (+)
# resta (-)
# multiplicación (*)
# división (/)
# módulo (%)
# división entera (//)
# exponenciación (**)

a=5
b=2
print("<< Operadores aritméticos >>")
print("Suma: a+b es ", a+b)
print("Resta: a-b es ", a-b)
print("Multiplicación:  a*b es ", a*b)
print("División: a/b es ", a/b)
print("División entera a//b es ", a//b)
print("Exponenciación: es ", a**b)
print("")


# Operadores de comparación: se utilizan para comparar dos valores y devolver un
# valor booleano True o False. 
# igual a (==)
# distinto de (!=)
# menor que (<)
# mayor que (>)
# menor o igual que (<=)
# mayor o igual que (>=)
print("<< Operadores relacionales o de comparación >>")
print("¿Es a igual a b?: ", a==b)
print("¿Es a distinto a b?", a!=b)
print("¿Es a menor que b?", a<b)
print("¿Es a mayor que b?", a>b)
print("¿Es a mayor o igual que b?", a>=b)
print("¿Es a menor o igual que b?", a<=b)
print("")


#Operadores lógicos: se utilizan para combinar expresiones booleanas y devolver un
# valor booleano True o False. Los operadores lógicos incluyen and, or y not.
c=10
print("<< Operadores lógicos >>")
print("¿Es a mayor que b, y mayor que c?", a>b and a>c)
print("¿Es a mayor que b, o mayor que c?", a>b or a>c)
print("¿Es a mayor que b, y no mayor que c?", a>b and (not a>c))
print("")

# Operadores de asignación: se utilizan para asignar un valor a una variable.
# Los operadores de asignación incluyen el signo igual (=), así como los operadores de
# asignación compuesta, como +=, -=, *=, /=, %= y //=.
print("<< Operadores de asignación >>")
print("Asignar a la variable a el valor de c: ")
a=c
print("Ahora a es: ",a)

print("Incrementar a en 3: ")
a+=3 #Equivale a:  a= a+3
print("Ahora a es: ",a)

print("Decrementar a en 2:")
a-=2 #Equivale a:  a= a-2
print("Ahora a es: ",a)

print("Mutiplicar a por 4")
a*=4 #Equivale a:  a= a*4
print("Ahora a es: ",a)

print("Dividir a entre  2")
a/=2 #Equivale a:  a= a/2
print("Ahora a es: ",a)

print("Asignar a la variable a el resto de su división entre 3")
a%=3 #Equivale a:  a= a%3
print("Ahora a es: ",a)

print("División entera de c entre 4")
c//=4  #Equivale a:  c= c//4
print("Ahora c es: ",c)
print("")

# Operadores de pertenencia: se utilizan para comprobar si un valor está presente
# en una secuencia o en un conjunto, y devolver un valor booleano True o False.
# Los operadores de pertenencia incluyen in y not in.
print("<< Operadores de pertenencia >>")
d = [1, 2, 3]

print("¿b está contenido en d?: ",b in d)  # True
print("¿4 está contenido en d?: ",4 in d)  # False
