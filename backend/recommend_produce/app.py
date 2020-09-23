from flask import Flask, request, send_file
import todayPrices
import os


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

@app.route('/produceImg', methods = ['GET'])
def produceImg():
    path_dir = './static/data/img/'
    file_list = os.listdir(path_dir)  # path 에 존재하는 파일 목록 가져오기
    name = request.args.get('name')
    for f in file_list:
        if name in f:
            print(f)
            return send_file(path_dir + f, mimetype='image/jpg')

    filename =  'error.jpg'
    return send_file(path_dir+filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run()
