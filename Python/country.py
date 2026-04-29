d1=dict()
i=1
n=n=int(input("enter number of entries:"))
while i<=n:
    c=input("Enter Country:")
    cap=input("Enter Capital:")
    curr=input("Enter Currency of country:")
    d1[c]=(cap,curr)
    i=i+1
    l=d1.keys()
print("\nCountry\t\t","Capital\t\t","Currency")
for i in l:
              z=d1[j]
              print('\n',i,'\t\t',end="")
              for j in z: 
                print(j,'\t\t',end="\t\t")
x=input("\nEnter Country to be searched:")
for i in l:
              if i==x:
                print("\nCountry\t\t","Capital\t\t","Currency\t\t")
              z=d1[i]
              print('\n',i,'\t\t',end="")
              for j in z:
                print(j,'\t\t',end="\t\t")
              break
