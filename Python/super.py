class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display1(self):
        print("Name:",self.name)
        print("Age:",self.age)


class Student(person):
    def __init__(self,name,age,roll_no,mark):
        super(Student,self).__init__(name,age)
        self.roll_no=roll_no
        self.mark=mark
    def display(self):
        self.display1()
        print("rollno",self.roll_no)
        print("Marks",self.mark)

p=Student('mona',20,12,99)
p.display1()
