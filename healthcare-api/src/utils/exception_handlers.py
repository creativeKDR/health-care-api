from werkzeug.exceptions import HTTPException


class UserNotFoundException(HTTPException):
    code = 404
    description = 'User not found'


class InvalidCredentialException(HTTPException):
    code = 403
    description = 'Password not matching'
