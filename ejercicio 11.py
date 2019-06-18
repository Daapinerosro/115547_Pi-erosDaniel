

x=input('El texto ingresado es ')
cont1=0 
cont2=0  
cont3=0  
cont4=0 
cont5=0  

for i in range(0,len(x)):
    valor=ord(x[i])
    if(valor==65 or valor==69 or valor==73 or valor==79 or valor==85):
        cont1=cont1+1
    elif (valor==193 or valor==201 or valor==205 or valor==211 or valor==218 or
          valor==225 or valor==233 or valor==237 or valor==243 or valor==250):
        
        cont2=cont2+1
        
    elif(x[i].isdigit()):
        cont3=cont3+1
    if (x[i]==' '):
        cont4=cont4+1

print('existen',cont1,'N° de Vocales Mayusculas')
print('existen',cont2,'Vocales con tilde')
print('existen',cont3,'Digitos')
print('existen',cont4,'N° Espacios')
