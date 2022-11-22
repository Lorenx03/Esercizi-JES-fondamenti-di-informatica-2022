sequenza = [3, 5, 12, 31, 43, 7, 11, 20, 14, 78, 23, 95, 27]


def stampaPosPari(s):
    for i in range(0, len(s), 2):
        print(s[i])


def stampaPosDispari(s):
    for i in range(1, len(s), 2):
        print (s[i])


print("Stampa pos Pari:")
stampaPosPari(sequenza)

print("Stampa pos Dispari:")
stampaPosDispari(sequenza)
