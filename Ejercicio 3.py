# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:49:43 2019

@author: Daniel
"""
 
nument=int(input("escribe el número entero de sólo 3 dígitos"))
lista=[]

if (-999<nument and nument<999):
    if (0<nument<999):
        j=(nument % 1000) // 100
        lista.append(j)
        k=(nument % 100) // 10
        lista.append(k)
        n=(nument % 10) // 1
        lista.append(n)
       
        lis=0        
        for p in range(0,3):
            if (lista[p]==8):
                lis=1+lis          
        print("contiene el número 8",lis)        
    if (-999<nument<0):
        num=(nument*(-1))
        j=(num % 1000) // 100
        lista.append(j)
        k=(num % 100) // 10
        lista.append(k)
        n=(num % 10) // 1
        lista.append(n)
        lis=0        
        for p in range(0,3):
            if (lista[p]==8):
                lis=1+lis          
        print("contiene el número 8",lis)  
else:
     print("no ingreso un número de 3 dígitos")
    
