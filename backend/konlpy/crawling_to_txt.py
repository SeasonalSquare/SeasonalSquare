from bs4 import BeautifulSoup
import requests

print('== CRAWLING ON THE PROGRESS ==')

grocery_name = '감자'

# 특정요리 url
url = 'https://www.10000recipe.com/recipe/list.html?q='
page = '&order=reco&page='
num = 1

recipe_list = []
title_crawling = []
former_len = -1
current_len = 0

flag = 1

while flag:
    former_len = len(title_crawling)

    response = requests.get(url + grocery_name + page + str(num)).text
    data = BeautifulSoup(response, 'html.parser')

    # print(data)

    # contents > 재료
    recipes = data.select('#contents_area_full > ul > ul > li')
    # 음식사진, 음식이름

    for recipe in recipes:
        image = recipe.select_one('div.common_sp_thumb > a > img').attrs['src']
        title =  recipe.select_one('div.common_sp_caption > div.common_sp_caption_tit.line2').text
        pk = recipe.select_one('div.common_sp_thumb > a').attrs['href'].replace('/recipe/','')

        tem = {'image': image, 'title': title, 'pk': pk }
        recipe_list.append(tem)
        title_crawling.append(title)
    
    current_len = len(title_crawling)

    if current_len == former_len:
        flag = 0

    num += 1

text_file = open("titles.txt", "w")
text_file.write(str(len(title_crawling)) + '\n')

for elm in title_crawling:
    text_file = open("titles.txt", "a", encoding="utf-8")
    text_file.write(elm + '\n')
text_file.close()

print('== JOB DONE ==')