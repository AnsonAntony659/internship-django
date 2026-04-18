num=int(input("Enter the Percentage Number"))

if num>85:
    print('A')
elif num>70 and num<=85:
     print('B')
elif num>60 and num<=70:
     print('c')
elif num>45 and num<=60:
     print('D')
else:
    print("E")


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
    
