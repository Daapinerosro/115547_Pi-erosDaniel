"14. Leer una cadena de texto y organice \
alfabéticamente cada una de las letras \
que la componen, repitiendo cada una\
 tantas veces como se encuentra. Por ejemplo, la cadena \
 ‘tarea importante’ será ‘aaaeeimnoprrttt’. (Note que no\
 se incluyen los espacios)."
 
cadt=(str(input("escriba un texto: ")))

cadtex=sorted(cadt)
cadtex1=[]
#
for i in range(0,len(cadtex)):
    if cadtex[i]!="  ":
        
        cadtex1.append(cadtex[i])
        
print(cadtex1)

cadena = "".join(cadtex1)
cadt1=str(cadena)

print("El orden alfabéticamente repitiendo cada \
 una tantas veces como se encuentre",cadt1)
