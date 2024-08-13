import os
os.system ("cls")

#Un ejemplo de la sentencia if-elif-else
print ("Primero comparemos cual de entre tres números enteros es el mayor") 
a=int(input("Introduce a: "))
b=int(input("Introduce b: "))
c=int(input("Introduce c: "))
if a>b and a>c:
    print("a es el mayor")
elif b>a and  b>c:
    print("b es el mayor")
elif c>a and c>b:
    print("c es el mayor")
else:
    print("Ninguno es mayor que los otros dos")    

#Un ejemplo de la sentencia while
print ("Ahora obtengamos el promedio de  n números")
n=int(input("¿Cuántos números deseas promediar?: "))
if n>0:
    total=0
    i=1
    while i <n+1:
        print("Ingresa el dato",i,": ",end= "" )
        num=float(input())
        total=total+num
        i=i+1
    promedio=total/n  
    print("El promedio es: ",promedio) 
print("Hemos terminado de calcular el promedio")    

#Un ejemplo de la sentencia for
print ("Ahora obtengamos la mediana de  n números")
n=int(input("¿Cuántos números deseas ingresar?: "))
if n>0:
    datos=[]
    for i in range(1,n+1):
        print("Ingresa el dato",i,": ",end= "" )
        num=float(input())
        datos.append(num)
    print("Los datos ingresados son: ")
    for elemento in datos:
        print(elemento)   
    datos.sort()
    print("Los datos ingresados y ordenados son: ")
    for elemento in datos:
        print(elemento)
    print("La cantidad de datos es:",len(datos)) 

    
    if len(datos)%2==1 : #número de datos impar
        posMediana= (len(datos)+1)//2
        print("La mediana está en la posición:",posMediana) 
        print("El valor de la mediana es: ",datos[posMediana-1] )
    else:
        pos2= len(datos)//2
        pos1=pos2-1
        print("La mediana está en la posición:",pos2+0.5)
        mediana=(datos[pos1]+datos[pos2])/2
        print("El valor de la mediana es: ",mediana)
print("Hemos terminado de calcular la mediana")              





        
