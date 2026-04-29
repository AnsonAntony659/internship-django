phone=dict()
i=1
n=int(input("Enter number of entries:"))
while i<=n:
    a=input("Enter Name:")
    b=input("Enter phone no:")
    phone[a]=b
    i=i+1
    l=phone.keys()
    x=input("Enter name to be searched:")
    for i in 1:
        if i==x:
            print(x,":phone no is:",phone[i])
            break
        else:
            print(x,"does not exist")
