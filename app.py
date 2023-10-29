weight = input("what is your weight? ")
unit = input("What is your weight unit? (kg/lb)")
unit = unit.lower()
weight = float(weight)
if unit == "kg":
    print(f"Your weight in Pounds is: {round(weight * 2.204, 2)}")
elif unit == "lb":
    print(f"Your weight in kilos is: {round(weight / 2.204, 2)}")
else:
    print(" This weight unit is not supported")




