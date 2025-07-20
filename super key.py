class giri:
    c = " "
    def __init__(self):
        print("I am giri")
    def G1(self,a,b):
        print("value:",a+b)
        
class janu(giri):
    def __init__(self):
        print("I am janu")
    def J1(self):
        super().__init__()
        super().G1(10,15)
        super().c=" giri"
j1 = janu()
j1.J1()



