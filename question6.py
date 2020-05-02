import math
n1 = 0
n2 = 1
nth = 0
count = 0
nterms = int(input("enter the limit"))
if (nterms<0):
    print("not possible")
else :
    while(count < nterms):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1

def isperfectsquare(x):
    s = int(math.sqrt(x))
    return s*s ==x
def isfibonacci(n):
    return isperfectsquare(5*n*n + 4) or isperfectsquare(5*n*n - 4)
a = int(input("input the number"))
if(isfibonacci(a)== True):
        print(a,"is a fibonacci number")
else :
        print(a,"is not a fibonacci number")
