from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.director import Director

class Movie:
    db_name = 'movies_db'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        self.director_id = data['director_id']
        self.director = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies JOIN directors ON directors.id = movies.director_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        movies = []
        for result in results:
            print(result)
            # Create the movie object

            a_movie = cls(result)

            # Create the director object
            director_data = {
                'id': result['directors.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name']
            }
            # # Create the director object
            # director_data = {
            #     'id': result['directors.id'],
            #     'first_name': result['first_name'],
            #     'last_name': result['last_name']
            # }

            a_director = Director(director_data)

            # Associate the two objects together
            a_movie.director = a_director
            movies.append(a_movie)
        return movies

    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM directors WHERE id = %(id)s;"
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     return cls(results[0])

    @classmethod
    def create(cls, data):
        query = "INSERT INTO movies(title, release_date, director_id) VALUES(%(title)s, %(release_date)s, %(director_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def edit(cls, data):
    #     query = "UPDATE directors SET first_name=%(first_name)s, last_name=%(last_name)s WHERE id= %(id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def delete(cls, data):
    #     query="DELETE FROM directors WHERE id= %(id)s;"
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    
