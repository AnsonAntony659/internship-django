classxi=dict()
n=int(input("Enter total number of section in xi class:"))
i=1
while i<=n:
     a=input("Enter Section:")
     b=input("Enter Stream name:")
     classxi[a]=b
     i=i+1
print("class",'\t',"Section",'\t',"Stream name")
for i in classxi:
    print("xi",'\t',i,'\t',classxi[i])
     


Dict={'Teena': 18,'Riya':12,'Alya':22,'Ravi':25}
Dict=['Riya']=28
print(Dict)
