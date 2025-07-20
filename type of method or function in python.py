"""
#instence method
class Laptop():
    def display(self,name):
        self.h = name 
        print("The name is:",self.h)
hp = Laptop()
hp.display("giri")

#class method
class Laptop():
    name = "giri"
    @classmethod
    def Display(cls):
        cls.name = "yuvi"
        print("My sister name is:",cls.name)
#hp = Laptop()
#Laptop.Display(hp)
Laptop.Display()
#Laptop.Display(Laptop)
"""
#static method
class stu():
    @staticmethod
    def giri():
        print("The student")
s1 = stu()
s1.giri()
stu.giri()
