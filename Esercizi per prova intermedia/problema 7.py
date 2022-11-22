s = "alfeo"
L = [2, 8, 0]

def func(s,L):
    out =""

    for c in L:
        if c < (len(s)-1):
            out = out + s[c]
    
    print(out)

func(s,L)