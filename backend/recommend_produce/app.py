from flask import Flask, request, send_file, render_template
import todayPrices
import os
from flask_cors import CORS
import produceWithout
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/todayProduce', methods = ['GET'])
def todayProduce():
    #test1.test111.__init__(self='')
    #result = test1.test11()
    result = todayPrices.__init__(self='')
    print(result)
    return result

@app.route('/todayProduceWithout', methods = ['GET'])
def todayProduceWithout():
    allergies = request.args.get('allergies')
    vegi = request.args.get('vegi')
    print("들어온 알러지", allergies)
    print("들어온 베지타입", vegi)
    result = produceWithout.__init__(self='', allergies=allergies, vegi=vegi)
    print(result)
    return result

@app.route('/produceImg', methods = ['GET'])
def produceImg():
    path_dir = './static/data/img/'
    file_list = os.listdir(path_dir)  # path 에 존재하는 파일 목록 가져오기
    name = request.args.get('name')
    print("넘어온 name =", name)
    findname = "-"
    for f in file_list:
        if name in f:
            findname = f
        if name == f:
            return send_file(path_dir + f, mimetype='image/jpg')
    if findname == "-":
        filename = 'error.jpg'
    else:
        filename = findname
    return send_file(path_dir+filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run()
