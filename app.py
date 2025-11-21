from flask import Flask

from extensions import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:581321@localhost:3306/lab_1"

db.init_app(app)

with app.app_context():
    from my_project.route.river_route import bp as bp_river
    from my_project.route.region_route import bp as bp_region
    app.register_blueprint(bp_river)
    app.register_blueprint(bp_region)


if __name__ == "__main__":
    app.run(debug=True)
