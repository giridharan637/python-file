#instanc varible
class phone():
    def __init__(self,brand,price,charger):
        self.brand=brand
        self.price=price
        self.charger=charger
    def display(self):
        print("The moblile brand is:",self.brand)
        print("The moblile price is:",self.price)
        print("The moblile charge-Type is:",self.charger)
vivo = phone("vivoy27","30,000","C-Type")
vivo.display()
oppo=phone("oppo","30,00","B-Type")
oppo.display()
#class varible
class phone():
    charger = "C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("The moblile brand is:",self.brand)
        print("The moblile price is:",self.price)
        print("The moblile charge-Type is:",self.charger)
vivo = phone("vivoy27","30,000")
vivo.display()
oppo=phone("oppo","30,00")
oppo.display()
        
        

        
        
