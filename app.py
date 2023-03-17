from flask import Flask
import subprocess

app = Flask(__name__)

args = ("ls")
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
@app.route('/')
def hello_world():
    return output
