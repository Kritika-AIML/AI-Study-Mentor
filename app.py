from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    streak = 7
    xp = 450
    study_hours = 32
    goal = 70

    return render_template(
        "dashboard.html",
        streak=streak,
        xp=xp,
        study_hours=study_hours,
        goal=goal
    )

@app.route("/planner")
def planner():
    return render_template("planner.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/doubt")
def doubt():
    return render_template("doubt.html")

if __name__ == "__main__":
    app.run(debug=True)