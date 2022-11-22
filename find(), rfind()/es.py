s = "asjdasdlorenzoakjshjksdlorenzo"

def indexOf(S, k):
#@param S: stringa
#@param k: sottostringa
#@return: int; -1 se non viene trovata a stringa o indice stringa
    if k in s and len(k) < len(S):
        for i in range(0, (len(S)-(len(k)-1))):
            out = False
            for j in range(0, len(k)):
                if k[j] == S[i+j]:
                    out = True
                else:
                    out = False
                    break

            if out == True:
                return i
    else:
        return -1


def rindexOf(S, k):
#@param S: stringa
#@param k: sottostringa
#@return: int; -1 se non viene trovata a stringa o indice stringa
    if k in s and len(k) < len(S):
        for i in range((len(S)-(len(k)-1)), 0, -1):
            out = False
            for j in range(0, len(k)):
                if k[j] == S[i+j]:
                    out = True
                else:
                    out = False
                    break

            if out == True:
                return i
    else:
        return -1
            

print(indexOf(s, "lorenzo"))
print(s.find("lorenzo"))
print(rindexOf(s,"lorenzo"))
print(s.rfind("lorenzo"))






