class train():
    def inputdata(self):
        self.tnum=int(input("Enter Train number:"))
        self.name=input("Enter Train Name:")
        self.start=input("Enter Starting Station:")
        self.dstnt=input("Enter Destination:")
        self.dptrtym=input("Enter depature time:")
        self.arritym=input("Enter Arrival time:")


class passenger(train):
    def inputdata1(self):
        self.tktnum=int(input("Enter Ticket Number:"))
        self.pname=input("Enter passenger Name:")
        self.gnd=input("Enter gender:")
        self.age=int(input("Enter age :"))
        self.adrs=input("Enter Address:")
        self.phno=int(input("Enter phone no :"))

        print("Train Number",self.tnum)
        print("Train Number",self.tnum)
        print("Starting Station",self.start)
        print("Destination",self.dstnt)
        print("Departure Time",self.dptrtym)
        print("Arrival Time",self.arritym)

class ticket(passenger):
    def inputdata2(self):
        print("Ticket Number",self.tktnum)
        print("Passenger Name",self.pname)
        print("Gender",self.gnd)
        print("Age:",self.age)
        print("Enter Address",self.adrs)
        print("Phone number",self.phno)

c=ticket()
c.inputdata()
c.inputdata1()
c.inputdata2()
         
        
        
        
        
        
        
