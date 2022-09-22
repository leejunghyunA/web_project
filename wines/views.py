from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DateDetailView
import joblib
import pickle

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

    # wine__df = ['없음']
    # wine_type = request.GET.get('type')
    # df_dang = request.GET.get('dang')
    # # df_flavor = request.GET['Flavor']
    # df_mouthfeel = request.GET.get('body')
    # df_acidity = request.GET.get('acidity')

    # new_df = wine_df[(wine_df['당도']==df_dang)&(wine_df['산도']==df_acidity)&(wine_df['바디']==df_mouthfeel)&(wine_df['와인타입']==wine_type)]
    # context = {
    #     'names':new_df['와인이름'].tolist(),
    #     'types': new_df['와인타입'].tolist(),
    #     'dangs': new_df['당도'].tolist(),
    #     'foods': new_df['음식'].tolist(),
    # }

    # new_index = new_df.index.tolist()
    # new_names = new_df['와인이름'].tolist()
    # types = new_df['와인타입'].tolist()
    # dangs = new_df['당도'].tolist()
    # foods = new_df['음식'].tolist()
    # # post_list = len(new_names)
    # total_li = zip(new_index, new_names, types, dangs, foods)
    # total = len(new_index)

    # # 결과 담기
    # targetdict = {
    #     'wine_name': new_names,
    #     'wine_type' : types,
    #     'wine_dang' : dangs,
    #     'wine_foods' : foods,
    # }

    # targetJson = json.dumps(targetdict)
    # return render(request, 'wines/postlist.html', {'total_li': total_li, 'total': total})

    # return render(request, 'wines/postlist.html', {'result':new_names, 'wine_type': types, 'wine_dang': dangs, 'wine_foods': foods, 'post_list': post_list,})


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


# def var1(request):
#     return render(request, 'wines/var1.html')

# def var1_result(request):
#     wine_df = pd.read_csv('wines/semi_final.csv')
#     # wine__df = ['없음']
    
#     wine_type = request.GET['type']
#     df_dang = request.GET['dang']
#     # df_flavor = request.GET['Flavor']
#     df_mouthfeel = request.GET['body']
#     df_acidity = request.GET['acidity']

#     new_df = wine_df[(wine_df['당도']==df_dang)&(wine_df['산도']==df_acidity)&(wine_df['바디']==df_mouthfeel)&(wine_df['와인타입']==wine_type)]
    
#     new_names = new_df['와인이름'].tolist()
#     types = new_df['와인타입'].tolist()
#     dangs = new_df['당도'].tolist()
#     foods = new_df['음식'].tolist()

#     # # 결과 담기
#     # targetdict = {
#     #     'wine_name': new_names,
#     #     'wine_type' : types,
#     #     'wine_dang' : dangs,
#     #     'wine_foods' : foods,
#     # }

#     # targetJson = json.dumps(targetdict)

#     return render(request, 'wines/var1_result.html', {'result':new_names, 'wine_type': types, 'wine_dang': dangs, 'wine_foods': foods})

# def ver2(request):
#     return render(request, 'wines/ver2.html')