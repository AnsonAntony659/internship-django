class Subject():

    def subject_details(self):
        self.Name=input("ENTER YOUR NAME:")
        self.Physics=int(input("Enter mark for physics:"))
        self.chemistry=int(input("Enter mark for Chemistry:"))
        self.Biology=int(input("Enter mark for Biology:"))


class Subject_marks(Subject):

    def marks(self):
         self.total= self.Physics+self.chemistry+self.Biology
         self.percentage=(self.total/300)*100


    def grade(self):
        if self.percentage>=80:
            print("Wow Distinctit")
        elif  self.percentage>=60:
            print("First class")
        elif  self.percentage>=45:
            print("second class ")
        elif  self.percentage>=40:
            print("pass")
        else:
            print("fail")

    def display(self):
        print("Name is:",self.Name)
        print("Total Mark:",self.total)
        print("Your Grade is:",self.percentage)

s=Subject_marks()
s.subject_details()
s.marks()

s.display()
s.grade()

            
