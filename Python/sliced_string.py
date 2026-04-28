#slicing
alphabet_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sliced_string=alphabet_string[6:15:4]
print(alphabet_string)
print(sliced_string)





#extend
list1=[5,3,8,6]
list2=[12,13]
list1.extend(list2)
print(list1)


#inseret
names=['vinay','Sonia','Nadhika']
names.insert(2,'deepak')
print(names)


#reverse
names=['vinay','soniya','shauriya','Radhika']
names.reverse()
print(names)


list=[12,13,14,15,16,17,158,159]
list.index(158)





l=[10,"FUN",40,"FEW",50,"FULL"]
for i in range(len(l)):
    if type(l[i])==int:
        l[i]=l[i]**2
    elif type(l[i]==str):
        l[i]=(l[i]).swapcase()
print(l)




L=[3,21,5,6,3,8,21,6]
L1=[]
L2=[]
for i in L:
    if i not in L2:
        x=L.count(i)
        L1.append(x)
        L2.append(i)
print('elment','\t\t','Frequency')
for i in range(len(L1)):
    print(L2[i],'\t\t',L1[i])



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















