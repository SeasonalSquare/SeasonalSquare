from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Recipe, Allergy
from .serializers import RecipeSerializer, RecipeListSerializer


# Create your views here.
@api_view(['GET'])
def grocery(request, grocery_name):
    user = request.user
    if user.is_authenticated:
        user_allergy = user.allergy.all()
        ban_list = [allergy for allergy in user_allergy]
        vegi_allergy = [[], [10, 3, 4, 5, 10100,10101,10102,10103,10104,10105,10002, 10000, 10001,10003], [3,       4,5, 10100,10101,10102,10103,10104,10105,    10002,    10000,10001,10003], [10, 4,5, 10100,10101,10102,10103,10104,10105,    10002,    10000,10001,10003], [4,5, 10100,10101,10102,10103,10104,10105,    10002,    10000,10001,10003], [10002,    10000,10001,10003], [10000, 10001, 10003]]
        if user.vegetarian:
            for pk in vegi_allergy[user.vegetarian.pk]:
                print(pk)
                ban = get_object_or_404(Allergy, pk=pk)
                print(ban)
                ban_list.append(ban)
        recipes = Recipe.objects.filter(main_grocery=grocery_name).exclude(allergies__in=ban_list)
        serializer = RecipeListSerializer(recipes, many=True)
        for recipe in serializer.data:
            recipe['pk'] = recipe['id']
        
        return Response(serializer.data)
    else:
        recipes = Recipe.objects.filter(main_grocery=grocery_name)
        serializer = RecipeListSerializer(recipes, many=True)
        for recipe in serializer.data:
            recipe['pk'] = recipe['id']
        
        return Response(serializer.data)


@api_view(['GET'])
def recipe(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)

    recipes = Recipe.objects.filter(main_grocery=recipe.main_grocery)

    serializer = RecipeListSerializer(recipes, many=True)

    """
    Step 1.데이터 전처리 과정
    KOnlpy로 명사 단위 형태소 분석
    """
    from konlpy.tag import Okt
    from konlpy.utils import pprint

    okt = Okt()
    doc_nouns_list = []
    idx_list = [recipe.pk]

    for elm in serializer.data:
        title_nouns = ' '.join(okt.nouns(elm['title']))
        doc_nouns_list.append(title_nouns)
        idx_list.append(elm['id'])

    current_title_nouns = ' '.join(okt.nouns(recipe.title))
    doc_nouns_list = [current_title_nouns] + doc_nouns_list
    """
    Step 2. TF-IDF 분석

    """
    from sklearn.feature_extraction.text import TfidfVectorizer

    tfidf_vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(doc_nouns_list)

    """
    Step 3.  코사인 유사도 계산

    """

    from sklearn.metrics.pairwise import linear_kernel
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


    """
    Step 4.  항목별 유사도 가져오기

    """

    def recipe_REC(idx=0, cosine_sim=cosine_sim):
        result = {}
        
        #입력한 레시피로 부터 인덱스 가져오기
        # 모든 레시피에 대해서 해당 레시피와의 유사도를 구하기
        sim_scores = list(enumerate(cosine_sim[idx]))

        # 유사도에 따라 레시피들을 정렬
        sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)
        sim_scores_reversed = sorted(sim_scores, key=lambda x:x[1], reverse = False)

        # 가장 유사한 3개의 레시피를 받아옴
        sim_scores = sim_scores[2:5]
        sim_scores_reversed = sim_scores_reversed[1:4]

        # 가장 유사한 3개 레시피의 인덱스 받아옴
        recipe_indices = [i[0] for i in sim_scores]
        recipe_indices_reversed = [i[0] for i in sim_scores_reversed]
        rrecipes = []
        for idx in recipe_indices:
            temp = {}
            rrecipe = get_object_or_404(Recipe, pk=idx_list[idx])
            temp['title'] = rrecipe.title
            temp['image'] = rrecipe.image
            temp['pk'] = rrecipe.id
            rrecipes.append(temp)

        
        urrecipes = []
        for idx in recipe_indices_reversed:
            temp = {}
            rrecipe = get_object_or_404(Recipe, pk=idx_list[idx])
            temp['title'] = rrecipe.title
            temp['image'] = rrecipe.image
            temp['pk'] = rrecipe.id
            urrecipes.append(temp)
        
        result['rel_recipes'] = rrecipes
        result['unrel_recipes'] = urrecipes

        return result
    result = recipe.get_content()
    result['recommend'] = recipe_REC()
    return Response(result)
