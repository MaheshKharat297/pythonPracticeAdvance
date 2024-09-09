import random

def selectName(names):
    name = random.choice(names)
    return name

name_count = int(input("Please enter how many people is present : "))
names = []
for i in range(name_count):
    name = str(input("Enter name :"))
    names.append(name)

selected_name = selectName(names)
print(f"YAY!! {selected_name} will pay the bill !!!!")