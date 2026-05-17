from django.urls import path
# from django.
from .views import ArticleListView, CategorieListView, ArticleDetailView, CommentUpdateView, CommentDeleteView, InscriptionView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='liste_article'),
    path('categories', CategorieListView.as_view(), name='liste_categorie'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='detail_article'),
    path('articles/<int:pk>/edit', CommentUpdateView.as_view(), name='update_comment'),
    path('articles/<int:pk>/delete', CommentDeleteView.as_view(), name='delete_comment'),
    path('register/', InscriptionView.as_view(), name='register'),
]
