from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Classes
# Update the File class in your models.py or wherever you define your database models

class File(db.Model):
    """File class"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(50), nullable=True)  # Add a new field for role

    def __repr__(self):
        return f"File('{self.title}', '{self.description}', '{self.role}')"


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def landingPage():
    return render_template("land.html")

@app.before_request
def create_tables():
    db.create_all()
    # sample_item = File(title='Sample Item', description='This is a sample item.')
    # db.session.add(sample_item)
    # db.session.commit()

@app.route('/index')
def file_index():
    files = File.query.all()
    return render_template('index.html', files=files)

@app.route('/files/<int:file_id>')
def read_file(file_id):
    file = File.query.get_or_404(file_id)
    return render_template('read.html', file=file)

@app.route('/files/create', methods=['GET', 'POST'])
def create_file():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        role = request.form['role']

        new_item = File(title=title, description=description, role=role)
        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for('file_index'))

    return render_template('create_file.html')
