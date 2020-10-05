import sys
sys.stdin = open('titles.txt', 'r', encoding='UTF-8')

# 농수산물의 총 개수, 미리 필요하다.
num = int(input())

# 각 타이틀에서 개수만큼 레시피 제목을 뽑아온다.
titles = [input() for _ in range(num)]

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

for sentence in titles:
    raw_list = okt.nouns(sentence)
    for noun in raw_list:
        try:
            m_dict[noun] += 1
        except:
            m_dict[noun] = 1

# 내림차 순 정렬
pgm_lang_val_reverse = sorted(m_dict.items(), 
                              reverse=True, 
                              key=lambda item: item[1])

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

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(doc_nouns_list)

print(tfidf_matrix)

# pprint(tfidf_vectorizer)
# doc_nouns_similarities = (tfidf_matrix * tfidf_matrix.T)
# print()
# print('레시피 제목별 키워드 유사도')
# # print(doc_nouns_list)
# pprint(doc_nouns_similarities.toarray())