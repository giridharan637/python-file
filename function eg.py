"""
def add():
    print("Addtion:")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a+b
    print(c)
add()
def sub():
    print("Suraction:")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a-b
    print(c)
sub()
def mul():
    print("Multlpaction:")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a*b
    print(c)
mul()
def div():
    print("divection:")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    if(b!=0):
        c = a/b
        print(c)

    else:
        print("zero dinamater is not allowed")
div()

n = int(input("Enter n:"))
def findoddoreven(n):
    if(n%2==0):
        print("this even number")
    else:
        print("odd number")
findoddoreven(n)

n = int(input("Enetr mark:"))
def passorfail(mark):
    if(mark>=35):
        print("pass")
    else:
        print("fail")
passorfail(n)
"""
a = int(input("Enter a:"))
b = int(input("Enter b:"))
def printrage(a,b):
    for i in range(a,b+1):
        print(i)
printrage(a,b)

