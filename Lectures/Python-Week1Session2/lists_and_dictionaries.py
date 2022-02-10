user_one = {
    "first_name": "Devon",
    "last_name": "Newsom",
    "location": "Washington"
}

user_two = {
    "first_name": "James",
    "last_name": "Cayo",
    "location": "Connecticut"
}

users = [ user_one, user_two ]

# TODO: loop through list of dictionaries, display each kvp
for user in users:
    for key in user:
        print(f"{key} : {user[key]}")
        



# print(user_one["first_name"]) # "Devon"

# print(user_two["last_name"])

# looping through dictionaries
# [('first_name', 'Devon'), ('last_name', 'Newsom'), ('location', 'Washington')]
result = user_one.items()
just_keys = user_one.keys()

# for k, v in user_one.items():
#     print(f"{k} : {v}") 

# user_one["shoe_size"] = 10

# for k, v in user_one.items():
#     print(f"{k} : {v}") 