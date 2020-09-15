# 장고(Django) 시작하기

## 1. Venv 환경 켜기
```bash
# backend 폴더 내에서
$ venv/Scripts/activate
# (venv) 표시가 있는지 확인
```

- venv 환경 종료
```bash
$ deactivate
```

## 2. 장고 설치하기

#### A. `requirement.txt`가 없는 경우
```bash
$ pip install django
```

#### B. `requirement.txt`가 있는 경우
```bash
# requirements.txt 내의 모든 라이브러리를 설치
$ pip install -r requirements.txt
```

#### 참고. requirement.txt 생성법
**반드시 venv 환경인지 확인합니다.**

```bash
$ pip freeze > requirements.txt
```

## 3. 장고 프로젝트 시작하기
```bash
$ django-admin startproject mysite
```

## 4. 장고 서버 실행
```bash
$ python manage.py runserver
```