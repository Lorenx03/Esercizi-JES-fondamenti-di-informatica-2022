s = 'osso'

def isPalindrome(S):
    reverse = ""

    for i in range(len(S)-1, -1, -1):
        reverse = reverse + S[i]

    print(S)
    print(reverse)

    if reverse == S:
        return True
    else:
        return False

print(isPalindrome(s))