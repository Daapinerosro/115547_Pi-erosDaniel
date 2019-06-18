numero=int(input("escribe el número "))#Número para operar
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
    lista_copia = list(lista)# Se hace una copia para que no que borren números que no
# estan repetidos 
    for i in lista_copia:# se toman decisiones para que los números repetidos se 
    # guarden en lista: lix
        if i  not in lis:
            lis.append(i)
        else:
            lix.append(i)
    print("Los numeros removidos por repetición, son",lix[::-1])
    
    lisa=[]
# se hace el mismo proedimiento que atras, pero en este caso se guardan 
# los números repetidos en una lista donde sólo esten los representantes de 
# los dígitos repetidos
    lix_copia= list(lix)
    for j in lix_copia:
        if j not in lisa:
            lisa.append(j)
        else:
            lix.remove(j)
        
    if (len(lisa)>0):# Si hay dígitos repetidos, imprimirlos
        print("los dígitos que se repitieron en el número\
     son",lisa[::-1])
    else:# si no los hay decirlo 
        print("No hay números repetidos")
else:
    print("no es un numero entero positivo")