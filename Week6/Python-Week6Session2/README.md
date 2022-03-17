# Python - Week 6 Session 2
# Agenda
1. Class calendar, assignment & discussion reminders
    - [Stack Schedule](https://docs.google.com/spreadsheets/d/1R8Pj8DblfmmpihO34Cn0J_FjMZz_6zkPZC9v_lnqL4s/edit#gid=2097812438)
    - [Login and Registration](https://login.codingdojo.com/m/309/9262/62428)
    - [Recipes](https://login.codingdojo.com/m/309/9263/62433)
    - [Belt Exam](https://login.codingdojo.com/m/309/9263/62432)
    - [Discussions](https://login.codingdojo.com/d/309/124/1200)
2. Review
    - [Validations](https://login.codingdojo.com/m/309/9261/62404)
    - [Login and Registration](https://login.codingdojo.com/m/309/9256/62366)
3. Belt Exam Review
    - Must submit 15 out of the 16 assignments for the stack
    - Before starting, make sure to complete Login and Registration(you can create a copy of your log/reg and build the belt exam on top)
    - Wireframe
    - EXAMPLE
     - instead of recipes, movie tracker, experience
     - title(VARCHAR), experience(TEXT), rating(INT), date_watched(DATETIME), user_id(INT - foreign key)
    - Start thinking about MVC(Models, Views, Controllers)
        - Models
            - users? first_name? last_name? email? password? created_at updated_at
            - What is going to have a relationship with users?  What is being CRUD in the wireframe
            - ERD - add new table to existing log_and_reg ERD
            - SQL Query
            - Flask Model
            - What is being returned? One object? List of objects, ID?
            - used by the controller to get data
        - Views
            - templates in flask_app
            - HTML
            - Controller decides if route ends in the rendering of an HTML template
        - Controllers
            - Has access to information such as data from form, path params, etc.
            - Calls Flask model class methods to get data
            - Ends controller method with either a redirect(to another route that will render) or renders a HTML template
    - Start Coding
        - Get the Flask app up and running before going too deep into the code (make sure virtual environment has flask-bcrypt and PyMySQL installed)
            - Go into project folder
            - pipenv shell, 
            - pipenv install flask-bcrypt PyMySQL
            - copy over flask_app and server.py from log and reg app
            - python server.py
        - Login and registration should work independent of any additions to the ERD or code
    
5. Homework
    - [Login and Registration](https://login.codingdojo.com/m/309/9262/62428)
    - [Recipes](https://login.codingdojo.com/m/309/9263/62433)

