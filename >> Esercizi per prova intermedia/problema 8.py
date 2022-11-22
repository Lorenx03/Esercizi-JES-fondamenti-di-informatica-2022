s = "ci12387"

def func(s):
    out = ""
    for c in s:
        if c.isalpha():
            out += "*"

    return out

print(func(s))