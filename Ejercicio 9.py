
"""9.Hacer un programa que lea las coordenadas (x1,y1,r1) y (x2,y2,r2)\
 que corresponden al centro y al radio de dos círculos. Lea un punto de \
 coordenadas (a,b). Determina si (a,b) está \
 contenido: a) dentro del círculo 1; b) dentro \
del círculo 2; c) dentro de ambos círculos; d) fuera \
de ambos círculos. Recordemos que el círculo es el lugar\
 geométrico de los puntos del plano cuya distancia a \
 otro punto fijo, llamado centro, es menor o \
 igual que una cantidad constante, llamada radio."""
import math#determino las variables a ingresar
x1=(int)(input('(circulo número 1)introduzca la coordenada en x: '))
y1=(int)(input('(circulo número 1)introduzca la coordenada en y: '))
r1=(int)(input('(circulo número 1)introduzca el radio: '))

x2=(int)(input('(circulo número 2)introduzca la coordenada en x: '))
y2=(int)(input('(circulo número 2)introduzca la coordenada en y: '))
r2=(int)(input('(circulo número 2)introduzca el radio: '))

a=(int)(input('coord en a: '))
b=(int)(input('coord en b: '))
#Con ayuda del modulo  math y sqrt agrego los datos a una posicion 
di1=math.sqrt((x1-a)**2+(y1-b)**2)
di2=math.sqrt((x2-a)**2+(y2-b)**2)
#por último determino condicionales 
cont=0
if (di1<=r1):
    print('(a,b) esta en el circulo 1')
    cont=cont+1
else:
    print('(a,b) no esta en el circulo 1')
if (di2<=r2):
    print('(a,b) esta en el circulo 2')
    cont=cont+1
else:
    print('(a,b) no esta en el circulo 2')
if (cont==2):
    print('(a,b) esta en los dos circulos')
if (cont==0):
    print('(a,b) no esta en ninguno de los dos circulos')