# tiger = Pet("Growler", "Tiger", "ROAR")
class Pet:
    default_health = 100
    default_energy = 50
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.energy = Pet.default_energy
        self.health = Pet.default_health

    def sleep(self):
        # restores back to default health
        self.health = Pet.default_health
        print(f"{self.name}'s health is restored!")

    def eat(self):
        self.energy += 5
        self.health += 10
        

    def play(self):
        self.health += 5
        

    def noise(self):
        print(self.sound)