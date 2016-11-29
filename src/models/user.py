import uuid
from flask import session
from src.common.Database import Database


class User(object):

    def __init__(self, first_name, last_name, account, pwd, role, cloud_id=0, user_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account
        self.pwd = pwd
        self.role = role
        self.cloud_id = cloud_id
        self.user_id = uuid.uuid4().hex if user_id is None else user_id

    def json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'account': self.account,
            'pwd': self.pwd,
            'role': self.role,
            'cloud_id': self.cloud_id,
            'user_id': self.user_id
        }

    def register(self):
        Database.insert(collection = 'user',
                        data = self.json())
        # session['account'] = self.account

    @staticmethod
    def check_pwd(account, pwd):
        user_info = Database.find_one(collection='user',
                                      query={'account': account})
        if user_info is None:
            return False

        if pwd == user_info['pwd']:
            return True
        else:
            return False

    @staticmethod
    def login(account):
        session['account'] = account

    @staticmethod
    def logout():
        session['account'] = None