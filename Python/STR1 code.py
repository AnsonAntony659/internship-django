
STR1=list("SNo4")
for i in range(len(STR1)):
    if i==3:
        x=int(i)
        x+=x-3
        STR1[i]=x
    elif (STR1[i].islower()):
        STR1[i]=STR1[i].upper()
    else:
        STR1[i]=STR1[i]*2
print(STR1)






L=[10,20,3,100,65,87,2]
for i in  range(len(L)):
    if type(L[i])==int:
        if L[i]%2==0:
            L[i]=L[i]+10
        else:
            L[i]=L[i]+5
print(L)




L=[10,20,30,40,50,60,70]
x=int(len(L)/2)
#for i in range(x):
    #L[i],L[x+i]=L[x+i],L[i]
print(x)


STR1=input("Enter a Sentence")
L=STR1.slice()
count=0
for i in range(len(L)):
    count+=1
print("Number of words=",count)
