"""
class student:
    def __init__(self):
        self.name=" "
        self.rg=" "
    def display(self):
        print("The student name is: ",self.name)
        print("The student Registor NO is: ",self.rg)

s1=student()
s1.name="giri"
s1.tg="RTC2024BAI051"
s1.display()

class Furit:
    def __init__(self,col):
        self.colure=col
F=Furit("pink")
print(F.colure)

class Teacher:
    def __init__(self,name,RG):
        self.name=name
        self.rg=RG

    def display(self):
        print("The name:",self.name)
        print("The rgno:",self.rg)
 
t1=Teacher("giri","rtc123")
t2=Teacher("yuvi","rtc456")
t1.display()
t2.display()
"""
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addtion:",self.a+self.b)
    def sub(self):
        print("sub:",self.a-self.b)
    def mul(self):
        print("Multiple:",self.a*self.b)
    def div(self):
        if(b!=0):
             print("Dived:",self.a/self.b)
        else:
            print("Zero is not allowed")


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = calc(a,b)
c.add()
c.sub()
c.mul()
c.div()
