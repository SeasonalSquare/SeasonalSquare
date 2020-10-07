from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Recipe
from .serializers import RecipeSerializer, RecipeListSerializer


# Create your views here.
@api_view(['GET'])
def grocery(request, grocery_name):
    recipes = Recipe.objects.filter(main_grocery=grocery_name)
    serializer = RecipeListSerializer(recipes, many=True)
    for recipe in serializer.data:
        recipe['pk'] = recipe['id']
    
    return Response(serializer.data)


@api_view(['GET'])
def recipe(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)

    print(recipe.main_grocery)
    print(recipe.title)
    recipes = Recipe.objects.filter(main_grocery=recipe.main_grocery)

    serializer = RecipeListSerializer(recipes, many=True)
    # num = len(serializer.data)
    # for elm in serializer.data:
    #     print(elm['id'])


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
    # print(current_title_nouns)

    doc_nouns_list = [current_title_nouns] + doc_nouns_list
    # print(doc_nouns_list)
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
        
        for idx in recipe_indices:
            print(idx, ":", doc_nouns_list[idx])
            print(idx, ":", idx_list[idx])
            rrecipe = get_object_or_404(Recipe, pk=idx_list[idx])
            print(rrecipe.title)
        print()
        print('색다른 레시피들')

        for idx in recipe_indices_reversed:
            print(idx, ":", doc_nouns_list[idx])
            print(idx, ":", idx_list[idx])
            rrecipe = get_object_or_404(Recipe, pk=idx_list[idx])
            print(rrecipe.title)
        return
    recipe_REC()
    return Response(recipe.get_content())
