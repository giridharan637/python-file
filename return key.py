"""

s_username = "giri"
s_password = "giri@123"

user = input("Enter user name: ")
pas = input("Enter a password: ")

def validat(user, pas):
    if (s_username == user) and (s_password == pas):
        return True
    else:
        return False

result = validat(user, pas)
print(result)
"""
a = int(input("Enter a:"))
b = int(input("Enter b:"))
def add():
    return a+b

sum = add()
print("The sum :",sum)
c = int(input("Enter c:"))
ans = sum*c
print("The final value is:",ans)
