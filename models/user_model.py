from flask_bcrypt import Bcrypt
from pymongo import MongoClient
import os

bcrypt = Bcrypt()

MONGO_URI = os.getenv("MONGO_URI")
print(f"Loaded MONGO_URI: {MONGO_URI}")
client = MongoClient(MONGO_URI)
db = client['AirPlanes']
users_collection = db['users']


class UserModel:
    def __init__(self, db):
        self.collection = db.users

    def create_user(self, full_name, email, phone, password):
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user_data = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "password": hashed_pw
        }
        self.collection.insert_one(user_data)

    def find_by_email(self, email):
        return self.collection.find_one({"email": email})
