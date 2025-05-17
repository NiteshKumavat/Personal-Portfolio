from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///responses.db'

db = SQLAlchemy(app)

class responses(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(500), nullable=True)
    message = db.Column(db.String(20000), nullable=False)


with app.app_context():
    db.create_all() 


projects = {
    "Python": {
        "Clock": [
            "An alarm clock application developed using Python's GUI capabilities.",
            "assets/clock.png"
        ],
        "GUI_Hangman": [
            "A Hangman game implemented with a graphical user interface using Tkinter.",
            "assets/hangman.png"
        ],
        "To-Do-List": [
            "A beginner-friendly to-do list application for managing tasks.",
            "assets/to-do-list.png"
        ],
        "Weather_GUI": [
            "A weather application that demonstrates API integration and OOP concepts using Tkinter.",
            "assets/wheather.jpg"
        ]
    },
    "Java": {
        "Quiz-Application": [
            "A quiz application built in Java for managing and attempting quizzes.",
            "assets/quiz.png"
        ]
    }
}


@app.route("/")
def home() :        
    return render_template("index.html")

@app.route("/index.html")
def index() :
    return render_template("index.html")

@app.route("/project.html")
def project() :
    return render_template("project.html", projects=projects)

@app.route("/contact.html", methods=["GET", "POST"])
def contact() :
    if request.method == "POST" :
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        data = responses(name=name, email=email, subject=subject, message=message)
        db.session.add(data)
        db.session.commit()
        return render_template("contact.html", reply=True)



    return render_template("contact.html", reply=False)

@app.route('/resume')
def resume() :
    return send_from_directory(
        directory=os.path.join(app.root_path, 'static/files'),
        path='resume.pdf',
        as_attachment=True
    )
if __name__ == '__main__' :
    app.run(debug=True)