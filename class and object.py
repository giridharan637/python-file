"""
class student:
    name= " "
    age = " "
    def sectionA(self):
        print("This stuent is A section")
    def sectionB(self):
        print("This student is B section")

obj1 = student()
obj1.name="giri"
obj1.age=18
print("the student name is:",obj1.name)
print("The student age:",obj1.age)
obj1.sectionA()
print() 
obj2 = student()
obj2.name="Keerthanan"
obj2.age=17
print("the student name is:",obj2.name)
print("The student age:",obj2.age)
obj2.sectionB()
"""
class Laptop:
    price =" "
    proceser =" "
    ram =" "
    def HP(self):
        print("This is HP laptop")
    def DELL(self):
        print("this is DELL laptop")
    def LENOVO(self):
        print("This is LENOVO laptop")
hp = Laptop()
hp.price = 200000
hp.proceser = "High"
hp.ram = "8GB"
hp.HP()
print("The hp laptop price is :",hp.price)
print("The hp laptop proceser is:",hp.proceser)
print("The hp laptop ram storage is:",hp.ram)
de = Laptop()
de.price = 400000
de.proceser = "low"
de.ram = "16GB"
de.DELL()
print("The dell laptop price is :",de.price)
print("The dell laptop proceser is:",de.proceser)
print("The dell laptop ram storage is:",de.ram)
le = Laptop()
le.price = 200000
le.proceser = "High"
le.ram = "8GB"
le.LENOVO()
print("The lenovo laptop price is :",le.price)
print("The lenovo laptop proceser is:",le.proceser)
print("The lenovo laptop ram storage is:",le .ram)
    
