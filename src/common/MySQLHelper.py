import pymysql.cursors
import dbconfig

class MySQLHelper:
    def connect(self, database='classicmodels'):
        # Connect to the database
        return pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             password=dbconfig.db_password,
                             db=database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def get_all_employees(self):
        connection = self.connect()

        try:
            query = "SELECT * FROM `employee`;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, tableName, columnNames, values):
        connection = self.connect()

        try:
            # The following introduces a deliberate security flaw.
            # See section on SQL injection below
            query = "INSERT INTO %s (%s)"%(tableName, columnNames)
            query +=  "VALUES(%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()
        finally:
            connection.close()

    def update(self, tableName, columnName, value, whereColumn, whereValue):
        connection = self.connect()

        try:
            query = "UPDATE %s SET `%s`=%s WHERE `%s`=%s;"
            with connection.cursor() as cursor:
                cursor.execute(query, (tableName, columnName, value, whereColumn, whereValue))
                connection.commit()
        finally:
            connection.close()

    def clear(self, tableName, columnName, value):
        connection = self.connect()

        try:
            query = "DELETE FROM %s WHERE `%s`" % (tableName, columnName)
            query += "=%s;"
            with connection.cursor() as cursor:
                cursor.execute(query, (value,))
                connection.commit()
        finally:
            connection.close()
