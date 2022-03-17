from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Opinion:
    db = "feb_belt_exam_prep"
    def __init__(self, data):
        self.id = data['id']
        self.movie_title = data['movie_title']
        self.experience = data['experience']
        self.date_watched = data['date_watched']
        self.rating = data['rating']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    @classmethod
    def create_opinion(cls, data):
        query = "INSERT INTO opinions(movie_title, experience, date_watched, rating, user_id) VALUES(%(movie_title)s, %(experience)s, %(date_watched)s, %(rating)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM opinions"
        results = connectToMySQL(cls.db).query_db(query)
        opinions = []
        for row in results:
            opinions.append(cls(row))
        return opinions
    
    @classmethod
    def get_one(cls, data):
        query= "SELECT * FROM opinions JOIN users ON user_id = users.id WHERE opinions.id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        opinion = cls(row)
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at'],
        }
        user = User(user_data)
        opinion.user = user
        return opinion

    @classmethod
    def update(cls, data):
        query = "UPDATE opinions SET movie_title=%(movie_title)s, experience=%(experience)s, date_watched=%(date_watched)s, rating=%(rating)s WHERE id= %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query="DELETE FROM opinions WHERE id= %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_opinion(opinion):
        isValid = True
        if len(opinion['movie_title']) < 2:
            flash("Movie Title must be at least 3 characters", "error")
            isValid = False
        if len(opinion['experience']) < 2:
            flash("Experience must be at least 3 characters", "error")
            isValid = False
        return isValid


    