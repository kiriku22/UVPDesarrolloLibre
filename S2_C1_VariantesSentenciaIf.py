
#Este programa compara tres números
print("Este programa determina cual de 3 números es mayor")
A= int(input("Introduce el número A: "))
B= int(input("Introduce el número B: "))
C= int(input("Introduce el número C: "))
if A>B and A>C:
   print("El mayor es A")
if B>A and B>C:
   print("El mayor es B") 
if C>A and C>B:
   print("El mayor es C")
if A==B and A==C:
   print("Los tres son iguales")
if (A==B and A>C) or (B==C and B>A) or(A==C and A>B):  
   print("Ninguno es mayor que los otros dos") 
   
#Este programa compara tres números

print("Este programa determina cual de 3 números es mayor")
A= int(input("Introduce el número A: "))
B= int(input("Introduce el número B: "))
C= int(input("Introduce el número C: "))
if A>B:
   if A>C:
      print("El mayor es A")
   else:
      if C>A:
        print("El mayor es C")
      else:
        print("Ninguno es mayor que los otros dos")  
      
else:
   if B>A:
       if B>C:
          print("El mayor es B")
       else:
          if C>B:
             print("El mayor es C")
          else: 
             print("Ninguno es mayor que los otros dos")  
   else:
       if C>A:
            print("El mayor es C")
       else:
          if C==A:      
             print("Los tres son iguales")      
          else:
             print("Ninguno es mayor que los otros dos") 


#Este programa compara tres números
print("Este programa determina cual de 3 números es mayor")
A= int(input("Introduce el número A: "))
B= int(input("Introduce el número B: "))
C= int(input("Introduce el número C: "))
if A>B:
   if A>C:
      print("El mayor es A")
   elif C>A:
        print("El mayor es C")
   else:
        print("Ninguno es mayor que los otros dos")  
      
elif B>A:
   if B>C:
        print("El mayor es B")
   elif C>B:
        print("El mayor es C")
   else: 
        print("Ninguno es mayor que los otros dos")  
else:
   if C>A:
        print("El mayor es C")
   elif C==A:      
        print("Los tres son iguales")      
   else:
        print("Ninguno es mayor que los otros dos") 

#Este programa compara tres números
print("Este programa determina cual de 3 números es mayor")
A= int(input("Introduce el número A: "))
B= int(input("Introduce el número B: "))
C= int(input("Introduce el número C: "))
if A>B and A>C:
   print("El mayor es A")
elif B>A and B>C:
   print("El mayor es B") 
elif C>A and C>B:
   print("El mayor es C")
elif A==B and A==C:
   print("Los tres son iguales")
else:  
   print("Ninguno es mayor que los otros dos") 
