def max_of_list(numbers):
    # [2,5,1,456,2,200]
    # get a variable for temporary 'max'
    current_max = numbers[0]

    # loop through numbers
    for num in numbers:
        # if we find a number bigger than current max
        if num > current_max:
            current_max = num
        # we have a new current_max!
    return current_max