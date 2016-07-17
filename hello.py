from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))