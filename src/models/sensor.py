import uuid
from datetime import datetime

from src.Database import Database


class Sensor(object):

    def __init__(self, longitude, latitude, type, status,
                 start_time=datetime.utcnow(),
                 end_time=datetime.utcnow(),
                 sensor_id=None):
        self.longitude = longitude
        self.latitude = latitude
        self.type = type
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.sensor_id = uuid.uuid4().hex if sensor_id is None else sensor_id

    def json(self):
        return {
            'longitude': self.longitude,
            'latitude': self.latitude,
            'type': self.type,
            'status': self.status,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'sensor_id': self.sensor_id
        }

    # insert
    def save_to_mongo(self):
        Database.insert(collection='sensor',
                                 data=self.json())

    # query all sensors
    @staticmethod
    def getAll():
        return Database.find(collection='sensor',
                             query={})

    # query one by sensor id
    @staticmethod
    def getOne(sensor_id):
        return Database.find_one(collection='sensor', query={'sensor_id': sensor_id})

    # query by longitude, latitude, radius(miles)
    @staticmethod
    def getByPosition(longitude, latitude, radius):
        pass

    # edit
    @staticmethod
    def editOne(sensor_id, data):
        Database.update(collection='sensor',
                                 where={'sensor_id': sensor_id},
                                 data=data)
    # delete
    @staticmethod
    def deleteOne(sensor_id):
        Database.delete_many(collection='sensor', query={'sensor_id': sensor_id})