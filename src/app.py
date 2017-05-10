from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from models.user import User
from common.Database import Database
from models.sensor import Sensor
from common.MySQLHelper import MySQLHelper

app = Flask(__name__)
app.secret_key = "jose"
DB = MySQLHelper()

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def login_template():
    return render_template('landing.html')


@app.route('/register')
def register_template():
    return render_template('registration.html')


@app.route('/show/employee')
def employee_template():
    employees = DB.get_all_inputs('employees')
    return render_template('sensorsTable.html', sensors=employees)

@app.route('/employee/<int:id>', methods=['DELETE'])
def employee_deletion(id):
    DB.clear('employees', 'employeeNumber', id)

# for static html files
@app.route('/<string:page_name>/')
def static_page(page_name):
    if page_name == "usage":
        return render_template('%s.html' % page_name, account=session.get('username'))
    else:
        return render_template('%s.html' % page_name)

# for the first page of Normal User, Sensor Provider, Cloud Provider
@app.route('/user/normal')
def normal_usr_index():
    if session.get('username'):
        return render_template('index.html')
    else:
        return redirect(url_for('new_login'))

@app.route('/user/admin')
def admin_index():
    if session.get('username'):
        return render_template('sensormanagement.html')
    else:
        return render_template('login-error.html')

@app.route('/user/cloud')
def cloud_provider_index():
    return render_template('editcluster.html')

@app.route('/auth/login', methods=['POST'])
def login_user():
    account = request.form['account']
    pwd = request.form['password']

    if User.check_pwd(account, pwd):
        User.login(account)
        # redirect to the function name
        if session.get('user_role') == '1':
            return redirect(url_for('normal_usr_index'))
        elif session.get('user_role') == '2':
            return redirect(url_for('admin_index'))
    else:
        session['username'] = None
        session['user_role'] = None
        session['user_id'] = None
        return render_template('login-error.html')

@app.route('/auth/logout')
def logout_user():
    User.logout()
    return redirect(url_for('new_login'))

@app.route('/new/login')
def new_login():
    return render_template('login.html')

@app.route('/auth/register', methods=['POST'])
def register_user():
# (cls, cursor, account, pwd, first_name, last_name, user_role)
    account = request.form['account']
    pwd = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user_role = request.form['role']

    user = User(first_name=first_name,
                last_name=last_name,
                username=account,
                pwd=pwd,
                user_role=user_role)
    user.register()
    return redirect(url_for('login_template'))


if __name__ == "__main__":
    app.run(debug=True, port=5002)