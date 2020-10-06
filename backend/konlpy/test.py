from sklearn.feature_extraction.text import TfidfVectorizer


doc_list = [
    '프리시즌 아시아 투어를 떠나는 토트넘은 싱가포르, 중국을 차례로 방문해 ICC 경기를 치른다.',
    '영국 "풋볼 런던"은 11일 "토트넘이 ICC 첫 경기에서 가장 강력한 스쿼드로 유벤투스에 맞설 것"이라고 평가했다.',
    '토트넘에 합류하는 손흥민은 유벤투스전 출전을 목표로 구슬땀을 흘릴 예정이다.',
]

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(doc_list)
doc_similarities = (tfidf_matrix * tfidf_matrix.T)

print(doc_similarities.toarray())

from konlpy.tag import Okt


okt = Okt()

doc_nouns_list = [' '.join(okt.nouns(doc)) for doc in doc_list]
print(doc_nouns_list)

tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf_matrix = tfidf_vectorizer.fit_transform(doc_nouns_list)
doc_nouns_similarities = (tfidf_matrix * tfidf_matrix.T)

print(doc_nouns_similarities.toarray())