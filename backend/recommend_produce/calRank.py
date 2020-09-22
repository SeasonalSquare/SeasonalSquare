import datetime
import pandas as pd

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d')
todayMonth = now.month

season = {} # seanson
name = []
kcal = []
months = []
with open('./static/data/seanson.dat',encoding = 'utf-8') as file:
    for produce in file:
        t = produce.split(' ')
        name.append(t[0])
        if len(t) == 2:
            kcal.append('-')
            months.append('-')
        else:
            kcal.append(t[1] + ' ' + t[2].split('/')[0])
            months.append(produce.split('/')[1][:-1])

season = {"name":name, "kcal":kcal, "months":months}
#print(pd.DataFrame(season))


today = {} #today Price
name = []
fullname = []
price = []
unit = []
value = []
direction = []

with open('./static/data/today.dat',encoding = 'utf-8') as file:
    for produce in file:
        if "-" not in produce:
            t = produce.split(':')
            name.append(t[0])
            fullname.append(t[1])
            price.append(t[2])
            unit.append(t[3])
            value.append(t[4])
            direction.append(t[5][0])




today = {"name":name, "fullname":fullname, "price":price,"unit":unit, "value":value,"direction":direction}
#print(pd.DataFrame(today))

a = pd.DataFrame(season)
b = pd.DataFrame(today)
df_INNER_JOIN = pd.merge(a, b, on="name")
count = []
for row in df_INNER_JOIN.itertuples():
    '''
    print(row)
    print(row[3]) # month
    print(row[7])  # 등락률
    print(row[8])  #등락여부( 0:가격하락 1:가격상승 2:등락없음 )
    '''
    sum = 0
    if row[8] == '0': #등락여부( 0:가격하락 1:가격상승 2:등락없음 )
        #print("랭크점수올리는중",row)
        sum += 1
        sum += float(row[7])
    #print(todayMonth, row[3])
    if str(todayMonth) in row[3]:
        sum += 1

    count.append(sum)
df_INNER_JOIN['rank'] = count
#print(df_INNER_JOIN)

df_sorted_by_values = df_INNER_JOIN.sort_values(by='rank' ,ascending=False)

# 정렬 결과를 출력합니다.
print(df_sorted_by_values)
df_sorted_by_values.to_csv('./static/data/result.csv')



