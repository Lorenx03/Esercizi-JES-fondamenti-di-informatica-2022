def removeAlpha(s):
#@param s: string; stringa di input
    out = ""

    for c in s:
        if c.isdigit():
            out = out + c
            
    return out 


def removeDigit(s):
#@param s: string; stringa di input
    out = ""

    for c in s:
        if c.isalpha():
            out = out + c

    return out


print(removeAlpha("cia34o"))
print(removeDigit("cia34o"))
