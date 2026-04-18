salary=int(input("Enter the Slary of a person"))
if salary <=50000:
    tax=0.05*salary
elif salary<=60000:
    tax=0.07*salary
elif salary<=70000:
    tax=0.08*salary
else :
    tax=0.10*salary
print("salary:",salary,"Tax:",tax)  
    
