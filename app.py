from flask import Flask
import subprocess

app = Flask(__name__)

args = ("./pocketbase", "--help")
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
with open ("output.txt", "w") as k:
    k.write(output)
    
@app.route('/')
def hello_world():
    with open ("output.txt", "r") as k:
        jk=k.read(output)
    return jk
