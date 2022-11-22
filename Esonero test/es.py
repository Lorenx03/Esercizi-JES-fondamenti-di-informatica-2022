lista = ['ciao', 'prova', 'lavanderia', 'so', 'foo']

def trovaString(L, z):
    for i in range(len(L)):
        if len(L[i]) == z:
            return i
    
    return -1
        

print(trovaString(lista, 2))

