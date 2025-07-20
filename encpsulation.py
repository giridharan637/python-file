#ENC
class giri:
    def __init__(self):
        self.__password="1234"
    def display(self):
        print("My passsowd is:",self.__password)

G = giri()
G.__password="456" 
G.display()
#normal
class giri:
    def __init__(self):
        self.password="1234"
    def display(self):
        print("My passowrd is:",self.password)
G = giri()
G.password="678"
G.display()
