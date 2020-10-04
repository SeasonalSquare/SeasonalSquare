import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import json
import takeSeason
import calRank
def crawl_today_produce():
    open_url = 'http://www.kamis.or.kr/service/price/xml.do?action=dailySalesList&p_cert_key=940b44e5-05f1-4ef1-a938-09a9d3e7ae6d&p_cert_id=1215&p_returntype=xml'
    # Open API URL 생성

    res = requests.get(open_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    # XML 도 Html 과 동일하게 html.parser 이용

    data = soup.find('price')
    items = data.find_all('item')
    name = ""
    count1 = 0
    count2 = 0
    nameList = []
    lists = []
    # XML 데이터에서 item 태그를 모두 불러와 data 변수에 저장
    for item in items:
        product_cls_code = item.find('product_cls_code')
        if(product_cls_code.get_text() == '01'):
            count1 = count1 +1
            item_name = item.find('item_name').get_text().split('/')
            if item_name[0] not in nameList:
                nameList.append(item_name[0])
            if item_name[0] == item_name[1]:
                name = item_name[0]
            else:

                name = item_name[0]  +'('+  item_name[1]+ ')'
            unit = item.find('unit')
            price = item.find('dpr1') #가격
            value = item.find('value') #등락률
            direction = item.find('direction') #등락여부( 0:가격하락 1:가격상승 2:등락없음 )
            result = (item_name[0] + ':' + name+ ':' + price.get_text() + ':' +unit.get_text() + ':' + value.get_text() + ':' + direction.get_text() )

            lists.append(result)
            #print(item_name[0], name, price.get_text() ,unit.get_text() , value.get_text() , direction.get_text() )

    '''
    print(lists)
    print(count1)
    print(nameList)
    '''

    #오늘 데이터 삽입
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d')
    with open('./static/data/today.dat', 'w', encoding='utf-8', ) as file:
        file.write(nowDatetime+ '\n')
        for info in lists:
            file.write(info +'\n')


    with open('./static/data/seanson.dat',encoding = 'utf-8') as file:
        for produce in file:
            for name in nameList:
                produce_name = produce.split(" ")

                #print(name, produce)
                if name == produce_name[0]:
                    nameList.remove(name)

    #print(lists)
    for name in nameList:
        takeSeason.crawlSeason(name)

def __init__(self):
    print("today서버 파일 실행중..")

    with open('./static/data/seanson.dat', encoding='utf-8') as file:
        for produce in file:
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d')
            if produce != nowDatetime:
                crawl_today_produce()
                calRank.calToday.__init__(self='')


            df = pd.read_csv('./static/data/result.csv')
            df = df.drop(['Unnamed: 0'], axis=1)
            records = df.iloc[0:40].to_json(orient='records', force_ascii=False)
            #print(df.iloc[0:10].to_json(orient='records'))

            return str(records)