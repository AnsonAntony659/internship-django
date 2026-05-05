class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display1(self):
        print("Name",self.name)
        print("Age",self.age)


class Student(person):
    def __init__(self,name,age,rollno,mark):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark

    def display(self):
        self.display1()
        print("Roll No",self.rollno)
        print("Marks",self.mark)


class GStudent(Student):
    def __init__(self,name,age,rollno,mark,stream):
        super().__init__(name,age,rollno,mark)
        self.stream=stream

    def display2(self):
        self.display()
        print("Stream",self.stream)


p = GStudent('Mona',20,12,99,'computer')
p.display2()
