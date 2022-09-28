from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('choice/', views.choice, name = 'choice'),
    path('choice/postlist/', views.postlist, name='postlist'),
    path('choice/postdetail/<int:idx>/', views.postdetail, name='postdetail'),
    path('wines/search/', views.postsearch, name="postsearch"),
    path('flavor_cho/', views.flavor_cho, name='flavor_cho'),
    path('flavor_cho/flavor/<str:name>/', views.flavor, name='flavor'),
    path('foods_cho/', views.foods_cho, name='foods_cho'),
    path('foods_cho/foods/<str:fo_name>/', views.foods, name='foods'),
    path('situation_cho/', views.situation_cho, name='situation_cho'),
    path('situation_cho/situation/<int:si_index>/', views.situation, name='situation'),
    path('char_cho/', views.char_cho, name='char_cho'),
    path('char_cho/char/', views.char, name="char"),
    path('ocr_upload', views.ocr_upload, name = 'ocr_upload'),
    path('like_list/', views.like_list, name= 'like_list'),
]