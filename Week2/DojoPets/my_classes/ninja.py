class Ninja:
    # first_name
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name # Donatello
        self.last_name = last_name
        self.pet = pet # <Pet >
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        # print name of Ninja!
        print(f"{self.first_name} is going for a walk!")
        # walks the ninja's pet 
        #   invoking the pet play() method
        self.pet.play()


    def feed(self):
        # feeds the ninja's pet invoking the pet eat() method
        print(f"{self.first_name} is feeding the pet!")
        self.pet.eat()

    def bathe(self):
        # cleans the ninja's pet invoking the pet noise() method
        print(f"{self.first_name} is bathing the pet!")
        self.pet.noise()


        

