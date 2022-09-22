from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DateDetailView
import joblib
import pickle
# 검색기능
from django.db.models import Q
import pandas as pd
import numpy as np
import json

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
    li = ['녹색 과일','빨간 과일','허베이셔스','자연(Earthy)', '꽃','핵과', '오크(Oak)', '까만 과일', '열대 과일', '스파이스','허브','시트러스','이스트','유산발효','말린 허브','말린 과일']

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
    li = ['육류', '에피타이저', '매운음식', '해산물', 'sweet디저트', '양식', '중국음식', '디저트']

    return render(request, 'wines/foods_cho.html', {'foods_li': li})

def foods(request, fo_name):
    wine_df = pd.read_csv('wines/wine_final_real.csv')
    li1 = []
    for i in range(len(wine_df)):
        foods_ = wine_df['음식'][i].split(' ')
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