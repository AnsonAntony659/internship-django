class vehicle():
    def __init__(self,brand,year):
        self.year=year
        self.brand=brand
    def display(self):
        print("brand",self.brand,"year",self.year)



class car(vehicle):
    def __init__(self,brand,year,name):
        vehicle.__init__(self,brand,year)
        self.name=name
    def display_car(self):
        print("name",self.name)
c=car(brand="maruthi",year=2018,name="Albin")
c.display()
c.display_car()
