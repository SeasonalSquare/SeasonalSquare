import todayPrices
import datetime
import pandas as pd

def __init__(self, allergies, vegi):
    print("베지타입", vegi)
    with open('./static/data/seanson.dat', encoding='utf-8') as file:
        for produce in file:
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d')
            if produce != nowDatetime:
                todayPrices.__init__(self='')

            df = pd.read_csv('./static/data/result.csv')
            df = df.drop(['Unnamed: 0'], axis=1)
            dropIndex = []
            names = allergies.split(",")
            print("자른것", names)
            for i in range(len(df)):
                # print(df.iloc[i])
                for name in names:
                    if name == df.iloc[i][0]:
                        names.remove(name)
                        dropIndex.append(i)
                        break

            df = df.drop(dropIndex)

            records = df.iloc[0:40].to_json(orient='records', force_ascii=False)
            # print(df.iloc[0:10].to_json(orient='records'))

            return str(records)
