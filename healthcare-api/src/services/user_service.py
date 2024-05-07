from models import db
from models.user import User
from utils.authorization import auth
from utils.utilities import Utilities


class UserService:

    @staticmethod
    def get_user_by_id(user_id):
        # fetch user data by using userId
        return User.query.get(user_id)

    @staticmethod
    def get_users():
        # fetch all users data
        return User.query.all()

    @staticmethod
    def create_user(userName, email, password, age=None, gender=None, height=None, weight=None, medicalConditions=None):
        # Create a new user instance
        new_user = User(ID=Utilities.generateUUID(), UserName=userName, Email=email,
                        Password=auth.hash_password(password), Age=age,
                        Gender=gender, Height=height, Weight=weight, MedicalConditions=medicalConditions)
        # Add the user to the session and commit the transaction
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user(user_id, **kwargs):
        # fetch user data by using userId and update fields
        user = User.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        return None


