from flask import Blueprint, request, jsonify
from werkzeug.exceptions import HTTPException

from services.health_data_service import HealthDataService
from utils.authorization import token_required

health_data = Blueprint('healthData', __name__)


@health_data.route('/health/<string:health_data_id>', methods=['GET'])
@token_required
def get_health_data(health_data_id):
    healthData = HealthDataService.get_health_data_by_id(health_data_id)
    if not healthData:
        return jsonify({'message': 'Health Data not found', 'code': 404}), 404
    return jsonify(healthData.serialize()), 200


@health_data.route('/health/users/<string:userId>', methods=['GET'])
@token_required
def get_health_data_by_userId(userId):
    healthData = HealthDataService.get_health_data_by_userId(userId)
    if not healthData:
        return jsonify({'message': 'Health Data not found', 'code': 404}), 404
    return jsonify(healthData.serialize()), 200


@health_data.route('/health', methods=['GET'])
@token_required
def get_all_health_data():
    healthData = HealthDataService.get_health_data()
    serialized_healthData = [data.serialize() for data in healthData]
    if not serialized_healthData:
        return jsonify({'message': 'Health Data not found', 'code': 404}), 404
    return jsonify(serialized_healthData), 200


@health_data.route('/health', methods=['POST'])
@token_required
def create_health_data():
    data = request.json
    userId = data.get('userId')
    heartRate = data.get('heartRate')
    bloodPressure = data.get('bloodPressure')
    bloodSugarLevel = data.get('bloodSugarLevel')
    symptoms = data.get('symptoms')
    medication = data.get('medication'),
    sleepDuration = data.get('sleepDuration')
    try:
        new_health_data = HealthDataService.create_health_data(userId, heartRate, bloodPressure, bloodSugarLevel,
                                                               symptoms,
                                                               medication, sleepDuration)
    except HTTPException as e:
        return jsonify({'message': e.description, 'code': e.code}), e.code
    return jsonify({'message': 'Health Data created successfully', 'health_data_id': new_health_data.ID}), 201


@health_data.route('/health/<string:health_data_id>', methods=['PUT'])
@token_required
def update_health_data(health_data_id):
    data = request.json
    try:
        updatedHealthData = HealthDataService.update_health_data(health_data_id, **data)
    except HTTPException as e:
        return jsonify({'message': e.description, 'code': e.code}), e.code
    if updatedHealthData:
        return jsonify({'message': 'Health data updated successfully', 'health': updatedHealthData.serialize()}), 200
    return jsonify({'message': 'Health Data not found', 'code': 404}), 404
