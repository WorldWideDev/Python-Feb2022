# String

# What are strings useful for?
# - connect different data types together??
# messages, names, prompts (to users)
# human readable text
# What can we do with strings?

message = "YOU SHALL NOT PASS"
messanger = "Gandolf"

# f-strings can include variables
combined_message = f"{message} -{messanger} ({10} is a good number)"
# print(combined_message)
# contatenation: using "+" to combine strings
concat_message = message + " -" + messanger

# grab first character of a string
# print(message[0])

# access the length of a string with len()
len_of_message = len(message)
# print(len_of_message)

# loop through
for i in range(len_of_message):
    print(message[i])

# Number

# What are numbers useful for?
# arithmatic
    # +, -, /, *, %
# What can we do with numbers?


# Boolean

# What are booleans useful for?
# What can we do with booleans?
# display all odd numbers from 0 - 10
for i in range(10):
    if i%2 == 1:
        print(i)

# print all numbers between 0 - x, that are evenly divisible by y
def print_number_machine(upper_limit, divisible_by):
    for i in range(upper_limit):
        if i%divisible_by == 0:
            print(i)


print_number_machine(15,3)
print_number_machine(10000,100)

# Syntax
    # code blocks (if statements, functions, classes, loops(for, while))
        # indentation will dictate what is/isn't a code block