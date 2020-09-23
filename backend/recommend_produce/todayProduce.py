import requests
from bs4 import BeautifulSoup
import takeSeason
import datetime
import calRank
import pandas as pd
import json


def __init__(self):
    print("today서버 파일 실행중..")

    df = pd.read_csv('./static/data/result.csv')
    df = df.drop(['Unnamed: 0'], axis=1)
    df.iloc[0:10].to_json('./static/data/result10.json', orient='table')
    records = json.loads(df.iloc[0:10].to_json()).values()
    print("??왜 출력안해?",records)

    return records

