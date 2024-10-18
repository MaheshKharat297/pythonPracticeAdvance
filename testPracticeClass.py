class CarDesign:
    followers = 0
    def __init__(self, color, modal, type):
        self.color = color
        self.modal = modal
        self.type = type
        self.numberModels = 0

    def car(self):
        print(f"Here is your car with {self.color} color, {self.modal} model, {self.type} type")
        print("Number of models sold : ", self.numberModels)

    def update_followers(self):
        self.followers += 1




carDesign = CarDesign("Green", "1890", "4 wheeler")
carDesign.numberModels = 40
carDesign.car()
carDesign.update_followers()
carDesign.update_followers()
carDesign.update_followers()
print(carDesign.followers)

carDesign_2 = CarDesign("red", "2000", "6 wheeler")
carDesign_2.numberModels = 100
carDesign_2.car()
carDesign_2.update_followers()
print(carDesign_2.followers)

