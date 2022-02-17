from my_classes.ninja import Ninja
from my_classes.pet import Pet

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
tiger = Pet("Growler", "Tiger", "ROAR")
donatello = Ninja("Donatello", "Turtle", tiger, ["pizza", "cookies"], "regular pet food")

# Have the Ninja feed, walk , and bathe their pet.
donatello.walk()
donatello.feed()
donatello.bathe()