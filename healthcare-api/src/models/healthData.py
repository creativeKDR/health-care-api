from models import db


class HealthData(db.Model):
    __tablename__ = 'HealthData'

    ID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.String(36), db.ForeignKey('User.ID'), nullable=False)
    CreatedAt = db.Column(db.DateTime, nullable=False)
    HeartRate = db.Column(db.Integer)
    BloodPressure = db.Column(db.String(20))
    BloodSugarLevel = db.Column(db.Integer)
    Symptoms = db.Column(db.Text)
    Medication = db.Column(db.String(200))
    SleepDuration = db.Column(db.Integer) 

    def serialize(self):
        return {
            'id': self.ID,
            'userId': self.UserID,
            'createdAt': self.CreatedAt,
            'heartRate': self.HeartRate,
            'bloodPressure': self.BloodPressure,
            'bloodSugarLevel': self.BloodSugarLevel,
            'symptoms': self.Symptoms,
            'medication': self.Medication,
            'sleepDuration': self.SleepDuration,
        }