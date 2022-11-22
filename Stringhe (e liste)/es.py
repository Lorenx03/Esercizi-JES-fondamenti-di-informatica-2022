
def f1(s_1, s_2):
    if len(s_1) > len(s_2):
        return s_1
    else:
        return s_2


def f2(s_1, s_2, s_3):
    if len(s_1) > len(s_2) and len(s_1) > len(s_3):
        return s_1

    if len(s_2) > len(s_1) and len(s_2) > len(s_3):
        return s_2
    
    if len(s_3) > len(s_2) and len(s_3) > len(s_1):
        return s_3



def f3(n):
    maxLenght = ""

    for i in range(len(n)):
        if len(maxLenght) < len(n[i]):
            maxLenght = n[i]

    return maxLenght


print(f1("ciao", "testotestotestotesto"))
print(f2("ciao", "testotestotestotesto", "stqw"))
print(f3(["ciao", "testotestotestotesto", "stqw"]))
