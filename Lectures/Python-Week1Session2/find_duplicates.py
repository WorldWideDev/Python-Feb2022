"""
    write a function that takes in a list of numbers
    return the most commonly found number

    input: [2,5,76,21,2,5,2]
    out: 2

    input: [2,2,3,3,3,2]
    out: 3
"""

def most_common_dupe(numbers): # [2,5,76,21,2,5,2,6]
    numbers_map = {}
    for num in numbers:
        if num in numbers_map:
            numbers_map[num] += 1
        else:
            numbers_map[num] = 1
    
    max_num = list(numbers_map.keys())[0]
    for k in numbers_map.keys():
        if numbers_map[k] > numbers_map[max_num]:
            max_num = k
        
    return max_num 

most_common_dupe([2,5,76,21,2,5,2,6])