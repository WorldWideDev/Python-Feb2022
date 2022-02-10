
"""
    Countdown - Create a function that accepts a number as an input. 
    Return a new list that counts down by one, 
        from the number (as the 0th element) down to 0 (as the last element).
"""

def count_town(number):
    # input: 10
    # output: [10,9,8,7,6,5,4,3,2,1,0]
    output_list = []
    #            start stop increment
    for x in range(number, -1, -1):
        output_list.append(x) # [10, 9, 8 ...]

    return output_list

result = count_town(10)
print(result)

"""
Values Greater than Second - 
    Write a function that accepts a list and creates a new list containing only 
    the values from the original list that are greater than its 2nd value. 

    Print how many values this is and then return the new list. 
    If the list has less than 2 elements, have the function return False
"""
def greater_than_second(numbers): # numbers: [2,4,6,32,4]
    if len(numbers) < 2:
        return False

        

    second_value = numbers[1]
    output = []

    # for i in range(0, len(numbers)):
    for number in numbers:
        if number > second_value:
            output.append(number)

    return output

greater_than_second([2,4,6,32,4])