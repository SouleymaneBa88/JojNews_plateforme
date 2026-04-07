from django.urls import path
from . import views

urlpatterns = [
    # path('',views.liste_article,name='category'),
    path('',views.poste_commentaire,name='commentaire'),
]
