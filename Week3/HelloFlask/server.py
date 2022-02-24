from flask import Flask, render_template

app = Flask(__name__)



# localhost:5000
@app.route("/")
def index():
    example_db_data = [
        { "id": 1, "first_name": "Marge", "last_name": "Simpson"},
        { "id": 2, "first_name": "Homer", "last_name": "Simpson"},
        { "id": 3, "first_name": "Lisa", "last_name": "Simpson"},
        { "id": 4, "first_name": "Bart", "last_name": "Simpson"},
        { "id": 5, "first_name": "Hans", "last_name": "Moleman"},
    ]
    return render_template("index.html", users=example_db_data)

# localhost:5000/greeting/jaron
# localhost:5000/greeting/taro
# localhost:5000/greeting/rachel
@app.route("/greeting/<guest>")
def greeting(guest):
    print(guest)
    return render_template("sup.html", user=guest)


if __name__ == "__main__":
    app.run(debug=True)