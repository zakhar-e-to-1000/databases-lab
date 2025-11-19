from flask import Flask

from extensions import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:581321@localhost:3306/lab_1"

db.init_app(app)

# Імпорти після ІНІЦІАЛІЗАЦІЇ db
with app.app_context():
    from my_project.route.river_route import bp as bp_river
    app.register_blueprint(bp_river)


if __name__ == "__main__":
    app.run(debug=True)
