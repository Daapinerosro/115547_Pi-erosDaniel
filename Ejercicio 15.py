



"punto 15"
cad=(int)(input('Cantidad de digitos son ')) 
lista=[] # se guerda la cantidad de elementos a instrudicr por cad
for i in range(cad):
    lista.append(input('introduzca el numero'+str(i+1)+':'))

lis=[]
for i in range(len(lista)):#itera para reconocer las veces que se repite 2 
    #un numero
    a=lista.count(lista[i])
    if (a==2):
        cadena='el numero '+lista[i]+' se repite 2 veces en la lista'
        if cadena not in lis:
            lis.append(cadena)
            print('entra')
            
for i in range(len(lis)):
    print(lis[i])