def inserisci (L, n1, n2):
    out = []

    for elem in L:
        out.append(elem) 
        if elem == n1:
            out.append(n2)


    print(out)
            
#return out

print(inserisci([3, 12, 4, 3, 10, 3], 3, 0))
