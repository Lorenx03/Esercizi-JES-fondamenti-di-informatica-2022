s = "la mia casa bianca"

def appearsMoreThanOnce(S, k):
    i = 0
    for c in S:
        if c == k:
            i += 1
    
    if i > 0:
        return True
    else:
        return False


def indexOf(S, k):
    for i in range(len(S)):
        if S[i] == k:
            return i

    return -1

def asterischi(S):
    for c in S:
        if appearsMoreThanOnce(S, c) and c != " " and c != "*":
            indexOfc = indexOf(S, c)
            S = S[0:indexOfc+1] + S[indexOfc+1:len(S)].replace(c, "*")
    print(S)
    
    

    

asterischi(s)

#print(S[0:i] + S[i:len(s)])
            
        


