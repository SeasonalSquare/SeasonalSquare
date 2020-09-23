from flask import Flask
import todayProduce
import todayPrices
import test1

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/todayProduce', methods = ['GET'])
def todayProduce():
    #test1.test111.__init__(self='')
    #result = test1.test11()
    result = todayPrices.__init__(self='')
    print(result)
    return result


if __name__ == '__main__':
    app.run()
