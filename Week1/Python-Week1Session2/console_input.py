# we can get input from console with

# collect three names
status = "play"
names = []
while status != "quit":

    print("type your name:")
    name = input()
    print(f"Hello, {name}!")
    names.append(name)

    print("would you like to continue? enter quit to exit")
    status = input()

    
print(names)