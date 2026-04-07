from django.contrib import admin
from .models import Categorie,Article,Commentaire
# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom',)
    search_fields =('nom',)

    def has_add_permission(self, request):
        return request.user.is_staff
    
    def has_change_permission(self, request, obj = None):
        return request.user.is_staff
    
    def has_delete_permission(self, request, obj = None):
        return request.user.is_staff

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','auteur_nom',)
    list_filter=('categorie','date_creation',)
    search_fields=('titre','auteur_nom',)

    def has_add_permission(self, request):
        return request.user.is_staff
    
    def has_change_permission(self, request, obj = None):
        return request.user.is_staff
    
    def has_delete_permission(self, request, obj = None):
        return request.user.is_staff

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('article','auteur_nom','date_creation',)
    list_filter=('article','auteur','date_creation')
    search_fields=('date_creation','auteur',)
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = None):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False
