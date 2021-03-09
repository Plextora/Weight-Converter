weight = int(input("Enter your weight: "))
unit = input("What unit is your weight? (L)bs or (K)ilograms (L for lbs K for kilograms.) ")
if  unit.upper() == "L":
    converted = weight * 0.45
    print(" ")
    print(f"You are {converted} kilograms!")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds!")

print(" ")



print("If the converted weight is decimals, round the weight")
print(" ")
print("Example: 45.75 kilograms = 46 kilograms")