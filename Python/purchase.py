name=input("Enter the customer name:")
item=int(input("Enter 1 for AC and 2 For LCD Tv:"))
amount=int(input("Enter the Purchase amount:"))
discount=0
if item==1:#ac
    if amount<20000:
        discount=5
    elif amount>=20000 and amount<=40000:
        discount=7.5
    elif amount>=40000 and amount<=40000:
        discount= 10
    elif amount>60000:
        discount=12
    else:
        print ("invalid ")
elif item==2:#lcd tv
    if amount<20000:
        discount=2.5
    elif amount>=20000 and amount<=40000:
        discount=5
    elif amount>=40000 and amount<=40000:
        discount=7
    elif amount>60000:
        discount=8.5
    else:
        print("invalid ")


discount_amount=amount*discount
amount_final=amount-discount_amount

print("Customer Name:",name)
print("Disount Amount:",discount_amount)
print("Final Amount:",amount_final)
    
    
    




