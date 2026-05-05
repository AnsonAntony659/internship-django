class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def display(self):
        print("Enter length and breadth",self.length,self.breadth)

class area(rectangle):
    def __init__(self,length,breadth):
        rectangle.__init__(self,length,breadth)
        self.area=self.length*self.breadth
    def displayarea(self):
        print("area of a rectangle",self.area)

s=area(length=10,breadth=33)
s.display()
s.displayarea()
        
        
        
