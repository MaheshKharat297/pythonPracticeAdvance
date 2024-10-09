import copy

class Car:

    def __init__(self, model, color):
        self.model = model
        self.color = color


honda_color = ["Red", "White"]
honda = Car("Honda", honda_color)

deepcopy_honda = copy.deepcopy(honda)
deepcopy_honda.color.append("Green")
print("Deepcopy honda colors :", deepcopy_honda.color)
print("Original colors : ", honda.color)

shallow_honda = copy.copy(honda)
shallow_honda.color.append("Green")
print("Shallow copy honda colors :", shallow_honda.color)
print("Original colors : ", honda.color)