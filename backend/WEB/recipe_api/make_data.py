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
        "1": ["땅콩", "땅콩버터", "잣", "피넛버터", "땅콩분태", "볶은 땅콩",'볶은땅콩', '호두가루', "견과류(땅콩/호두등)", "땅콩잼", "생땅콩", '다진 땅콩', '생 땅콩', '호두', '잣', '피칸(견과류)', '견과류', '각종견과류', '각종 견과류'],
        "2": ["새우", "꽃새우", "손질된 새우", "새우살", "새우젓", "건새우", "건 새우", "마른새우", "보리새우", "알새우", "생 새우살", "새우젓국물", "칵테일새우", "칵테일 새우", "칵테일생새우", "새우가루", "손질한 새우", "손질새우", "왕새우", "꽃게", "크래미", "해물믹스"],
        "3": ["계란", "계란 흰자", "계란흰자", "계란 노른자", "계란노른자", "계란물", "계란 노른자 약", "계란 섞은 것", "달걀", "달걀 노른자", "달걀노른자", "달걀흰자", "달걀 흰자", "흰자(L)", "메추리알", "노른자", "노른자(L)" ], 
        "4": ["모시조개", "바지락", "바지락살", "홍합 등 해물(대체가능)", "홍합살", "관자살", "싱싱한 관자", "관자 약", "해물믹스"],
        "5": ['오징어', '손질된 오징어', '불린 오징어', '오징어 자른것', '갑오징어', '문어숙회', '해물믹스', '낙지', ],
        "6": ["통깨", "깨", "참깨", "참깨(깨소금)", "참깨(검은깨도 가능)", "참깨(볶지않은것)", "고운 들깨가루", "들깨가루", "들깨가루(생략가능)", "들깨", "참기름", "참기름(or들기름)", "참기름(들기름)", "들기름", "깻잎", "깻잎(깨순)", "깻잎 작은것", "깻잎 데친것", "깻잎순", "깻잎(생략가능)", "통깨", "통깨 약간", "볶은참깨", "볶은 참깨", "볶은 깨"],
        "7": ["맛술", "청주", '청주또는 미림', '맛술 미림', '맛술(미림)', '미림', '미림 또는 소주', '소주', '소주(청주)', '생강맛술또는 소주', '적 포도주', '화이트와인', '정종'],
        "8": ['인스턴트커피', '녹차가루', '홍차 티백'],
        "9": ['표고버섯', '버섯', '양송이 버섯', '양송이버섯', '새송이버섯', '표고버섯 가루', '팽이버섯', '느타리버섯', '표고버섯가루', '건 표고버섯', '꼬마 새송이버섯', '목이버섯', '새송이버섯 작은것', '느타리 버섯', '말린 느타리버섯', '팽이', '느타리', '양송이', '새송이 수북'],
        "10": ['우유', '저지방 우유', '바나나우유', '바나나맛 우유', '연유', '요거트', '플레인요거트', '플레인요구르트', '플레인 요구르트', '플레인 요구르트(개당 80g)', '요거트파우더', '무가당 플레인 요거트', '버터', '실온 버터', '무염버터', '무염 버터', '차가운 버터', '찬 버터', '녹인버터', '녹인 무염버터', '무염버터 /녹인버터', '버터(팬에 칠할 여분의)', '크림치즈', '생크림', '생크림(휘핑크림)', '휘핑크림 or 생크림', '치즈', '스트링치즈', '리코타치즈', '피자치즈', '슬라이스치즈', '슬라이스 치즈', '파마산치즈', '모차렐라치즈', '모짜렐라치즈', '모짜렐라 치즈', '체다치즈', '모짜렐라 치즈 또는 저지방 체다치즈', '모짜렐라슬라이스치즈', "모짜렐라 치즈 한그릇(취향껏', 'amount': '조절)", '파마산치즈가루', '아이스크림', '바닐라아이스크림'],

        "10000": ["소고기(불고기감)", "소고기(등심)", "소고기(양지)", "소고기간것", "소고기 불고기용", "소고기", "소고기불고기", "소고기국거리", "소고기 다짐육", "소고기(같은것)", "소고기다짐육", "소고기 등심", "소고기 국거리용", "소고기 국거리", "소고기샤브샤브", "소고기(국거리용)", "소고기 불고기감", "소고기 다진것", "소고기(불고깃감)", "소고기 부채살", "소고기 갈빗살", "소고기불고기감", "소고기 (양지)", "소고기 한우 국거리", "소고기다시다", "소고기양지", "소고기사태", "부채살 or 차돌박이", "차돌박이", "양지", "한우 소고기 (살치살)", "한우 양지", "살치살", "등심", "쇠고기", "쇠고기 다짐육", "쇠고기(불고기용)", "쇠고기(등심)", "쇠고기(불고기용이나 부드러운 부위)", "채끝등심", "우둔살", "소고기 한우 국거리", '소고기간것+돼지고기 간것', '돼지고기+소고기'],
        "10001": ['돼지고기', '돼지고기등심', '간 돼지고기', '돼지고기 간것', '돼지고기 갈은것', '돼지고기 (갈은 것)', '돼지고기다짐육', '돼지고기 다짐육', '돼지고기 목심', '돼지목살', '돼지고기 안심', '돼지고기 불고기감', '돼지목심', '돼지고기 앞다리살', '돼지고기앞다리살', '다진 돼지안심', '간돼지고기', '돼지고기간것', '잘게 썰은 돼지고기', '다짐 돼지고기', '다진돼지고기', '다진 돼지고기', '돼지고기(다진것)', '소고기간것+돼지고기 간것', '돼지고기+소고기', '돼지고기 등뼈', '한돈 앞다리살 (돼지고기)', '삼겹살', '대패삼겹살', '대패 삼겹살', '베이컨', '베이컨 썰은 거', '소시지', '비엔나소시지', '비엔나 소시지', '분홍 소시지', '소시지(비엔나)', '소시지(프랑크)', '프랑크소시지', '통 소시지', '큰 비엔나 소시지', '소세지', '비엔나소세지', '비엔나 소세지', '햄', '슬라이스햄', '채썬 햄', '통조림햄', '통조림 햄', '스팸 햄', '샌드위치햄', '슬라이 햄', '스팸', '스팸 작은 사이즈', '스팸 120g', '프로슈토 또는 하몽'],
        "10002": ['닭', '닭가슴살', '닭 가슴살', '꼬꼬빌 닭가슴살', '닭가슴살 소세지', '닭가슴살통조림', '닭다리', '닭다리살', '손질된 닭다리살', '닭안심', '닭 안심', '닭안심살', '삼계탕 닭', '토종닭', '생닭 9호', '닭볶음용', '닭봉', '닭육수', '닭날개', '훈제 닭가슴살 또는 닭가슴살', '닭안심살(닭다리 또는 가슴살)', '치킨스톡 육수', '치킨스톡', '치킨스톡 작은거', '치킨 윙', '큐브형 치킨스톡'],
        "10003": [], # 양고기 결과 없음
        
        "10100": [], # 장어 결과 없음
        "10101": ['가자미', '가자미(250g)'],
        "10102": ['멸치(까나리)액젓', '멸치액젓', '멸치육수', '멸치다시육수', '멸치', '멸치 다시마 육수', '다시마 멸치육수', '멸치 액젓', '(국물용)멸치', '멸치(중멸)', '육수용 멸치', '중멸치', '잔멸치', '멸치다시다육수', '멸치 다시물', '건멸치', '국물멸치', '지리멸치', '멸치다시마육수', '국멸치', '멸치액젖', '멸치액젓(기호에 맞게 가감)', '멸치액젓(피쉬소스)', '피쉬소스(멸치액젓)', '손질한 다시멸치', '국물용 멸치', '멸치 젓국'],
        "10103": ['황태채', '황태', '북어포'],
        "10104": [], # 갈치 결과 없음
        "10105": ['고등어'],

        "10200": ['간장', '맛간장', '양조간장', '진간장', '조선간장', '국간장', '저염 간장','조림간장', '초간장', '양조 간장', '집간장', '(집)국간장', '양념간장', '중국간장', '집 간장', '다시마맛간장', '간장 소주잔', '된장', '집된장', '시판된장', '재래식 된장', '미소 된장', '병아리콩', '완두콩', '콩나물', '콩기름', '콩가루', '두유', '두부', '순두부', '연두부', '순 두부'],
        "10201": ['쌀', '찹쌀', '멥쌀', '맵쌀', '맵쌀(흰쌀)', '멥쌀이나 찹쌀', '불린쌀', '불리지 않은 쌀', '밥', '흰밥', '쌀밥', '찬밥', '따뜻한 밥', '흑미밥', '현미밥', '흰쌀밥', '공기밥', '즉석밥', '쌀뜨물', '쌀뜬물', '쌀가루', '쌀떡', '쌀떡볶이 떡', '떡국떡', '떡볶이떡', '떡볶이 떡', '떡볶이용 떡', '가래떡', '현미 떡국떡', '쌀국수', '쌀국수면', '쌀 박력분', '쌀 한줌(쌀가루)', '라이스페이퍼', '라이스페이퍼 약', '빵용 쌀가루'],
        "10202": ['메밀가루'],
        "10203": ['밀가루 중력분', '박력분', '중력분', '강력분', '밀가루', '밀가루 약', '밀가루중력분', '밀가루박력분', '밀가루풀', '밀가루(강력분)', '밀가루(박력분)', '밀가루(박력)', '중력분 밀가루', '박력분(소주컵기준)', '파스타', '파스타면', '파스타면', '스파게티면', '스파게티 면', '만두피', '생왕 만두피', '식빵', '모닝빵', '바게트 빵', '바게트빵', '통밀식빵', '호밀식빵', '핫도그 빵', '통밀가루', '우리밀 통밀', '우리밀 중력분']
        "10204": ['팥', '팥앙금', '팥배기', '팥 삶은 물 + 일반 물', '빙수 팥', '빙수용 팥', '통 팥', '물 팥'],
        "10205": ['옥수수', '옥수수전분', '옥수수전분가루', '옥수수콘', '캔옥수수', '옥수수콘 통조림', '옥수수통조림', '스위트콘', ],
        "10206": ['녹두', '깐 녹두', '불린 녹두', '껍질 벗긴 녹두', '국산 녹두', '숙주', '숙주나물', '숙주(삶은것)', '숙주 1봉', '데친 숙주', '데친숙주'],

        "10300": ['딸기', '딸기시럽', '냉동딸기'],
        "10301": ['망고'],
        "10302": ['멜론', '멜론(얼린것)', '멜론(중)', '메론', '꼬마 멜론'],
        "10303": ["포도", '화이트와인', '적 포도주'],
        "10304": ["키위", "키위(껍질 벗긴)"],
        "10305": ['복숭아', '천도복숭아'],
        "10306": ['바나나', '바나나 중간크기', '바나나(껍질 제외)', '바나나우유', '바나나맛 우유'],


        "10400": ["계피"],
        "10401": ["겨자"],
        "10402": ["생강"],
        "10403": ["당근"],
        "10404": ["샐러리"],
        "10405": ["오이"],
        "10406": ["마", "마즙"],
        "10407": ["토마토스파게티소스", "토마토소스", "토마토", "토마토케첩", "토마토 약", "토마토소스(없어도ㅇㅋ)", "토마토(얼린것)", "토마토케첩(또는 홀토마토캔)"],
        "10408": ["토란"],
        "10409": ["마늘", "마늘쫑", "마늘 다진것", "마늘(편썬것)", "마늘다진것", "마늘 뚱뚱한거", "마늘(편으로 썰어서 준비)"],
        "10410": ["삶은 호박고구마", "고구마", "고구마 나감자", "작은 고구마", "찐 고구마", "고구마줄기", "고구마(대)", "고구마(중)", "고구마 중간크기", "고구마(2개)", "고구마(작은 것)", "찐고구마", "삶은 고구마", "고구마 3개 /큰거", "삶은 고구마 大", "고구마(찐것)", "삶은 호박고구마", "삶은 고구마(소)", "삶은 고구마", "작은 고구마", "고구마 큰거", "고구마 3개 /큰거", "고구마 (주먹만 한 거)", "밤고구마", "호박고구마"],
        "10411": ["시금치", "시금치 (잎 부분)"],
        "10412": ["양파", "양파(작은사이즈)", "양파(작은거)", "양파 큰것", "양파가루", "양파(小)", "양파(중간크기)", "양파 작은것", "양파 채썬것", "양파채", "양파 중", "양파반개", "양파 작은사이즈", "양파 등 기호성 야채", "양파(소금1t)", "양파(소)", "양파 3분의", "양파(중)", "양파 썰은 거"],
        "10413": ["감자", "감자 중간크기", "감자 전분가루", "감자(250g)", "감자전분", "감자 작은것", "감자전분가루", "감자(중간사이즈)", "감자큰거", "감자 큰크기", "감자 작은 것", "감자 중", "감자(소)"],
        "10414": ["밤"],
        "10415": ["가지"],
        "10416": ["연근"],
        "10417": ["무", "무 (3x3)", "무(중간크기)", "무채", "무말랭이", "무우", "무 중", "무 둥글게", "무 중간크기", "무우(중)", "무(큰무1/3개 작은무 1/2개)", "무순"],
        "10418": ["부추 대체 (쪽파)", "부추", "다진 부추", "자른 부추", "영양부추", "부추 크게"],
        "10419": ["단호박", "단호박 큰 것", "단호박가루", "호박씨(선택가능)", "호박", "호박잎", "애호박", "애호박 다진 것", "애호박 3분의", "밤호박"],

        "10500": [],

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
        for key, value in allergy_data.items():
            if jaeryo in value:
                allergy_list.append(int(key))
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
        allergy_list, writer, content = get_content(pk)
        tem = {"model": "recipe_api.recipe", 
            "pk": pk, 
            "fields": {
                "writer": writer,
                "image": image, 
                "title": title, 
                "main_grocery": grocery_name,
                "allergies": allergy_list,
                "content": str(content),
                }
            }
        recipe_list.append(tem)
recipe_json.write(json.dumps(recipe_list, ensure_ascii=False))
grocery.close()
recipe_json.close()