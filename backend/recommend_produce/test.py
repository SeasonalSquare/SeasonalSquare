import datetime
import pandas as pd

df = pd.read_csv('./static/data/result.csv')
df = df.drop(['Unnamed: 0'], axis=1)
print(df)
t = 0
names = ["시금치","오이","생강"]
dropIndex = []
for i in range(len(df)):
    #print(df.iloc[i])
    for name in names:
        if name == df.iloc[i][0]:
            names.remove(name)
            dropIndex.append(i)
            break

df = df.drop(dropIndex)

print(df)
records = df.iloc[0:10].to_json(orient='records', force_ascii=False)
            # print(df.iloc[0:10].to_json(orient='records'))