class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display1(self):
        print("Name",self.name)
        print("Age",self.age)


class student():
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks

    def display(self):
        print("Roll No",self.rollno)
        print("Marks",self.marks)


class gstudent(person,student):
    def __init__(self,name,age,rollno,marks,stream):
        person.__init__(self,name,age)
        student.__init__(self,rollno,marks)
        self.stream=stream

    def display2(self):
        self.display1()
        self.display()
        print("Stream",self.stream)


p = gstudent('arjun',20,12,99,'computer')
p.display2()
