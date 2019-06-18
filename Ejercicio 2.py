
lista=[]
numero=(int)(input("digite el número"))
num=int(((numero)**2)**0.5)
conteo=0
while(num>=10):
    residuo=num%10
    lista.append(residuo)
    if(num==0):
        num=num+10
        num=num//10 
        conteo=conteo+1
    else:
        num=num//10 
        conteo=conteo+1
    
lista.append(num)

reves=0
for i in range (0,conteo+1):
    
    reves=lista[i]*10**(conteo-i)+reves
    if (numero>0):
        f=(reves)
    else:
        f=(-reves)

print("El número al reves es",f)

    
