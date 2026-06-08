num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater.")
elif num2 > num1:
    print("The second number is greater.")
elif num1 == num2:
    print("Both numbers are equal.")
else:
    print("Invalid Input")