def print_result(new_weight: float, new_unit: str):
    print(f"Your weight in {new_unit} is: {new_weight}")


weight = input("what is your weight? ")
unit = input("What is your weight unit? (kg/lb)")
unit = unit.lower()
weight = float(weight)
if unit == "kg":
    new_weight = round(weight * 2.204, 2)
    print_result(new_weight, 'lb')
elif unit == "lb":
    new_weight = round(weight / 2.204, 2)
    print_result(new_weight, 'kg')
else:
    print(" This weight unit is not supported")
