from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

auth_bp = Blueprint('auth', __name__)

# MongoDB connection using Atlas URI
MONGO_URI = os.getenv("MONGO_URI")
print(f"Loaded MONGO_URI: {MONGO_URI}")
client = MongoClient(MONGO_URI)
db = client['AirPlanes']
users_collection = db['users']

# SIGNUP
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['new-password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for('auth.signup'))

        if users_collection.find_one({'email': email}):
            flash("Email already exists. Please use a different email.", "error")
            return redirect(url_for('auth.signup'))

        hashed_password = generate_password_hash(password)

        user = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "password": hashed_password
        }

        users_collection.insert_one(user)
        flash("Signup successful! Please log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

# LOGIN
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_collection.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            session['user'] = user['email']
            flash("Login successful!", "success")
            return redirect(url_for('view.home'))  # Adjust if your home route is different
        else:
            flash("Invalid email or password", "error")
            return redirect(url_for('auth.login'))

    return render_template('login.html')
