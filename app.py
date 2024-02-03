from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Classes

@app.route('/')
def landingPage():
    return render_template("land.html")

if __name__ == '__main__':
    app.run(debug=True)
