from flask import Flask
import platform
k=platform.platform()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return k
