from django.urls import path

from posts.views import article_detail, article_list

urlpatterns = [
    
    path('article/<int:id>/', article_detail, name='article_detail'),
    path('articles/', article_list, name='article_list'),

]