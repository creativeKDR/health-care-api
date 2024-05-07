from datetime import datetime, timedelta

from models.user import User
from utils import config
from utils.authorization import auth
from utils.exception_handlers import UserNotFoundException, InvalidCredentialException


class LoginService:

    @staticmethod
    def authenticate_user(email, password):
        # fetch user by email if it presents in database
        user = User.query.filter_by(Email=email).first()
        if not user:
            raise UserNotFoundException()
        # if user found then decrypting the user password
        hash_password = auth.decrypt_password(user.Password)
        if password != hash_password:
            raise InvalidCredentialException()
        token_claims = {"id": user.ID,
                        "userName": user.UserName,
                        "email": user.Email}
        return {
            "accessToken": auth.create_access_token(authUser=token_claims),
            "expiresAt": datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES),
            "userId": user.ID,
            "userName": user.UserName}
