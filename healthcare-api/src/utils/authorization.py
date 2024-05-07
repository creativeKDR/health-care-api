import datetime
from functools import wraps

import jwt
from flask import request, jsonify

from utils import config
from utils.aesEncryption import AESCipher


class Authorization:

    def create_access_token(self, *, authUser: dict) -> str:
        return self._create_token(
            lifetime=datetime.timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES),
            authUser=authUser,
        )

    def _create_token(self, lifetime: datetime.timedelta, authUser: dict) -> str:
        # authorization token generator
        payload = {}
        expire = datetime.datetime.utcnow() + lifetime
        payload["iss"] = config.TokenAuthentication['Issuer']
        payload["aud"] = config.TokenAuthentication['Audience']
        payload["exp"] = expire
        payload["iat"] = datetime.datetime.utcnow()
        payload["authUser"] = authUser

        return jwt.encode(payload, config.TokenAuthentication['SecretKey'], algorithm=config.ALGORITHM)

    def hash_password(self, password: str) -> str:
        iv = bytearray(16)
        key = config.PasswordHelper
        cipher = AESCipher(key, iv)
        encrypted_data = cipher.encrypt(password)
        return encrypted_data.decode('utf-8')

    def decrypt_password(self, password: str) -> str:
        iv = bytearray(16)
        key = config.PasswordHelper
        cipher = AESCipher(key, iv)
        decrypted_data = cipher.decrypt(password.encode('utf-8'))
        return decrypted_data


# authorization token decryption decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        bearer_token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            bearer_token = auth_header.split('Bearer ')[1]
        if not bearer_token:
            return jsonify({'message': 'Authorization Token is missing'}), 403
        try:
            jwt.decode(bearer_token.encode("utf-8"),
                       issuer=config.TokenAuthentication['Issuer'],
                       algorithms=config.ALGORITHM,
                       audience=config.TokenAuthentication['Audience'],
                       key=config.TokenAuthentication['SecretKey'],
                       options={"verify_signature": True},
                       )
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Authorization Token expired, log in again'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid authorization token. Please log in again.'}), 403

        return f(*args, **kwargs)

    return decorated


auth = Authorization()
