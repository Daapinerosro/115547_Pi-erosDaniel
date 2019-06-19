nombre=(input("favor escriba dos nombres"))
nom= nombre.upper().lower()

def ordenar_lista_cadenas(L):
    
    f = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN")
    range_num = range(len(L))
    L_sin_tilde = [L[i].translate(f) for i in range_num]
    tmp = sorted(zip(L_sin_tilde, range_num))
    L_ord, idx = zip(*tmp)
    return [L[idx[i]] for i in range_num]


lista = nom.split()
li=lista[0:2]
print(sorted(li))
print("El orde de su lista cadena es",ordenar_lista_cadenas(li))           


        
