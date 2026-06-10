n = int (input("Enter no for check number is perfect or not : "))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum + i
if sum == n:
    print("Perfect Number") 
else:
    print("Not perfect")       