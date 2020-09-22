from flask import Flask
import todayProduce
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/todayProduce', methods = ['GET'])
def todayProduce():
    return  todayProduce


if __name__ == '__main__':
    app.run()
