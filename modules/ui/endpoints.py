from flask import Blueprint, render_template, request
from modules import  cbpi

react = Blueprint('react', __name__, template_folder='templates', static_folder='static')

@cbpi.initalizer(order=10)
def init(cbpi):
    print "INITIALIZE UI"
    cbpi.app.register_blueprint(react, url_prefix='/ui')




@react.route('/')
def index():
    return react.send_static_file("index.html")









