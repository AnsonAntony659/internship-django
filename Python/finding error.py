d1=dict()
i=1
n=int(input("Enter number of entries:"))
while i<=n:
    a=input("Enter name:")
    b=input("Enter age:")
    d1[a]=b
    i=i+1
l=d1.keys()
for i in l:
        print(i,'\t',d1[i])
