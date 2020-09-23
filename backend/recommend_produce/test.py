import datetime
import pandas as pd
import jsonify
import json
df = pd.read_csv('./static/data/result.csv')
df = df.drop(['Unnamed: 0'], axis=1)
df.iloc[0:10].to_json('./static/data/result10.json', orient='table')

records = json.loads(df.iloc[0:10].to_json()).values()

print(records)
