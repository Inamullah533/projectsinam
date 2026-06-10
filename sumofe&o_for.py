e = int(input("Enter number for sum even number: "))
o = int(input("Enter number for sum of odd number: "))
sum_odd = 0
sum_even = 0
for i in range(2,e+1,2):
    sum_even= sum_even + i
for j in range(1,o+1,2):
    sum_odd= sum_odd + j
print(f"The sum of even number is = {sum_even}")
print(f"The sum of odd numbers is = {sum_odd}")