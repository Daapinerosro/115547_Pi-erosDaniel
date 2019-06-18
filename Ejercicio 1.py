# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:17:44 2019

@author: Daniel
"""
print("1. Sin utilizar el comando abs, escribir un \
programa que calcule e imprima el valor absoluto de cualquier número \
(sea entero o decimal).")

valor="absoluto"# declarando variabla para desarrollar el ciclo while
while valor =="absoluto":#Mientras la variable se mantenga, retomar ciclo
   
    x=float(input("Digite un número"))#float para que input sea un dato tanto entro como decimal 
    
    if (x<0):# si el valor ingresado es neegativo
        y=x*-1
        print("el valor absoluto es",y)
        
    if (x>=0):#si el número ingresado es positivo 
        print("el valor absoluto es",x) 
        