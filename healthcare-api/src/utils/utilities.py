import uuid
from datetime import datetime


class Utilities:

    @staticmethod
    def generateUUID():
        return str(uuid.uuid4())

    @staticmethod
    def generateTimeStamp():
        return datetime.now()
