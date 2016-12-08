from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from models.user import User
from src.common.Database import Database
from src.models.sensor import Sensor

app = Flask(__name__)
app.secret_key = "jose"

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def login_template():
    return render_template('landing.html')


@app.route('/register')
def register_template():
    return render_template('registration.html')


@app.route('/show/sensor')
def sensor_template():
    sensors = Sensor.getAll()
    return render_template('sensorsTable.html', sensors=sensors)

# for static html files
@app.route('/<string:page_name>/')
def static_page(page_name):
    if page_name == "usage":
        return  render_template('%s.html' % page_name, account=session['account'])
    else:
        return render_template('%s.html' % page_name)

# for the first page of Normal User, Sensor Provider, Cloud Provider
@app.route('/user/normal')
def normal_usr_index():
    return render_template('index.html')

@app.route('/user/sensor')
def sensor_provider_index():
    return render_template('sensormanagement.html')

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
        if session['role'] == '1':
            return redirect(url_for('normal_usr_index'))
        elif session['role'] == '2':
            return redirect(url_for('sensor_provider_index'))
        elif session['role'] == '3':
            return redirect(url_for('cloud_provider_index'))
    else:
        session['account'] = None
        session['role'] = None
        session['user_id'] = None
        return render_template('login-error.html')


@app.route('/auth/register', methods=['POST'])
def register_user():
# (cls, cursor, account, pwd, first_name, last_name, role)
    account = request.form['account']
    pwd = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    role = request.form['role']

    user = User(first_name=first_name,
                last_name=last_name,
                account=account,
                pwd=pwd,
                role=role)
    user.register()
    return redirect(url_for('login_template'))


if __name__ == "__main__":
    app.run(debug=True, port=5002)