class Society():
    def details(self):
        self.societyname=input("Enter The Society Name:")
        self.house_num=int(input("Enter The House Number:"))
        self.No_of_memb=int(input("Enter The Number Of Members:"))
        self.Flat=int(input("Enter the Flat Number"))
        self.Income=int(input("Enter the Income"))
        if self.Income>=25000:
            print("A TYPE")
        elif 20000 <= self.Income < 25000:
            print("B TYPE")
        elif self.Income<=15000:
            print("C TYPE")
        else:
            print("Invalid Input")

    def print(self):
        print("Enter the Society Name:",self.societyname)
        print("Enter the House Number:",self.house_num)
        print("Enter the No of Members:",self.No_of_memb)
        print("Enter the Flat Number:",self.Flat)
        print("Enter the Income:",self.Income)

s=Society()
s.details()
s.print()



