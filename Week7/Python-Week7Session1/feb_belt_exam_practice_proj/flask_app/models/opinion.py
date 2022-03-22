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
        self.users_who_favorited = []
    
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
    def get_all_with_favorites(cls):
        query= "SELECT * FROM opinions JOIN users ON users.id=opinions.user_id "\
                "LEFT JOIN favorited_opinions ON opinions.id = favorited_opinions.opinion_id "\
                "LEFT JOIN users AS users2 ON users2.id = favorited_opinions.user_id "\
                "ORDER BY opinions.created_at DESC; "\

        results = connectToMySQL(cls.db).query_db(query)
        opinions = [] 
        for result in results:
            new_opinion = True
            like_user_data = {
                "id" : result["users2.id"],
                "first_name": result["users2.first_name"],
                "last_name": result["users2.last_name"],
                "email": result["users2.email"],
                "password": result["users2.password"],
                "created_at": result["users2.created_at"],
                "updated_at": result["users2.updated_at"]
            }
            # opinions have been added, and the last one added is the same opinion as the current row(multiple users who liked)
            if len(opinions) > 0 and opinions[len(opinions)-1].id == result['id']:
                opinions[len(opinions)-1].users_who_favorited.append(User(like_user_data))
                new_opinion = False

            if new_opinion:
                opinion = cls(result)

                #Put all relevant user information into a new data dictionary
                user_data = {
                    'id': result['users.id'],
                    'first_name': result['first_name'],
                    'last_name': result['last_name'],
                    'email': result['email'],
                    'password': result['password'],
                    'created_at': result['users.created_at'],
                    'updated_at': result['users.updated_at'],
                }
                #Create a user object with the user data
                user = User(user_data)


                # Set user attribute in opinion object to the newly created user object
                opinion.user = user

                # if there is a user who liked, then add it to the list
                if result['users2.id'] is not None:
                    opinion.users_who_favorited.append(User(like_user_data))
                opinions.append(opinion)
        return opinions

    @classmethod
    def get_all_user_favorited_opinions(cls, data):
        opinions_liked = []
        query="SELECT opinion_id FROM favorited_opinions JOIN users ON users.id=user_id WHERE user_id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        for result in results:
            opinions_liked.append(result['opinion_id'])
        return opinions_liked


        
    
    @classmethod
    def get_one(cls, data):
        query= "SELECT * FROM opinions JOIN users ON user_id = users.id WHERE opinions.id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        #Create an opinion object based off of the results of the query
        opinion = cls(row)

        #Put all relevant user information into a new data dictionary
        user_data = {
            'id': row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at'],
        }
        #Create a user object with the user data
        user = User(user_data)
        # Set user attribute in opinion object to the newly created user object
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

    @classmethod
    def like(cls, data):
        query="INSERT INTO favorited_opinions(user_id, opinion_id) VALUES(%(user_id)s,%(opinion_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def dislike(cls, data):
        query="DELETE FROM favorited_opinions WHERE opinion_id=%(opinion_id)s AND user_id=%(user_id)s;"
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


    