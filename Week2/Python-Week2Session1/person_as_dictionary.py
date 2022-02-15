
# Representing a "Person" as a dictionary
user_dict = {
    "first_name": "Devon",
    "last_name": "Newsom"
}

# Pros:
#   - 'flexible', new key/value pairs could be added if neccessary
#   - simple, no additional code needed

# Cons:
#   - 'unpredictable', new key/value pairs could be added if neccessary!
#   - limited, unable to provide any custom behavior


# TODO: Create a custom Python class to represent this example!
# attribues: what a class "contains"
# methods: what a class "does"


class Person:
    # attribues: first_name, last_name
        # when we build each person!
    def __init__(self, first_name, last_name): # Constructor method
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(f"{self.first_name} {self.last_name}")

    def say_greeting(self, greeting):
        print(f"{greeting} - says {self.first_name}")

some_person = Person("Rachel", "Smith")

class Car:
    # generic function to convert miles to km
    @staticmethod
    def miles_to_km(miles):
        return miles * 1.60934

    @classmethod
    def car_factory(cls, owner):
        # in a classmethod, we have a default parameter to refer to the class itself
        #   cls -> Car
        #   we can do things like construct a bunch of Car objects!!
        return [cls("Volvo", "240", owner), cls("Volvo", "240", owner), cls("Volvo", "240", owner)]
       

    def __init__(self, make, model, person):
        # attributes
        self.make = make
        self.model = model
        # model
        self.odometer = 0
        self.owner = person
    
    def drive(self, num_miles):
        self.odometer += num_miles

some_car = Car("Toyota", "Camry", some_person)

Car.car_factory(some_person)