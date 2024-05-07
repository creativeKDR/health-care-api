from models import db
from models.healthData import HealthData
from utils.utilities import Utilities


class HealthDataService:

    @staticmethod
    def get_health_data_by_id(health_data_id):
        # fetch health data by using healthId
        return HealthData.query.get(health_data_id)

    @staticmethod
    def get_health_data_by_userId(userId):
        # fetch health data by using userId
        return HealthData.query.filter_by(UserID=userId).first()

    @staticmethod
    def get_health_data():
        # fetch all health data
        return HealthData.query.all()

    @staticmethod
    def create_health_data(userId, heartRate=None, bloodPressure=None, bloodSugarLevel=None, symptoms=None,
                           medication=None, sleepDuration=None):
        # Create a new health data instance
        new_health_data = HealthData(ID=Utilities.generateUUID(), UserID=userId, CreatedAt=Utilities.generateTimeStamp(),
                                     HeartRate=heartRate, BloodPressure=bloodPressure, Symptoms=symptoms,
                                     BloodSugarLevel=bloodSugarLevel, Medication=medication,
                                     SleepDuration=sleepDuration)
        # Add the health data to the session and commit the transaction
        db.session.add(new_health_data)
        db.session.commit()
        return new_health_data

    @staticmethod
    def update_health_data(health_data_id, **kwargs):
        # fetch health data by using healthId and update fields
        healthData = HealthData.query.get(health_data_id)
        if healthData:
            for key, value in kwargs.items():
                setattr(healthData, key, value)
            db.session.commit()
            return healthData
        return None
