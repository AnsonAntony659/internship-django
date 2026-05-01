try:
    num1=10
    num2=20
    print("Sum of Two Numbers",num1+num3)
except:
    print("An Error Occuerred")
finally:
    print("done...")


num1 =0
while num1!=100:
    try:
        num1=int(input("Enter a number"))
        num2=int(input("Enter Another Number"))
        num3=num1/num2
        print("the quotient is :",num3)
    except:
        print("Division by Zero")
    finally:
        print("Program executed succersfully")
    




class sample():
    l="Sajila"
    def __init__(self):
        print("Hai")
    def disp(self):
        print("name=",self.l)
        s=sample()
        s.disp()
