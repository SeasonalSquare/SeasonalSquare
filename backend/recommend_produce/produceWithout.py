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
                    if name == "견과류" and "땅콩" == df.iloc[i][0]:
                        names.remove("견과류")
                        dropIndex.append(i)
                        break
                    if name == "대두" and "땅콩" == df.iloc[i][0]:
                        names.remove("대두")
                        dropIndex.append(i)
                        break
                    if name == "소고기" and "쇠고기" == df.iloc[i][0]:
                        names.remove("소고기")
                        dropIndex.append(i)
                        break
                    if name == "갑각류" and "새우젓" == df.iloc[i][0]:
                        names.remove("갑각류")
                        dropIndex.append(i)
                        break
                    if name == "어패류" and "멸치액젓" == df.iloc[i][0]:
                        names.remove("어패류")
                        dropIndex.append(i)
                        break
                    if name == "깨" and "참깨" == df.iloc[i][0]:
                        names.remove("깨")
                        dropIndex.append(i)
                        break
                    if name == "유제품" and "우유" == df.iloc[i][0]:
                        names.remove("유제품")
                        dropIndex.append(i)
                        break

            if "버섯류" in names:
                for i in range(len(df)):
                    if "느타리버섯" == df.iloc[i][0]:
                        dropIndex.append(i)
                        break
                    if "팽이버섯" == df.iloc[i][0]:
                        dropIndex.append(i)
                        break
                    if "새송이버섯" == df.iloc[i][0]:
                        dropIndex.append(i)
                        break

            #vegi
            meets = []
            milk = 0
            shrimp = 0
            anchovy = 0
            for i in range(len(df)):
                if "쇠고기" == df.iloc[i][0]:
                    meets.append(i)
                if "우유" == df.iloc[i][0]:
                    milk = i
                if "새우젓" == df.iloc[i][0]:
                    shrimp = i
                if "멸치액젓" == df.iloc[i][0]:
                    anchovy = i


            if vegi == "vegan":
                for meet in meets:
                    if meet not in dropIndex:
                        dropIndex.append(meet)
                if milk not in dropIndex:
                    dropIndex.append(milk)
                if shrimp not in dropIndex:
                    dropIndex.append(shrimp)
                if anchovy not in dropIndex:
                    dropIndex.append(anchovy)
            elif vegi == "lacto-vegetarian":
                for meet in meets:
                    if meet not in dropIndex:
                        dropIndex.append(meet)
                if shrimp not in dropIndex:
                    dropIndex.append(shrimp)
                if anchovy not in dropIndex:
                    dropIndex.append(anchovy)
            elif vegi == "ovo-vegetarian":
                for meet in meets:
                    if meet not in dropIndex:
                        dropIndex.append(meet)
                if milk not in dropIndex:
                    dropIndex.append(milk)
                if shrimp not in dropIndex:
                    dropIndex.append(shrimp)
                if anchovy not in dropIndex:
                    dropIndex.append(anchovy)
            elif vegi == "lacto-ovo-vegetarian":
                for meet in meets:
                    if meet not in dropIndex:
                        dropIndex.append(meet)
                if shrimp not in dropIndex:
                    dropIndex.append(shrimp)
                if anchovy not in dropIndex:
                    dropIndex.append(anchovy)
            elif vegi == "pesco-vegetarian":
                for meet in meets:
                    if meet not in dropIndex:
                        dropIndex.append(meet)
            elif vegi == "pollo-vegetarian":
                for meet in meets:
                    if meet not in dropIndex:
                        dropIndex.append(meet)
            df = df.drop(dropIndex)

            records = df.iloc[0:40].to_json(orient='records', force_ascii=False)
            # print(df.iloc[0:10].to_json(orient='records'))

            return str(records)
