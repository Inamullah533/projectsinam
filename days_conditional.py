temp=int(input("Enter a temperature in celsius: "))
if temp < 0:
    print("It's freezing cold.")
elif temp >= 0 and temp < 10:
    print("It's very cold.")    
elif temp >= 10 and temp < 20:
    print("It's cold.")
elif temp >= 20 and temp < 30:
    print("It's warm.")
elif temp >= 30 and temp < 40:
    print("It's hot.")
elif temp >= 40:
    print("It's very hot.")