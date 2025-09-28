#n = int(input("Enter your number: "))

#for i in range(2,n+1,2):
 #   print(i)

'''n = int(input("Enter your number: "))
for i in range(n,0,-1):
    print(i)'''

n = int(input("Enter your number: "))

'''for i in range(1,11):
    print(f"{n} * {i} = {n*i}")'''

'''sum = 0
for i in range(1,n+1,1):
    sum += i
print(sum)'''



'''fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)'''

'''evensum = 0
oddsum = 0
for i in range(0,n+1,1):
    if i%2==0:
        evensum += i
    else: 
        oddsum += i

print(f"Sum of even number is {evensum}\nSum of odd number is {oddsum}")'''

factors = []
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
        

print(factors)