from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/sta/register', methods=['GET', 'POST'])
def register_sta():
    print(request.form)
    return 'OK!\n'


@app.route('/sta/deregister', methods=['GET', 'POST'])
def deregister_sta():
    print(request.form)
    return 'OK\n'


@app.route('/ap/register', methods=['GET', 'POST'])
def register_ap():
    print(request.form)
    return 'OK!\n'
