class science():
    def __init__(self):
        print("Science includes Biology and computer")


class biology(science):
    def display(self):
        self.bio=int(input("Enter Biology Marks:"))
        if self.bio >= 40:
            print("pass")
        else:
            print("fail")

class computer(science):
    def display1(self):
        self.inp=int(input("Enter computer marks:"))
        if self.inp>=40:
            print("pass")
        else:
            print("Fail")


class zoology(biology):
    def display2(self):
        self.zoo=int(input("Enter Zoology marks:"))
        print("Zoology Marks:",self.zoo)



class botany(biology):
    def display3(self):
        self.bot=int(input("Enter Botany Marks:"))
        print("Botany Marks",self.bot)


b=botany()
b.display3()
b.display()
z=zoology()
z.display2()
c=computer()
c.display1()



