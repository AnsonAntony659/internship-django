class gro():
    def __init__(self):
        self.name = input("Enter name:")
        self.bsalary = int(input("Enter basic salary:"))
        print("Name:", self.name, "Basic Salary:", self.bsalary)

    def cal(self):
        self.da = self.bsalary * 30 / 100
        self.hra = self.bsalary * 20 / 100
        self.pf = self.bsalary * 10 / 100
        print("DA:", self.da, "HRA:", self.hra, "PF:", self.pf)


class net(gro):
    def __init__(self):
        super().__init__()   # calls parent constructor

    def displayyy(self):
        self.gsalary = self.bsalary + self.da + self.hra
        self.nsalary = self.gsalary - self.pf
        print("Gross Salary:", self.gsalary, "Net Salary:", self.nsalary)


b = net()
b.cal()
b.displayyy()
    
class gro():
    def __init__(self):
        self.name=input("enter name:")
        self.bsalary=int(input("enter bsalary:"))
        print("name",self.name,"bsalary",self.bsalary)
    def cal(self):
         self.da=self.bsalary*30/100
         self.hra=self.bsalary*20/100
         self.pf=self.bsalary*10/100
         print("da",self.da,"hra",self.hra,"pf",self.pf)
class net(gro):
    def __init__(self,name,bsalary,gsalary,nsalary):
        gro. __init__(self,name,bsalary)
    def displayyy(self):
         self.gsalary=self.bsalary+self.da+self.hra
         self.nsalary=self.gsalary-self.pf
         print("gsalary",self.gsalary,"nsalary",self.nsalary)
b=net()
b.cal()
b.displayyy()

         
            
    
    
