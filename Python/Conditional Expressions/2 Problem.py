age = int(input("Enter the age: "))
day = str(input("Enter day: "))
price = int()
if age>=18:
    price = 12
else:
    price = 8

if day == "Wednesday":
    price = price-2
    print(price)
else :
    print(price)

#OTHER SYNTAX
# price = 12 if age>=18 else 8
# if day == "Wednesday" :
#price = price-2