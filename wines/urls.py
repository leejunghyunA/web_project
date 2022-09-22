from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('choice/', views.choice, name = 'choice'),
    path('choice/postlist/', views.postlist, name='postlist'),
    path('choice/postdetail/<int:idx>/', views.postdetail, name='postdetail'),
    path('wines/search/', views.postsearch, name="postsearch"),
    path('flavor_cho/', views.flavor_cho, name='flavor_cho'),
    path('flavor_cho/flavor/<str:idx>/', views.flavor, name='flavor'),
    # path('<str:name>/', views.PostDetail.as_view()),
    # path('<int:slug>/', views.postdetail.as_view()),
    # path('var1/', views.var1, name = 'var1'),
    # path('var1/var1_result/', views.var1_result, name='var1_result'),
    # 
]