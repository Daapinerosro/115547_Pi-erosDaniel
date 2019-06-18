print("Programación para la ingeniería Civil_Tarea_Daniel_Piñeros ")
print("DE 1 a 100, los primeros 15 multiplos de 3 y los siguientes que sean multiplos de 4")

cont=0
for g in range(0,100):
    if cont<=15:
        i=g%3
        if i==0:
            cont=cont+1
            print("El",g,"es un número multiplo de 3")
            
    else:
        q=g%4;
        if q==0:
            print("El",g,"es un número multiplo de 4")
            