from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from models.user import User
from src.Database import Database
from src.models.sensor import Sensor

app = Flask(__name__)
app.secret_key = "jose"

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.route('/sensor')
def sensor_template():
    sensors = Sensor.getAll()
    return render_template('sensorsTable.html', sensors=sensors)

@app.route('/auth/login', methods=['POST'])
def login_user():
    account = request.form['account']
    pwd = request.form['password']

    if User.check_pwd(account, pwd):
        User.login(account)
    else:
        session['account'] = None

    # redirect to the function name
    return redirect(url_for('sensor_template'))

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