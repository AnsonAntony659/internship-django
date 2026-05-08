class science():
    def __init__(self):
        print("Science includes Biology and computer")


class biology(science):
    def display(self):
        self.mark1=int(input("Enter Biology Mark:"))
        if self.mark1 >= 40:
            print("pass")
        else:
            print("fail")

class computer(science):
    def display1(self):
        self.mark2=int(input("Enter computer marks:"))
        if self.mark2>=40:
            print("pass")
        else:
            print("Fail")


class zoology(biology):
    def display2(self):
        self.mark3=int(input("Enter Zoology marks:"))
        print("Zoology Marks:",self.mark3)



class botany(biology):
    def display3(self):
        self.mark4=int(input("Enter Botany Marks:"))
        print("Botany Marks",self.mark4)


b=botany()
b.display3()
b.display()
z=zoology()
z.display2()
c=computer()
c.display1()



