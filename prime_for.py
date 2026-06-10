n = int (input("Enter number for check prime number or not: "))
sum = 0
for i in range(1,n,1):
    if n%i==0:
        print(f"{n} is prime number")
    else:
        print("Not prime number") 
        