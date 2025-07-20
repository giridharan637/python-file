"""
#method overring
class giri:
    def add(self,a,b):
        print("The two sum parent :",a+b)
class yuvi(giri):
    def add(self,a,b):
        print("The two  sum of child :",a+b)
obj = giri()
obj.add(10,15)
obj2 = yuvi() 
obj2.add(10,20)
#method overloading
class giri:
    def add(self,a,b,c=0):
        if c==0:
            print("The two sum:",a+b)
        else:
            print("The three sum:",a+b+c)
G = giri()
G.add(10,20)
G.add(10,20,30)
"""
class Animal:
    def sound(self):
        print("The Animal make sound")
class Dog(Animal):
    def sound(self):
        print("The Dog id bark")
class Bird(Animal):
    def sound(self):
        print("Bird sing")

B =Bird()
B.sound()
D = Dog()
D.sound()
A = Animal()
A.sound()
