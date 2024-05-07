from flask import Blueprint, request, jsonify
from werkzeug.exceptions import HTTPException

from services.login_service import LoginService

login = Blueprint('login', __name__)


@login.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    try:
        user = LoginService.authenticate_user(email, password)
    except HTTPException as e:
        return jsonify({'message': e.description, 'code': e.code}), e.code
    return jsonify(user), 200
