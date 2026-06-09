num = int(input("Enter any integer number: "))
if num == 0:
    print("Zero is neither even nor odd.")
elif num % 2 == 0:
    print(f"{num} is an even number.")
elif num % 2 != 0:
    print(f"{num} is an odd number.")
else:
    print("Invalid input.")