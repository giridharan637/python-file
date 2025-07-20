"""
#single in
class A():
    def Ain(self):
        print("I am parant class")
class B(A):
    def Bin(self):
        print("I am child class")

obj = B()
obj.Ain()
obj.Bin()
#multilevl in
class A:
    def Ain(self):
        print("I am A")
class B(A):
    def Bin(self):
        print("I am B")
class C(B):
    def Cin(self):
        print("I am c")
c = C()
c.Cin()
c.Bin()
c.Ain()
#herical in
class A:
    def Ain(self):
        print("I am A")
class B(A):
    def Bin(self):
        print("I am B")
class C(A):
    def Cin(self):
        print("I am C")
obj1 = C()
obj1.Cin()
obj1.Ain()
obj2 = B()
obj2.Bin()
obj2.Ain()
#Hybried
class A:
    def Ain(self):
        print("I am A")
class B(A):
    def Bin(self):
        print("I am B")
class C(B):
    def Cin(self):
        print("I am C")
class D(A):
    def Din(self):
        print("T am D")
class E(D,C):
    def Ein(self):
        print("I am E")

obj = E()
obj.Din()
obj.Cin()
obj.Ain()
obj.Bin()
obj.Ein()
"""
#multiple
class A():
    def Ain(self):
        print("I am A")
class B():
    def Bin(self):
        print("I am B")
class C(B,A):
    def Cin(self):
        print("I am C")
obj = C()
obj.Cin()
obj.Bin()
obj.Ain()

