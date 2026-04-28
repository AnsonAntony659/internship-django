#find the largest and smallest element in a list

num=[10,25,85,78,34,56]
largest=max(num)
smallest=min(num)

print("Largetst numbers:",largest)
print("Smallest numbers:",smallest)



n=int(input("Enter  number of elements:"))

numbers=[]

for i in range(n):
    num=int(input("enter a number"))
    numbers.append(num)


largest=numbers[0]
smallest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num

print("largest number:",largest)
print("smallest numbers:",smallest)




