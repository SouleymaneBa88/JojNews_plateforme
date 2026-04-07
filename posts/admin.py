from django.contrib import admin
from .models import Categorie, Article, Commentaire


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("id", "nom")
    search_fields = ("nom",)
    ordering = ("nom",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "titre", "categorie", "auteur", "date_creation")
    list_filter = ("categorie", "date_creation")
    search_fields = ("titre", "contenu", "auteur_nom")
    ordering = ("-date_creation",)

    readonly_fields = (
        "categorie_nom",
        "auteur_nom",
        "date_creation",
        "date_modification",
    )

    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "contenu")
        }),
        ("Relations", {
            "fields": ("categorie", "auteur")
        }),
        ("Informations sauvegardées", {
            "fields": ("categorie_nom", "auteur_nom"),
            "classes": ("collapse",)
        }),
        ("Dates", {
            "fields": ("date_creation", "date_modification"),
        }),
    )


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("id", "contenu_court", "article", "auteur", "date_creation")
    list_filter = ("date_creation",)
    search_fields = ("contenu", "auteur_nom")
    ordering = ("-date_creation",)

    readonly_fields = (
        "auteur_nom",
        "date_creation",
        "date_modification",
    )

    fieldsets = (
        ("Contenu", {
            "fields": ("contenu",)
        }),
        ("Relations", {
            "fields": ("article", "auteur")
        }),
        ("Informations sauvegardées", {
            "fields": ("auteur_nom",),
            "classes": ("collapse",)
        }),
        ("Dates", {
            "fields": ("date_creation", "date_modification"),
        }),
    )

    def contenu_court(self, obj):
        return obj.contenu[:50]

    contenu_court.short_description = "Commentaire"