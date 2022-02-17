"""
    write a function that takes in a list of numbers
    return the most commonly found number

    input: [2,5,76,21,2,5,2]
    out: 2

    input: [2,2,3,3,3,2]
    out: 3
"""

def most_common_dupe(numbers): # [2,5,76,21,2,5,2,6]
    # create empty dictonary to hold on to
        # each number in "numbers" as a key
        # a running count of each of those number's occurences in the list
    numbers_map = {}

    # numbers_map {
    #   2: 3,
    #   5: 2,
    #   76: 1,
    #   21: 1
    #   6: 1
    # }

    
    # vals: [3,2,1,1,1]

    # loop through list of numbers
    for num in numbers:

        # if 'num' is already a key in our numbers_map
        if num in numbers_map:
            # we can increment its value by 1
            numbers_map[num] += 1
        # if 'num' is not yet a key
        else:
            # we can create a new 'key value pair', giving 1 as its inital value
            numbers_map[num] = 1
    
    # once loop (above) is complete, 
    #   we have a full mapping of each number and it's number of occcurences

    # now we just need to find which key in this numbers_map dictionary
    #   contains the largest value

    # we can start by creating a list that contains only the keys
    numbers_map_keys = list(numbers_map.keys())
    # keys: [2,5,76,21,6]
    # from this list of keys, we can grab the first item as our temporary "max_num"
    max_num = [0]
    # now we can loop through this list of keys
    #   to find the key that is mapped to the largest value
    for key in numbers_map_keys:
        # if we find that a key's value is larger than our current one
        if numbers_map[key] > numbers_map[max_num]:
            # we can update our current max_num
            max_num = key
        
    return max_num 

most_common_dupe([2,5,76,21,2,5,2,6])