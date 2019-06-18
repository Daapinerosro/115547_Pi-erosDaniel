

numero=int(input("escribe un número"))#Número para reconocer 
lista=[]#próximas a utilizar
listasu=[]
listf=[]
conteo = 0#Necesario para mantener el ciclo while hasta que el número 
#digitado se convierta en caracteres de una lista
suma = 0
while(numero>=10):
    residuo=numero%10
    lista.append(residuo)
    numero=numero//10
    conteo=conteo+1
lista.append(numero)# termina con el último dígito y guardado en lista
for p in lista: # for para que sume todos los caracteres de la lista y su
    #suma queda guardad en el último caracter
    suma += int(p)
    listasu.append(suma)
    t=listasu[-1]# aquí queda guardada todos los valores de la lista
if (numero>=0):
    print ("La suma de los dígitos de tu número es",t)
else :
    print ("La suma de los dígitos de tu número son negativos y no hacen parte de la serie de Fibonacci")
    
  
a=1
b=0
r=0

for i in range (0,100):#for para expresar la serie de Fibonacci 
    r=b
    b=a
    a=r+b
    listf.append(a)

lis=0        
for p in range(0,100):# Slicing de acada espacio de la serie de fibonacci,
    #comparada con y=la suma de nuestra lista(número)
    
    if (listf[p]==t):
        lis=1+lis#Si hae parte de la serie de fibonacci queda guardada coomo 1
        # una (ocurrencia)
        
if (lis==1 and numero>0):# Como sólo puede haber una ocurrencia y el número
    #entero ingresado debe ser positivo
            print("La suma de los dígitos de tu número se encuentra en la \
 serie de Fibonacci")
else:# cuando el número entero ingresado es negativo y no hay ocurrencias 
            print("la suma de los dígitos no hace parte de la \
 la serie de Fibonacci")
            
    

        

        
        


    