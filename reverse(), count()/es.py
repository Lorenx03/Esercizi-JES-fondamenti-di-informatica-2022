s = [0,1,2,3,1,5,6,7,1,9]


def myReverse(L):
#@param L: list; lista input
    reverse = []

    for i in range(len(S)-1, -1, -1):
        reverse.append(S[i])

    return reverse


def myCount(L, k):
#@param L: list; lista input
    i = 0
    for c in S:
        if c == k:
            i = i + 1
    
    return i


print(myReverse(s))

print(myCount(s, 1))