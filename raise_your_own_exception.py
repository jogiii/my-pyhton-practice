height = float(input("enter you height: "))
weight = float(input("enter your weight: "))
if height> 3:
    raise ValueError("Are you even human !!")
bmi = weight/ height ** 2
print(f"your bmi is {bmi}")

