from . import app
#from models import User

@app.route('/')
def test():
    return 'Test?'

@app.route('/users')
def users():
    #us = User.query.all()

    return 'ok'