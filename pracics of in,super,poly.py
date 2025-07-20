"""
class Shap:
    def area(self):
        return 0
class Reatangle(Shap):
    def area(self ,lent,wid):
        self.lent = lent
        self.width = wid
        area = self.lent*self.width
        return area


a = int(input("Enter length:"))
b = int(input("Enter width:"))
R =Reatangle()
result = R.area(a,b)
print("The reatangle area is:",result)
class person:
    def __init__(self,name):
        self.name = name
class Student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print("The name is:",self.name)
        print("The grade is:",self.grade)

name = input("Enter name :")
grade = input("Enter grade:")
S = Student(name,grade)
S.display()

class Vechile:
    def start(self):
        print("The vechile is start")
class car(Vechile):
    def start(self):
        print("The care starten")
C = car()
C.start()
V = Vechile()
V.start()
"""
class Employe:
    name = "giri"
    salary = 5000
class Manager(Employe):
    dep="AI"
    def display(self):
        print("The name:",self.name)
        print("The salary:",self.salary)
        print("The dep:",self.dep)
M1 = Manager()
M1.display()





























