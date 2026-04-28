student={}
n=int(input("enter the number of students:"))
for i in range(n):
    adm=input("admission no:")
    rollno=input("rollno:")
    name=input("name:")
    mark=input("mark:")
    student[adm]=[rollno,name,mark]
    i=i+n
for i in student:
    print("\nAdmno",i,":")
    z=student[i]
    print("Name\t","class\t","per\t")
    for j in z:
        print(j, end="\t")
