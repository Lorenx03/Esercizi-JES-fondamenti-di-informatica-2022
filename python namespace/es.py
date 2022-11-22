a = 10

def func_1():
   print (a)


def func_2(x):
   global a
   a = 2
   y = x+10
   func_1()


def func_3(x):
   #print (a)
   a = 4
   y = x+10
   func_1()


func_2(7)
func_3(7)
