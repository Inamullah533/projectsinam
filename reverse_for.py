a = str(input("Enter any string : "))
string = ""
for i in range(1,len(a)+1):
    string =string + a[-i]
print(f"The reverse string is {string}")