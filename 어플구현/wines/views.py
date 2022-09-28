from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
import joblib
import pickle
from .models import Pose
# 검색기능
from django.db.models import Q
import pandas as pd
import numpy as np
import json
# 애림쓰
import os
from django.http import JsonResponse
from django.views.generic import FormView
from django.core.files.storage import FileSystemStorage
from PIL import Image
import re
import pytesseract
from difflib import SequenceMatcher
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'wines/index.html')

def choice(request):
    return render(request, 'wines/choice.html')

def postlist(request):

    # 전처리할 파일
    # 연속형
    # cls = joblib.load('wines/wine_model_v2.pkl')
    # 범주형
    cls = joblib.load('wines/wine_model_v3범주형.pkl')
    
    df = pd.DataFrame(columns=['alcohol', 'dang', 'acidity', 'body', 'type'])
    lis = []
    lis.append(request.GET.get('alcohol'))
    lis.append(request.GET.get('dang'))
    lis.append(request.GET.get('acidity'))
    lis.append(request.GET.get('body'))
    lis.append(request.GET.get('type'))

    df.loc[0, :] = lis
    ans = cls.predict(df)
    ans1 = ans.tolist()[0]

    wine_df = pd.read_csv('wines/wine_final_real.csv')
    
    new_df = wine_df[wine_df['추천솔루션 군집화_n']==ans1]

    new_clus = new_df['추천솔루션 군집화'].tolist()[0]
    new_index = new_df.index.tolist()
    new_names = new_df['와인이름'].tolist()
    types = new_df['와인타입'].tolist()
    dangs = new_df['당도'].tolist()
    foods = new_df['음식'].tolist()
    total_li = zip(new_index, new_names, types, dangs, foods)
    total = len(new_index)

    return render(request, 'wines/postlist.html', {'total_li': total_li, 'total': total, 'new_clus':new_clus})

def postdetail(request,idx):
    wine_df = pd.read_csv('wines/wine_final_real.csv')

    #idx = int(request.GET.get('idx'))
    #print(id)
    new_df = wine_df.loc[idx, :]

    new_names = new_df['와인이름']
    new_ennames = new_df['영어이름']
    types = new_df['와인타입']
    country = new_df['나라, 와이너리']
    grape = new_df['포도종']
    alcohol = int(new_df['도수'])
    dangs = new_df['당도']
    acidity = new_df['산도']
    body = new_df['바디']
    winery = new_df['와이너리이름']
    winery_info = new_df['와이너리설명']
    winery_ch = new_df['와이너리특징']
    aroma_ = new_df['아로마 딕셔너리']
    aroma_keys = list(eval(aroma_).keys())
    aroma_values = list(eval(aroma_).values())
    aroma_zip = zip(aroma_keys, aroma_values)

    foods = new_df['곁들일 음식']

    return render(request, 'wines/postdetail.html', {'result':new_names, 'enname': new_ennames, 'types': types, 'country':country, 'grape':grape, 'alcohol':alcohol, 'acidity':acidity, 'body':body, 'winery':winery, 'winery_info':winery_info, 'winery_ch':winery_ch, 'aroma_zip':aroma_zip, 'dangs': dangs, 'foods': foods})

# 검색 창 페이지
def postsearch(request):
    search = str(request.GET.get('search'))
    wine_df = pd.read_csv('wines/wine_final_real.csv')
    li1 = []
    for i in range(len(wine_df)):
        if search in wine_df['와인이름'][i]:
            li1.append(i)
    
    new_df = wine_df.loc[li1]
    new_index = li1
    new_names = new_df['와인이름'].tolist()
    types = new_df['와인타입'].tolist()
    dangs = new_df['당도'].tolist()
    foods = new_df['음식'].tolist()
    total_li = zip(new_index, new_names, types, dangs, foods)
    total = len(new_index)

    return render(request, 'wines/postsearch.html', {'total_li': total_li, 'total': total, 'search_value': search})

def flavor_cho(request):
    li = ['녹색 과일','빨간 과일','허베이셔스','자연(Earthy)', '꽃','핵과', '오크(Oak)', '까만 과일', '열대 과일', '스파이스','허브','시트러스','이스트','유산발효','말린 허브']

    return render(request, 'wines/flavor_cho.html', {'flavor_li': li})

def flavor(request, name):
    # choice_flavor = str(request.GET.get('flavor'))
    wine_df = pd.read_csv('wines/wine_final_real.csv')
    li1 = []
    for i in range(len(wine_df)):
        aroma_ = wine_df['아로마 딕셔너리'][i]
        aroma_ = list(eval(aroma_).keys())
        if name in aroma_:
            li1.append(i)
    new_df = wine_df.loc[li1]
    new_index = li1
    new_names = new_df['와인이름'].tolist()
    types = new_df['와인타입'].tolist()
    dangs = new_df['당도'].tolist()
    foods = new_df['음식'].tolist()
    total_li = zip(new_index, new_names, types, dangs, foods)
    total = len(new_index)

    return render(request, 'wines/flavor.html', {'total_li': total_li, 'total': total, 'choice_flavor': name})

# foods선택 안 
def foods_cho(request):
    li = ['육류', '양식', '중국음식', '해산물', '매운음식', '에피타이저', 'sweet디저트']

    return render(request, 'wines/foods_cho.html', {'foods_li': li})

def foods(request, fo_name):
    wine_df = pd.read_csv('wines/wine_final_real.csv')
    
    li1 = []
    for i in range(len(wine_df)):
        foods_ = wine_df['음식'][i].split(' ')

        # 디저트인 것도 sweet에 포함
        if fo_name == "sweet디저트":
            if "디저트" in foods_:
                li1.append(i)
            elif fo_name in foods_:
                li1.append(i)
            else:
                pass
        else:
            if fo_name in foods_:
                li1.append(i)

    new_df = wine_df.loc[li1]
    new_index = li1
    new_names = new_df['와인이름'].tolist()
    types = new_df['와인타입'].tolist()
    dangs = new_df['당도'].tolist()
    foods = new_df['음식'].tolist()
    total_li = zip(new_index, new_names, types, dangs, foods)
    total = len(new_index)

    return render(request, 'wines/foods.html', {'total_li': total_li, 'total': total, 'choice_foods': fo_name})

    # foods선택 안 
def situation_cho(request):
    li = ['가족과 함께', '술린이 연인과함께', '달콤한 친구와 함께', '술른이 연인과함께', '화끈한 친구와 함께']
    index_li = [0, 1, 2, 3, 4]
    total_li = zip(index_li, li)

    return render(request, 'wines/situation_cho.html', {'situation_li': total_li})

def situation(request, si_index):
    wine_df = pd.read_csv('wines/wine_final_real.csv')
    new_df = wine_df[wine_df['상황별추천 군집화_n']==si_index]

    new_clus = new_df['상황별추천 군집화'].tolist()[0]
    new_index = new_df.index.tolist()
    new_names = new_df['와인이름'].tolist()
    types = new_df['와인타입'].tolist()
    dangs = new_df['당도'].tolist()
    foods = new_df['음식'].tolist()
    total_li = zip(new_index, new_names, types, dangs, foods)
    total = len(new_index)

    return render(request, 'wines/situation.html', {'total_li': total_li, 'total': total, 'new_clus':new_clus})

def char_cho(request):
    return render(request, 'wines/char_cho.html')

def char(request):
    dang = int(request.GET.get('dangdo'))
    acidity = int(request.GET.get('acidity_'))
    body = int(request.GET.get('body_'))

    wine_df = pd.read_csv('wines/wine_final_real.csv')
    
    new_df = wine_df[(wine_df['당도']==dang)&(wine_df['산도']==acidity)&(wine_df['바디']==body)]


    new_index = new_df.index.tolist()
    new_names = new_df['와인이름'].tolist()
    types = new_df['와인타입'].tolist()
    dangs = new_df['당도'].tolist()
    foods = new_df['음식'].tolist()
    total_li = zip(new_index, new_names, types, dangs, foods)
    total = len(new_index)

    return render(request, 'wines/char.html', {'total_li': total_li, 'total': total, 'acidity': acidity, 'body':body, 'dangs':dang})

# 사진 검색 기능
pytesseract.pytesseract.tesseract_cdm = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
@csrf_exempt
def ocr_upload(request):
    context = {}

    imgname = ''
    text = ''
    # 업로드파일이 있는 경우 업로드 파일을 받아들임
    if 'uploadfile' in request.FILES:
        uploadfile = request.FILES.get('uploadfile', '')

        if uploadfile != '':
                
            # 파일이름 받기
            name_old = uploadfile.name

            # 파일 확장자이름를 받기
            name_ext = os.path.splitext(name_old)[1]

            # 파일 시스템에서 static안에 source에 파일을 저장하겠음
            fs = FileSystemStorage(location = 'static/source')
            # 업로드 시 저장될 이미지 파일이름 지정, imgname은 실제 저장되는 이름을 객체로 받은 것
            imgname = fs.save(f'src-{name_old}', uploadfile)
            
    
            # 파일을 불러내서 텍스트 추출
            imgfile = Image.open(f'./static/source/{imgname}')
            text = pytesseract.image_to_string(imgfile, lang = 'kor+eng', config = '-c preserve_interword_space=1 --psm 4')

            #########################################################################################v
            # 데이터프레임 내 와인이름 전처리
            wine_df = pd.read_csv('wines/wine_final_real.csv')

            # 데이터프레임 내 와인 이름 단어 추출
            wine_li_all = wine_df['와인이름'].tolist() + wine_df['영어이름'].tolist()
            
            context['imgname'] = imgname
            context['text'] = text

            # 삭제해야하는 단어 지정
            stopwords = ['\"','&', "\'", '\(', '\)', ',', '-', '[.]', '/','‘','’','“','”']

            # 한국어인지 영어인지 확인하는 사용자함수 생성
            def is_English_Korean(str):
                k_cnt, e_cnt = 0, 0
                
                for s in str:
                    # ord: 문자의 유니코드 값을 돌려주는 함수
                    if ord('가') <= ord(s) <= ord('힣'):
                        k_cnt += 1
                    elif ord('a') <= ord(s.lower()) <= ord('z'):
                        e_cnt += 1
                        
                return "한국어" if k_cnt > e_cnt else "영어"

            # 리스트 생성하기
            wine_li_delete_stopword = []
            wine_li_delete_blank = []
            for name in wine_li_all:
                # 영어면 소문자로 변경하기
                if is_English_Korean(name) == '영어':
                    name = name.lower()
                
                # 정규표현식으로 삭제해야하는 단어 제거
                # 띄어쓰기제거 한 와인이름 리스트도 생성
                for s in stopwords:
                    name = re.sub(s, '', name)
                    name2 = re.sub('\s','', name)
                wine_li_delete_stopword.append(name)
                wine_li_delete_blank.append(name2)
                
                
            # 데이터프레임 내 와인이름 단어 리스트 중복 제거
            wine_str_set = list(set(' '.join(wine_li_delete_stopword).split()))
            
            # 텍스트, 숫자로만 이루어진 단어 추출
            word_li = [word.lower() for word in re.findall('\w+',text)]

            # 중복 제거된 와인 이름 단어 리스트 내 존재하면 찾아야할 와인이름 완성하기
            wine_name = ''
            for w in word_li:
                if w in wine_str_set:
                    wine_name += w
            context['wine_name'] = wine_name.title()

            # 검색해야되는 와인이름 언어가 국문/영문인지 확인
            wine_lang = is_English_Korean(wine_name)        
            context['wine_lang'] = wine_lang

            # 데이터프레임 내 국문 와인이름 리스트, 영문 와인이름 리스트 구분  
            wine_ko = wine_li_delete_blank[:325]
            wine_en = wine_li_delete_blank[325:]

            # 해당 와인 이름과 60% 이상 일치하는 와인 인덱스 불러오기
            ## 와인데이터프레임 복사
            wine_df_result = wine_df.copy()
            wine_df_result['와인이름 일치율'] = np.nan

            ## 한국어/영어 구분하고 와인이름 일치율을 내림차순 정렬, 새로운 데이터프레임 생성
            if wine_lang == '한국어':
                for idx, df_wine_name in enumerate(wine_ko):
                    search_range = SequenceMatcher(None, df_wine_name, wine_name).ratio()
                    if search_range > 0.5:
                        wine_df_result.loc[idx,'와인이름 일치율'] = search_range

            else:
                for idx, df_wine_name in enumerate(wine_en):
                    search_range = SequenceMatcher(None, df_wine_name, wine_name).ratio()
                    if search_range > 0.5:
                        wine_df_result.loc[idx,'와인이름 일치율'] = search_range

            wine_df_result = wine_df_result.sort_values(by = '와인이름 일치율', ascending = False).dropna(subset = ['와인이름 일치율'])
            

            # 일치율에 따라 데이터 불러오기
            # 일치율이 1이면 바로 출력
            if len(wine_df_result[wine_df_result['와인이름 일치율'] == 1]):
                output = wine_df_result[wine_df_result['와인이름 일치율'] == 1]

            # 일치하는게 하나도 없으면 해당와인없음 반환
            elif len(wine_df_result) == 0:
                output = wine_df_result

            else:
                output = wine_df_result

            new_index = output.index.tolist()
            new_names = output['와인이름'].tolist()
            types = output['와인타입'].tolist()
            dangs = output['당도'].tolist()
            foods = output['음식'].tolist()
            total_li = zip(new_index, new_names, types, dangs, foods)
            total = len(new_index)  

            context['total_li'] = total_li
            context['total'] = total              

    return render(request, 'wines/postlist_image.html', context)

# def like_list(request, like_name):
#     wine_df = pd.read_csv('wines/wine_final_real.csv')
#     new_df = wine_df[wine_df['와인이름'] == str(like_name)]

#     new_names = new_df['와인이름'].tolist()[0]
#     grape = new_df['포도종'].tolist()[0]

#     return render(request, 'wines/like_list.html', {'result':new_names, 'grape':grape})

def like_list(request):
    wine_df = pd.read_csv('wines/wine_final_real.csv')
    if request.method == 'POST':
        like_name = request.POST.get('like_li')

        new_post = Pose()
        
        new_df = wine_df[wine_df['와인이름'] == str(like_name)]
        index_ = new_df.index
        idx = index_.values[0]
        new_post.name = like_name
        new_post.enname = new_df.loc[idx, '영어이름']
        new_post.save()

        like_list = Pose.objects.all()

        return render(request, 'wines/like_list.html', context={'result': like_list[:2]})
    else:
        return render(request, 'wines/like_list.html')