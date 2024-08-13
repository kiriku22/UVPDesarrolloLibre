import S2_C8_Moda
X=[0,0,0,0,0,0,0,0,0,0]
Y=[0,0,0,0,0,0,0,0,0,0]
#La siguiente función se encarga de leer los 10 valores de cada vector
def leerVector():
    vector=[]
    for i in range(0,10):
        print("Ingresa el dato",i,": ",end= "" )
        num=float(input())
        vector.append(num)
    return vector 
#La siguiente función calcula la media de 10 datos
def media(vector):
    total=0
    for v in vector:
        total=total+v
    promedio=total/10
    return promedio  

#La siguiente función calcula la mediana de 10 datos
def mediana(vector):
    vector.sort()
    return (vector[4]+vector[5])/2

def ejecutarOpcion(opcion):
    global X
    global Y
    if opcion == 1:
        X=leerVector()
        print("Datos de X",X)
        print("")
    elif opcion == 2:
        Y=leerVector()
        print("Datos de Y",Y)
        print("")
    elif opcion == 3:
         print("Media de X:",media(X))
         print("Media de Y:",media(Y))
    elif opcion == 4:
         print("Mediana de X:",mediana(X))
         print("Mediana de Y:",mediana(Y))
    elif opcion == 5:
         print("Moda de X:",S2_C8_Moda.Moda(X))
         print("Moda de Y:",S2_C8_Moda.Moda(Y))
    elif opcion == 6:
        print("Saliendo...")
        print("")
    else:
        print("Opción incorrecta...")

opcion=0
while opcion!= 8:
    print("")
    print("----------------------------------------------------------------------")
    print("Este programa realiza las siguientes operaciones sobre los vectores X,Y")
    print("con 10 elementos cada uno :")
    print("1.Lectura del vector X.")
    print("2.Lectura del vector Y.")
    print("3.Media de X, media de Y.") 
    print("4.Mediana de X, mediana de Y.")
    print("5.Moda de X, moda de Y.")
    print("6.Salir")
    print("")
    opcion = int(input("Elige la opción de tu preferencia:>> "))
    print ("Seleccionaste: ",opcion)
    ejecutarOpcion(opcion)

 

