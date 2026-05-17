from django.contrib import admin
from .models import Categorie, Article, Commentaire
from django.utils.html import format_html
from django.utils.timezone import localtime

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("id", "nom")
    search_fields = ("nom",)
    ordering = ("nom",)


from django.utils.html import format_html

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "apercu_article", "categorie", "auteur_badge")
    list_filter = ("categorie", "date_creation")
    search_fields = ("titre", "contenu", "auteur_nom")
    ordering = ("-date_creation",)

    exclude = ("auteur",)

    readonly_fields = (
        "categorie_nom",
        "auteur_nom",
        "date_creation",
        "date_modification",
    )

    fieldsets = (
        ("Informations principales", {
            "fields": ("titre", "contenu", "image")
        }),
        ("Relations", {
            "fields": ("categorie",)
        }),
        ("Informations sauvegardées", {
            "fields": ("categorie_nom", "auteur_nom"),
            "classes": ("collapse",)
        }),
        ("Dates", {
            "fields": ("date_creation", "date_modification"),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.auteur:
            obj.auteur = request.user
        super().save_model(request, obj, form, change)

    def auteur_badge(self, obj):
        if obj.auteur:
            return format_html(
                "<span style='background:#ce1126; color:white; padding:4px 8px; border-radius:8px;'>{}</span>",
                obj.auteur.username
            )
        return "Inconnu"

    auteur_badge.short_description = "Auteur"

    def apercu_article(self, obj):
        image_url = obj.image.url if obj.image else ""

        # format date en français
        date = localtime(obj.date_creation)
        date_formattee = date.strftime("%d %B %Y à %H:%M")

        return format_html(
            """
            <div style="
                display:flex;
                gap:12px;
                align-items:center;
                padding:10px;
                border-radius:12px;
                background:#fff;
                box-shadow:0 5px 15px rgba(0,0,0,0.1);
            ">
                {}
                <div>
                    <div style="font-weight:bold; font-size:15px; color:#00853f;">
                        {}
                    </div>
                    <div style="color:#555; font-size:13px; margin:5px 0;">
                        {}...
                    </div>
                    <div style="font-size:11px; color:gray;">
                        {}
                    </div>
                </div>
            </div>
            """,
            format_html(
                '<img src="{}" style="width:90px; height:90px; object-fit:cover; border-radius:10px;">',
                image_url
            ) if image_url else "",
            obj.titre,
            obj.contenu[:80],
            date_formattee
        )

    apercu_article.short_description = "Article"

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