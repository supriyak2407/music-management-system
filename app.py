from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import jsonify
import pymysql

app = Flask('MyProject', template_folder='Templates')
app.secret_key = '3456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2407@127.0.0.1:3306/music'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    __tablename__ = 'users'

    User_ID = db.Column(db.Integer, primary_key=True)
    User_Name = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    User_Password = db.Column(db.String(512), nullable=False)  # Adjust the length as needed
    Date_Of_Birth = db.Column(db.Date, nullable=False)


# Explicitly create the table
with app.app_context():
    db.create_all()


# Routes


# ... other routes and functions ...
from sqlalchemy.sql import text

from sqlalchemy.engine import ResultProxy

@app.route('/execute_query', methods=['POST'])
def execute_query():
    if request.method == 'POST':
        query = request.form['query']

        # Execute the query using SQLAlchemy
        result = db.session.execute(text(query))

        # Convert the result to a list of dictionaries for easier rendering in HTML
        result_dict = [dict(row) if isinstance(row, ResultProxy) else row for row in result]

        return render_template('query_result.html', result=result_dict)

@app.route('/login')
def login():
    return render_template('login.html')


# ... other routes and functions ...

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/validate_login', methods=['POST'])
def validate_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Query the database to check if the credentials are valid
    user = User.query.filter_by(User_Name=username, User_Password=password).first()

    # Return JSON response indicating whether the login is valid
    return jsonify({'valid': user is not None})


@app.route('/signup_submit', methods=['POST'])
def signup_submit():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        date_of_birth = data.get('date_of_birth')

        # Simple form validation
        if not all([username, email, password, date_of_birth]):
            return jsonify({'success': False})

        # Check if the username is already taken
        existing_user = User.query.filter_by(User_Name=username).first()
        if existing_user:
            return jsonify({'success': False})

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new User
        new_user = User(User_Name=username, Email=email, User_Password=hashed_password, Date_Of_Birth=date_of_birth)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Log information about the new user (for debugging purposes)
        print(f"New user added: {new_user.User_Name}, {new_user.Email}, {new_user.Date_Of_Birth}")

        flash.clear()
        flash('Signup successful! Please log in.', 'success')
        return jsonify({'success': True})
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error during signup_submit: {str(e)}")
        flash('An error occurred during signup', 'error')
        return jsonify({'success': False})


@app.route('/musicmain')
def musicmain():
    return render_template('musicmain.html')


@app.route('/page2nd')
def page2nd():
    # Implement logic for musicpage2
    return render_template('page2nd.html')


@app.route('/albumhome')
def albumhome():
    # Implement logic for album
    return render_template('albumhome.html')


@app.route('/billboard')
def billboard():
    # Implement logic for billboard
    return render_template('billboard.html')


@app.route('/Favourites')
def Favourites():
    # Implement logic for favourites
    return render_template('Favourites.html')


@app.route('/playlist')
def playlist():
    # Implement logic for playlist
    return render_template('playlist.html')

@app.route('/query')
def query():
    return render_template('query.html')

@app.route('/datavisualisation')
def datavisualisation():
    # Implement logic for playlist
    return render_template('datavisualisation.html')
if __name__ == '__main__':
    app.run(debug=True)