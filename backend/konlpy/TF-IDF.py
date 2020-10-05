import sys
sys.stdin = open('titles.txt', 'r', encoding='UTF-8')

# 농수산물의 총 개수, 미리 필요하다.
num = int(input())

# 각 타이틀에서 개수만큼 레시피 제목을 뽑아온다.
# titles = [input() for _ in range(num)]
titles = [input() for _ in range(num)]
# print('제목들')
# print(titles)

myeongsa = []
m_dict = {}

"""
Step 1.데이터 전처리 과정
KOnlpy로 명사 단위 형태소 분석
"""

# from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt
from konlpy.utils import pprint

okt = Okt()

doc_nouns_list = [' '.join(okt.nouns(doc)) for doc in titles]

"""
아래에 담길 m_dict는 명사 딕셔너리로 각 명사의 빈도수를 세준다.
"""

# 거를 단어
STOP_WORDS = ['맛있는', '노', '만들기', '요리', '법']

for sentence in titles:
    raw_list = okt.nouns(sentence)
    for noun in raw_list:
        if noun not in STOP_WORDS:
            try:
                m_dict[noun] += 1
            except:
                m_dict[noun] = 1

# 내림차 순 정렬
pgm_lang_val_reverse = sorted(m_dict.items(), 
                              reverse=True, 
                              key=lambda item: item[1])
# print(pgm_lang_val_reverse)
# rank = 1
# former_value = -1
# print_count = 0
# for key, value in pgm_lang_val_reverse:
#     if key == '당근':
#         print(key, '의 핵심 키워드 50건')
#         continue

#     print(rank, '위 ', key, ":", value, '건')
#     if former_value != value:
#         rank += 1

#     former_value = value
#     print_count += 1
#     if print_count > 50:
#         break

"""
Step 2. TF-IDF 분석

"""
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(doc_nouns_list)

# print(tfidf_matrix)

# pprint(tfidf_vectorizer)
# doc_nouns_similarities = (tfidf_matrix * tfidf_matrix.T)
# print()
# print('레시피 제목별 키워드 유사도')
# # print(doc_nouns_list)
# pprint(doc_nouns_similarities.toarray())


"""
Step 3.  코사인 유사도 계산

"""

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# print('cosine_sim')
# print(cosine_sim)

"""
Step 4.  항목별 유사도 가져오기

"""

#  판다스의 경우 지금 사용하지 않아도 될 듯
# import pandas as pd

def recipe_REC(title, cosine_sim=cosine_sim):
    #입력한 레시피로 부터 인덱스 가져오기
    idx = titles.index(title)

    # 모든 레시피에 대해서 해당 레시피와의 유사도를 구하기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 레시피들을 정렬
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)
    sim_scores_reversed = sorted(sim_scores, key=lambda x:x[1], reverse = False)

    # 가장 유사한 3개의 레시피를 받아옴
    sim_scores = sim_scores[1:4]
    sim_scores_reversed = sim_scores_reversed[1:4]

    # 가장 유사한 3개 레시피의 인덱스 받아옴
    recipe_indices = [i[0] for i in sim_scores]
    recipe_indices_reversed = [i[0] for i in sim_scores_reversed]
    
    """
    여기는 잠깐 주석처리할게요
    판다스를 활용해야하니까요
    """

    # #기존에 읽어들인 데이터에서 해당 인덱스의 값들을 가져온다. 그리고 스코어 열을 추가하여 코사인 유사도도 확인할 수 있게 한다.
    # result_df = df.iloc[recipe_indices].copy()
    # result_df['score'] = [i[1] for i in sim_scores]
    
    # # 읽어들인 데이터에서 content 부분만 제거, 제목과 스코어만 보이게 함
    # del result_df['content']

    # # 가장 유사한 10개의 레시피의 제목을 리턴
    # return result_df

    """
    여기까지
    """
    print('유사한 레시피들')
    for idx in recipe_indices:
        print(idx, ":", titles[idx])
    print()
    print('색다른 레시피들')
    for idx in recipe_indices_reversed:
        print(idx, ":", titles[idx])
    return

recipe_REC("여름제철 감자요리/간단 브런치로 좋은 계란 감자채전")