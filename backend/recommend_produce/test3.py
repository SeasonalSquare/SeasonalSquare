import datetime
import pandas as pd

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d')
todayMonth = now.strftime('%m')

season = {} # seanson
with open('./static/data/seanson.dat',encoding = 'utf-8') as file:
    dict_seanson = {}
    for produce in file:
        t = produce.split(' ')
        dict_seanson['name']=(t[0])
        if len(t) == 2:
            dict_seanson['kcal']=('-')
            dict_seanson['month']=('-')
        else:
            dict_seanson['kcal']=(t[1] + ' ' + t[2].split('/')[0])
            dict_seanson['month']=(t[3:])


    print(dict_seanson)


