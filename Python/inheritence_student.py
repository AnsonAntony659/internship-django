class student():
    def Students(self):
        self.name=input("Enter your name:")
        self.age=int(input("Enter Your Age:"))
        self.roll=int(input("Enter your Roll no:"))


class Details(student):
    def Detais_student(self):
        print("Name is:",self.name)
        print("Age Is:",self.age)
        print("Roll No:",self.roll)


s=Details()
s.Students()
s.Detais_student()


