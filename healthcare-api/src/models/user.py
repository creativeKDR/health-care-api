from models import db


class User(db.Model):
    __tablename__ = 'User'

    ID = db.Column(db.String(36), primary_key=True)
    UserName = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(10))
    Height = db.Column(db.Float)
    Weight = db.Column(db.Float)
    MedicalConditions = db.Column(db.String(200))

    health_data = db.relationship('HealthData', backref='user', lazy=True)

    def serialize(self):
        return {
            'id': self.ID,
            'userName': self.UserName,
            'email': self.Email,
            'age': self.Age,
            'gender': self.Gender,
            'height': self.Height,
            'weight': self.Weight,
            'medicalConditions': self.MedicalConditions,
        }
