
from flask import Flask
import home
import planners

app = Flask(__name__)

app.register_blueprint(home.home_bp)
app.register_blueprint(planners.planner_bp)

if __name__ == "__main__":
    app.run(debug=True)