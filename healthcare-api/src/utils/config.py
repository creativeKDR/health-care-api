userName = 'dbAdmin'
password = 'localDb#123'
dbName = 'healthcare_db'
SQLALCHEMY_DATABASE_URI = f'mysql://{userName}:{password}@localhost/{dbName}'

# Password Helper
PasswordHelper = "QTdIBCPpxA103nxx"

ALGORITHM = "HS512"

# 60 minutes * 24 hours * 1 day = 1 day
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1

TokenAuthentication = {
    "SecretKey": "HealthCare_JsonWebToken_Authentication_Security_Signature_Key",
    "Issuer": "HealthCareIssuer",
    "Audience": "HealthCareAudience",
    "TokenPath": "/api/token",
    "CookieName": "access_token"
}