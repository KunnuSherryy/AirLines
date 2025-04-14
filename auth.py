from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from pymongo import MongoClient

# Initialize blueprint
auth_bp = Blueprint('auth', __name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["abc_airline_db"]
user_collection = db["users"]

# Route for signup page
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data from the signup form
        full_name = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['new-password']
        confirm_password = request.form['confirm-password']

        # Check if passwords match
        if password != confirm_password:
            return "Passwords do not match. Please try again."

        # Hash the password for security
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert data into MongoDB (User model)
        user = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "password": hashed_password
        }

        # Insert the user into the collection
        result = user_collection.insert_one(user)

        # Handle the response
        if result.inserted_id:
            return redirect(url_for('view.home'))  # Redirect to login page after successful signup
        else:
            return "Error during signup. Please try again."

    return render_template('signup.html')  # Render the signup form if GET request

# Route for the login page (redirect after successful signup)
@auth_bp.route('/login')
def login():
    return render_template('login.html')


# blueprints/airports.py (Airport data blueprint)
from flask import Blueprint, jsonify
from pymongo import MongoClient

# Initialize blueprint
airport_bp = Blueprint('airport', __name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["abc_airline_db"]

# Route for viewing airports
@airport_bp.route('/')
def view_airports():
    try:
        # Assuming we store airport data in MongoDB instead of Supabase
        airports = list(db.airports.find({}, {'_id': 0}))  # Exclude MongoDB ObjectId
        return jsonify(airports)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Directory structure for templates:
# templates/
#   auth/
#     signup.html
#     login.html
