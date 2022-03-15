from flask_app.config.mysqlconnection import connectToMySQL


# data = {'first_name': 'Sal', 'last_name': 'the instructor}
# a_director = Director(data)
# a_director = Director('Sal', 'The Instructor')
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

    
