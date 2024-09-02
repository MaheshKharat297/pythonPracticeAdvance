def bmi(height, weight):
    h = float(height) ** 2

    final_bmi = int(weight) // h

    return int(final_bmi)

height = input("Enter Height here : ")
weight = input("Enter Weight here : ")
Actual_bmi = bmi(height, weight)

if Actual_bmi > 30:
    print(f"Your BMI is {Actual_bmi} which is overweight")
elif Actual_bmi < 30 and Actual_bmi > 25:
    print(f"Your BMI is {Actual_bmi} which is slightly high")
else:
    print(f"Your BMI is {Actual_bmi} which is Perfect")