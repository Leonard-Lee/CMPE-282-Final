import pymysql.cursors
import dbconfig

class MySQLHelper(object):
    def __init__(self):
        self.database = dbconfig.db_name
        self.host = dbconfig.db_host
        self.user = dbconfig.db_user
        self.pwd = dbconfig.db_password

    def connect(self):
        # Connect to the database
        return pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.pwd,
                             db=self.database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def get_all_employees(self):
        connection = self.connect()

        try:
            query = "SELECT employees.*,dept_emp.dept_no,dept_manager.emp_no as MANAGER_EMPNO,emp.first_name as Manager_Firstname,emp.last_name AS Manager_lastName " \
                    "FROM employees INNER JOIN dept_emp " \
                    "ON employees.emp_no = dept_emp.emp_no " \
                    "INNER JOIN dept_manager " \
                    "ON dept_manager.dept_no = dept_emp.dept_no " \
                    "INNER JOIN employees emp " \
                    "ON dept_manager.emp_no = emp.emp_no;"
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
