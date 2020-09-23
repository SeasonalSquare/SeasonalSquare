import requests
from bs4 import BeautifulSoup

class crawlSeason:
    def __init__(self, name):
        open_url = 'https://search.naver.com/search.naver?where=kdic&sm=tab_jum&query='+name

        # Open API URL 생성

        res = requests.get(open_url)
        soup = BeautifulSoup(res.content, 'html.parser')
        # XML 도 Html 과 동일하게 html.parser 이용

        data = soup.select('div.inner')
        print(data)
        months = []
        kcals = []
        for item in data:
            if item.em.string == "칼로리":
                t = item.span.a.string
                print("칼로리 정보 : ", t)
                kcals.append(t)
            if item.em.string == "제철":
                t = item.span.a.string
                if "월" in t:
                    print(t)
                    if "~" in t:
                        month = t.split("~")

                        start = month[0].split("월")
                        end = month[1].split("월")

                        for x in range(int(start[0]), int(end[0])+1):
                            months.append(str(x))
                        print("제철 정보 : ", start[0], end[0])
                    else:
                        month = t.split("월")
                        print("제철 정보 : ", month[0])
                        months.append(str(month[0]))
                    break

        print(months)
        if len(kcals) == 0:
            kcals.append("-")
        result = ' '.join(kcals) + '/' + ' '.join(months)
        print(result)

        with open('./static/data/seanson.dat', 'a',encoding = 'utf-8', ) as file:
            file.write(name + ' ' + result +'\n')
            # print(color, file=file)