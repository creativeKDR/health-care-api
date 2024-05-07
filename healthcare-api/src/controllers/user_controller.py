from flask import Blueprint, request, jsonify
from werkzeug.exceptions import HTTPException

from services.user_service import UserService
from utils.authorization import token_required

user = Blueprint('user', __name__)


@user.route('/users/<string:user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found', 'code': 404}), 404
    return jsonify(user.serialize()), 200


@user.route('/users', methods=['GET'])
@token_required
def get_all_user():
    users = UserService.get_users()
    serialized_users = [user.serialize() for user in users]
    if not serialized_users:
        return jsonify({'message': 'Users not found', 'code': 404}), 404
    return jsonify(serialized_users), 200


@user.route('/users', methods=['POST'])
def create_user():
    data = request.json
    userName = data.get('userName')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')
    gender = data.get('gender')
    height = data.get('height')
    weight = data.get('weight')
    medicalConditions = data.get('medicalConditions')
    try:
        new_user = UserService.create_user(userName, email, password, age, gender, height, weight, medicalConditions)
    except HTTPException as e:
        return jsonify({'message': e.description, 'code': e.code}), e.code
    return jsonify({'message': 'User created successfully', 'user_id': new_user.ID}), 201


@user.route('/users/<string:user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    data = request.json
    try:
        updated_user = UserService.update_user(user_id, **data)
    except HTTPException as e:
        return jsonify({'message': e.description, 'code': e.code}), e.code
    if updated_user:
        return jsonify({'message': 'User updated successfully', 'user': updated_user.serialize()}), 200
    return jsonify({'message': 'User not found', 'code': 404}), 404

