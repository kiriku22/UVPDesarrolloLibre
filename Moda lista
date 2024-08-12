def Moda(lista):
    # Crear un diccionario para contar las ocurrencias de cada elemento
    conteo = {}
    
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    
    # Encontrar la frecuencia máxima
    max_frecuencia = 0
    for frecuencia in conteo.values():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
    
    # Encontrar todos los valores que tienen la frecuencia máxima
    modas = []
    for valor,frecuencia in conteo.items():
        if frecuencia== max_frecuencia:        
            modas.append(valor) 
    
    return modas

list=[1,2,3,4,1,3,5]

print(Moda(list))


