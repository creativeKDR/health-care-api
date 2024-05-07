from flask import Blueprint, jsonify, request

from services.interpret_query_service import InterpreteQueryService
from utils.authorization import token_required

query = Blueprint('Query', __name__)


@query.route('/query', methods=['Post'])
@token_required
def get_query_data():
    data = request.json
    symptoms = data.get('symptoms')
    height = data.get('height')
    weight = data.get('weight')
    bloodPressure = data.get('bloodPressure')
    sugarLevel = data.get('sugarLevel')
    healthData = InterpreteQueryService.generatePrompt(symptoms=symptoms, height=height, weight=weight,
                                                       bloodPressure=bloodPressure, sugarLevel=sugarLevel)
    if not healthData:
        return jsonify({'message': 'Health Data not found', 'code': 404}), 404
    return jsonify({"result": healthData}), 200
