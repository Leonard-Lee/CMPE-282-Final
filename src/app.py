from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from models.user import User
from src.common.Database import Database

# user registration
# user = User(first_name='Leo', last_name='Lee',
#             account='Spartan', pwd='223', role=1)
#
# user.register()

# user account/pwd check
# result = User.check_pwd('Spartan122', '567')
# if result:
#     print "It is authorized"
# else:
#     print "Wrong pwd"

# save a sensor
# sensor = Sensor(longitude = 123.12,
#                 latitude = 222.33,
#                 type = 1,
#                 status=True)
# sensor.save_to_mongo()

# sensors = Sensor.getAll()
# for sensor in sensors:
#     print sensor
# update
# Sensor.editOne('e6b7b7e0dc5143bc925a6e3f5ce65135', {'longitude':111.22})

# delete
# Sensor.deleteOne('e6b7b7e0dc5143bc925a6e3f5ce65135')

# another_sensor = Sensor.getOne('e6b7b7e0dc5143bc925a6e3f5ce65135')
# print another_sensor
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