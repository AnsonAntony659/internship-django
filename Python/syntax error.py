#Syntax error
num1=10
num2=20
print("Sum of TWo Numbers ",num1+num3)


#type error
num1=10
num2=20
print("Sum of TWo Numbers="+num1+num2)


#value error
#age=int(input("Enter your Age:"))


#zero division error
num=eval(input("Enter a Number"))
rev_num=1/num
print("Inverse of a number",rev_num)



#Attribute Error
aList=0
for i in range(10):
    aList.append(i)
print(aList[10])


#Key Error
digits={0:'Zero',1:'one',2:'Two',3:'Three',4:'Four',}
print(digits['five'])


#Index Error
colors=['red','green','blue']
colors[4]


#IOError
f=open('pasdswordfile.text')


#Indendation Error
limit=5
for num in range(limit):
    print(num)


    
