s = "cantami o diva del pelide achille"


def myReverse(S):
#@param S: string; stringa di input
    reverse = ""

    for i in range(len(S)-1, -1, -1):
        reverse = reverse + S[i]

    return reverse


def myCount(S, k):
#@param S: string; stringa di input
    i = 0
    for c in S:
        if c == k:
            i = i + 1
    
    return i


print(myReverse(s))

print(myCount(s, 'a'))