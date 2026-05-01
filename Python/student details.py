class Student():
    def details(self):
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.address=input("Enter your Address:")
        self.phone_no=int(input("Enter your phone number:"))
        self.Roll_no=int(input("Enter your Rollno:"))

    def print(self):
        print("Student Name:",self.name)
        print("Student Age:",self.age)
        print("Student Address:",self.address)
        print("Student Phone no:",self.phone_no)
        print("Student Roll no",self.Roll_no)

s=Student()
s.details()
s.print()




