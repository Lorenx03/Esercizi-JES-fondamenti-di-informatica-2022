s = "ci12387as"

def func(s):
    out = 0
    for c in s:
        if c.isalpha():
            out += 1

    return out


print(func(s))
