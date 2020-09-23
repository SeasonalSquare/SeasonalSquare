from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def grocery(request, grocery_name):

    # 특정요리 url
    url = 'https://www.10000recipe.com/recipe/list.html?q='

    response = requests.get(url + grocery_name).text
    data = BeautifulSoup(response, 'html.parser')


    # contents > 재료
    recipes = data.select('#contents_area_full > ul > ul > li')
    # 음식사진, 음식이름
    recipe_list = []
    for recipe in recipes:
        image = recipe.select_one('div.common_sp_thumb > a > img').attrs['src']
        title =  recipe.select_one('div.common_sp_caption > div.common_sp_caption_tit.line2').text
        pk = recipe.select_one('div.common_sp_thumb > a').attrs['href'].replace('/recipe/','')

        tem = {'image': image, 'title': title, 'pk': pk }
        recipe_list.append(tem)


    return Response(recipe_list)


@api_view(['GET'])
def recipe(request, recipe_pk):
        # 특정 요리 recipe 정보
    url = 'https://www.10000recipe.com/recipe/'
    response = requests.get(url + str(recipe_pk)).text
    data = BeautifulSoup(response, 'html.parser')

    # 음식 사진
    dish_image = data.select_one('#contents_area > div.view2_pic > div.centeredcrop > img').attrs['src']
    # [ 재료 ]
    ingredients = data.select('#divConfirmedMaterialArea > ul:nth-child(1) > a')
    # [ 양념 ]
    sources = data.select('#divConfirmedMaterialArea > ul:nth-child(2) > a')

    recipe_data = {}
    ingredient_data = {}
    temp = []
    for ingredient in ingredients:
        # print(ingredient)
        jaeryo = ingredient.select_one('li').text.split('\n')
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
        image = step.select_one('img').attrs['src']
        item = { 'step' : idx, 'explain' : exp , 'image' : image}
        step_list.append(item)

    recipe_data['recipe'] = step_list
    return Response(recipe_data)
