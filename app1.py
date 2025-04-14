from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize Flask app
app = Flask(__name__)
# MongoDB connection (User model)
client = MongoClient("mongodb://localhost:27017/")  # Connect to local MongoDB
db = client["abc_airline_db"]  # Use or create the database
user_collection = db["users"]  # Use or create the collection for users

# Route for signup page
@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data from the signup form
        full_name = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['new-password']          # Fixed here
        confirm_password = request.form['confirm-password']  # And here


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
            return redirect(url_for('login'))  # Redirect to login page after successful signup
        else:
            return "Error during signup. Please try again."

    return render_template('signup.html')  # Render the signup form if GET request

# Route for the login page (redirect after successful signup)
@app.route('/login')
def login():
    return render_template('login.html')

# Route for fetching data from Supabase (e.g., viewing airport data)
@app.route('/view_airports')
def view_airports():
    data_response = supabase.table("airport").select("*").execute()

    # If successful, show the data; otherwise, show an error message
    if data_response.status_code == 200:
        return f"Airports Data: {data_response.data}"
    else:
        return f"Error fetching airports data: {data_response.error_message}"

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
