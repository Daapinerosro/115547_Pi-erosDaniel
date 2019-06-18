
"Ejerciio10"
entrada= 'abcdefghijklmnñopqrstuvwyxzáéíóúü'
salida= 'ABCDEFGHIJKLMNÑOPQRSTUVWYXZÁÉÍÓÚÜ'
cad=input("escriba una palabra")
cambio=str.maketrans(entrada,salida)
str=cad
cade=str.translate(cambio)

print(cade)



