from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


# data = {'first_name': 'Sal', 'last_name': 'the instructor}
# a_director = Director(data)
# a_director = Director('Sal', 'The Instructor')

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Director:
    db_name = 'movies_db'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM directors;"
        results = connectToMySQL(cls.db_name).query_db(query)
        directors = []
        for director in results:
            # Director(director) -> Director({id: 1, first_name=sal, ....})
            directors.append(cls(director))
        return directors

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM directors WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO directors(first_name, last_name) VALUES(%(first_name)s, %(last_name)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE directors SET first_name=%(first_name)s, last_name=%(last_name)s WHERE id= %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query="DELETE FROM directors WHERE id= %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_director(director):
        is_valid = True
        if len(director['first_name']) < 2: 
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(director['last_name']) < 2: 
            flash("Last name must be at least 2 characters")
            is_valid = False  

        if not EMAIL_REGEX.match(director['first_name']): 
            flash("First name is an invalid email address!")
            is_valid = False      

        # if valid, is_valid will return True, if not, is_valid will return False
        return is_valid

        # is_valid = True # we assume this is true
        # if len(burger['name']) < 3:
        #     flash("Name must be at least 3 characters.")
        #     is_valid = False
        # if len(burger['bun']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        # if int(burger['calories']) < 200:
        #     flash("Calories must be 200 or greater.")
        #     is_valid = False
        # if len(burger['meat']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        # return is_valid
    
