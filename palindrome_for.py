s = input("Enter any string or number: ")
rev = ""
for i in range(1, len(s) + 1):
    rev = rev + s[-i]

if s == rev:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
