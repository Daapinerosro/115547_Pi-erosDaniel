# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 02:08:45 2019

@author: Daniel
"""

print("Leer un número entero positivo y determinar la suma de sus\
dígitos pares. Por ejemplo, en el número 124, los dígitos\
 pares son el 2 y el 4 y su suma vale 6.")
numero=int(input("escribe el número entero positivo"))
lista=[]
listapar=[]
listasu=[]
conteo = 0
suma = 0
while(numero>=10):
    residuo=numero%10
    if (residuo%2==0):
        listapar.append(residuo)
    else:
        lista.append(residuo)
    numero=numero//10
    conteo=conteo+1
if (numero%2==0):
    listapar.append(numero)
else:
    lista.append(numero)


for p in listapar:
    suma += int(p)
    listasu.append(suma)
print ("La suma de sus dígitos pares",listasu[-1])

    
    
