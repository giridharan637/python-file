"""
# mark calculase
mark = int(input())
if(mark>35):
    print("pass")
elif(mark == 35):
    print("just pass")
else:
    print("Fail")
    # eligilble for scholarship
income = int(input())
if(income>7000):
        print("Not eligilble for scholarship")
else:
        print("Scholarship is available")
        #divsible by 3 and 4
n = int(input("Enter a number:"))
if(n%3==0 and n%5==0):
    print("divsible")
else:
    print("not divsible")
#odd or even
n = int(input())
if(n%2==0):
    print("Even number")
else:
    print("odd number")
    #score calculate
score = int(input("Enter a Score:"))
if(score<35):
    print("Poor student")
elif(score>35 and score<70):
    print("Average student")
elif(score>70):
    print("good student")
    #mini calc
a = int(input("Enter a first number:"))
b = int(input("Enter a first number:"))
op = input("Enter a operation:")
if(op == "+"):
    print("Addtion:",a+b)
elif(op == "-"):
    print("Subvalue:",a-b)
elif(op == "*"):
    print("multipleaction:",a*b)
elif(op == "/"):
    print("Divesion value is :",a/b)
elif(op == "%"):
    print("module:",a%b)
else:
    print("invalid operation")   
    """ 
score = int(input("Enetr a score for persantage:"))
if(score>= 70):
    name = input()
    dep = input()
    location = input()
    print("My name is :",name)
    print("My departement is:",dep)
    print("My location is:",location)
    print("Iam eligible")
else:
    print("not eligible")
    

