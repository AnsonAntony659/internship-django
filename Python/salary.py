d1=dict()
i=1
n=int(input("enter number of entries:")
while i<=n:
          Nm=input("\nEnter name of the employee:")
          basic=int(input("Enter Basic salary:")
          hra=int(input("Enter house rent allowance:"))
          ca=int(input("Enter conveyance allowance:"))
          d1[Nm]=[basic,hra,ca]
          i=i+1
l.d1.keys()
print("\nName",'\t\t',"Net Salary")
for i in l:
                    salary=0
                    z=d1[i]
                    for j in z:
                    salary=salary+j
                    print(i,'\t\t',salary)
