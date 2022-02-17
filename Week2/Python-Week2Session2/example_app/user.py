class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]

    #NOTE: this will look slightly different when we are acutally connecting to database
    @classmethod
    def user_factory(cls, db_data):
        user_list = []
        #TODO: convert list of dictionaries to list of Users!

        # use a for loop that appends to the user_list and then return user_list

        # db_data is a list
        for row in db_data:
            # row is a dictionary
            # cls == User
            user_list.append(cls(row))
        
        return user_list


# SELECT * FROM users; => 
example_db_data = [
    { "id": 1, "first_name": "Marge", "last_name": "Simpson"},
    { "id": 2, "first_name": "Homer", "last_name": "Simpson"},
    { "id": 3, "first_name": "Lisa", "last_name": "Simpson"},
    { "id": 4, "first_name": "Bart", "last_name": "Simpson"},
    { "id": 5, "first_name": "Hans", "last_name": "Moleman"},
]

some_user = User({ "id": 1, "first_name": "Marge", "last_name": "Simpson"})