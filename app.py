from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a modification to test the automation. Bravo, you did it!'