import os
from bs4 import BeautifulSoup
import requests
import json

def get_content(recipe_pk):
    url = 'https://www.10000recipe.com/recipe/'
    response = requests.get(url + str(recipe_pk)).text
    data = BeautifulSoup(response, 'html.parser')
    writer = data.select_one('#contents_area > div.view2_pic > div.user_info2 > span').text.strip()

    # 음식 사진
    dish_image = data.select_one('#contents_area > div.view2_pic > div.centeredcrop > img').attrs['src']
    # [ 재료 ]
    ingredients = data.select('#divConfirmedMaterialArea > ul:nth-child(1) > a')
    # [ 양념 ]
    sources = data.select('#divConfirmedMaterialArea > ul:nth-child(2) > a')
    allergy_data = {
        "1": ["땅콩", "땅콩버터", "잣", "피넛버터"],
        "2": [],
        "3": [], 
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "10": [],

    }
    recipe_data = {}
    ingredient_data = {}
    temp = []
    allergy_list = []
    for ingredient in ingredients:
        # print(ingredient)
        jaeryo = ingredient.select_one('li').text.split('\n')
        for key, value in allergy_data.items():
            if jaeryo in value:
                allergy_list.append(int(key))
        item = {'ingredient_name' : jaeryo[0].strip(), 'amount' : jaeryo[1] }
        temp.append(item)
    ingredient_data['main_ingredients'] = temp

    temp = []
    for source in sources:
        jaeryo = source.select_one('li').text.split('\n')
        item = {'source_name' : jaeryo[0].strip(), 'amount' : jaeryo[1] }
        temp.append(item)
    ingredient_data['source_ingredients'] = temp

    recipe_data['ingredient_data'] = ingredient_data

    steps = data.select('#contents_area > div.view_step > div.view_step_cont')
    # print(steps)
    step_list = []
    for idx, step in enumerate(steps, start=1):
        exp = step.select_one('div.media-body').text
        if step.select_one('img'):
            image = step.select_one('img').attrs['src']
        else:
            image = None
        item = { 'step' : idx, 'explain' : exp , 'image' : image}
        step_list.append(item)

    recipe_data['recipe'] = step_list
    return allergy_list, writer, recipe_data


current = os.getcwd()
grocery = open(current + '\\grocery.txt', 'r', encoding='UTF-8')
recipe_json = open(current + '\\recipe.json', 'w', encoding='UTF-8')
lines = grocery.readlines()
recipe_list = []
for line in lines:
    grocery_name = line.split(' ')[0]
    url = 'https://www.10000recipe.com/recipe/list.html?q='

    response = requests.get(url + grocery_name).text
    data = BeautifulSoup(response, 'html.parser')


    # contents > 재료
    recipes = data.select('#contents_area_full > ul > ul > li')
    # 음식사진, 음식이름
    for recipe in recipes:
        image = recipe.select_one('div.common_sp_thumb > a > img').attrs['src']
        title =  recipe.select_one('div.common_sp_caption > div.common_sp_caption_tit.line2').text
        pk = recipe.select_one('div.common_sp_thumb > a').attrs['href'].replace('/recipe/','')
        writer, content = get_content(pk)
        tem = {"model": "recipe_api.recipe", 
            "pk": pk, 
            "fields": {
                "writer": writer,
                "image": image, 
                "title": title, 
                "main_grocery": grocery_name,
                # "allergies": allergy_list,
                "content": str(content),
                }
            }
        recipe_list.append(tem)
recipe_json.write(json.dumps(recipe_list, ensure_ascii=False))
grocery.close()
recipe_json.close()