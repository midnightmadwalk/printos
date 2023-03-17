from flask import Flask
import os
import os
k=os.name
app = Flask(__name__)

@app.route('/')
def hello_world():
    return k
