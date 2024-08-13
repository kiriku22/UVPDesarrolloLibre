print("Imprimamos la tabla del 4:")
for i in range(1,11):
    print("4x",i,"= ",4*i)


print("Ahora con la sentencia break")
for i in range(1,11):
    if(i==5):
        break  # Se termina el ciclo
    print("4x",i,"= ",4*i)
    

print("Ahora con la sentencia continue")
for i in range(1,11):
    if(i==5):
        continue #Se interrumpe la iteración actual
    print("4x",i,"= ",4*i)
   