import uuid

from flask import session
from src.common.MySQLHelper import MySQLHelper


class User(object):

    def __init__(self, first_name, last_name, username, pwd, user_role):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.pwd = pwd
        self.user_role = user_role

    def json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'pwd': self.pwd,
            'user_role': self.user_role
        }

    def register(self):
        db = MySQLHelper()
        connection = db.connect()
        try:
            # The following introduces a deliberate security flaw.
            # See section on SQL injection below
            query = "INSERT INTO user (username, password, first_name, last_name, user_type)"
            query += "VALUES('{0}', '{1}', '{2}', '{3}', '{4}');" \
                .format(self.username, self.pwd, self.first_name, self.last_name, self.user_role)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
        # session['account'] = self.account

    @staticmethod
    def check_pwd(username, pwd):
        db = MySQLHelper()
        connection = db.connect()

        try:
            query = "SELECT `username`, `password`, `first_name`, `last_name`, `user_type` "
            query += "FROM `user` "
            query += "WHERE `username`=%s;"
            with connection.cursor() as cursor:
                cursor.execute(query, (username,))
                userDict = cursor.fetchone()
                print userDict
        finally:
            connection.close()

        if userDict['password'] == pwd:
            session['user_role'] = userDict['user_type']
            return True
        else:
            return False

    @staticmethod
    def login(username):
        session['username'] = username

    @staticmethod
    def logout():
        session['username'] = None