"Leer una lista de números ya ordenados de forma ascendente \
y verificar que dicha lista está ordenada. \
Luego, leer un número e insertarlo en la lista \
en la posición que le corresponde a dicho número."

numero=int(input("ingresa la lista de manera ordenada ascendente"))#Número para operar
if (numero>=0):
    lista=[]#Listas para uiliar
    lis=[]
    lix=[]
    conteo=0
   #Conteo necesario para ciclo while, para pasar mi número a una lista
    while(numero>=10):
        residuo=numero%10
        lista.append(residuo)
        numero=numero//10
        conteo=conteo+1
    
    lista.append(numero)
        # cuando acabe el ciclo, no habra ningun residuo y el 
        #número que quede se guarda en la lista 
reves=0
for i in range (0,conteo+1):
    
    reves=lista[i]*10**(conteo-(conteo-i))+reves
    if (numero>0):
        f=(reves)
    else:
        f=(-reves)
        
        
lix=sorted(lista)
print("la lista ingresada ya ordenada  es",lista[::-1])
lix.reverse()
print("Verificar los números ordenados ascendentes son")
print(lix)

a=int(input("ingrese un número para agregar a la lista "))
lista.extend([a])
lis=sorted(lista)
lis.reverse()
print("Verificar, después de agregar el número el orde queda así")
print(lis)

