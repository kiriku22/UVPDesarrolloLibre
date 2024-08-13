print("Este programa divide dos números:")

try:
  a=float(input("Introduce a:"))
  b=float(input("Introduce b:"))
  c=a/b
  print("El resultado de la división es:", c)

except ValueError:
    print("Debes introducir dos valores numéricos")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
   


''' Algunas excepciones  comunes:
* TypeError: se produce cuando se realiza una operación con un tipo
de datos incorrecto. Por ejemplo, intentar sumar una cadena y un 
número.

* ValueError: se produce cuando se llama a una función o se realiza
una operación con un valor que no es válido para ese contexto. 
Por ejemplo, llamar a la función int() con una cadena que no representa un número.

* IndexError: se produce cuando se intenta acceder a un índice
  fuera del rango de una lista o una tupla.

* KeyError: se produce cuando se intenta acceder a una clave que
  no existe en un diccionario.

* FileNotFoundError: se produce cuando se intenta acceder a un 
  archivo que no existe en el sistema de archivos.

* ZeroDivisionError: se produce cuando se intenta dividir un 
  número por cero.

* AttributeError: se produce cuando se intenta acceder a un 
  atributo que no existe en un objeto.

* NameError: se produce cuando se intenta utilizar una variable 
  o una función que no ha sido definida previamente
'''
