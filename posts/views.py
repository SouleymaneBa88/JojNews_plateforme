from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Article, Categorie
import requests
# def article_detail(request, id):
    # article = Article.objects.get(id=id)
    # commentaires = article.commentaires.all()

    # return render(request, "articles/article_detail.html", {
    #     "article": article,
    #     "commentaires": commentaires
    # })
def article_detail(request, id):

    article = get_object_or_404(Article, id=id)
    commentaires = article.commentaires.all()

    # 🔥 génération du résumé
    if request.method == "POST":

        # si déjà existant → on ne recalcul pas (optimisation)
        if not article.resume_ia:

            prompt = f"""
            Résume cet article simplement :

            {article.contenu}
            """

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "mistral",
                    "prompt": prompt,
                    "stream": False
                }
            )

            data = response.json()
            article.resume_ia = data["response"]

            # 💾 SAUVEGARDE EN BASE
            article.save()

    return render(request, "articles/article_detail.html", {
        "article": article,
        "commentaires": commentaires
    })


def article_list(request):

    categorie_id = request.GET.get("categorie")

    categories = Categorie.objects.all()

    articles = Article.objects.all().order_by('-date_creation')

    # FILTRE
    if categorie_id:
        articles = articles.filter(categorie_id=categorie_id)

    # PAGINATION
    paginator = Paginator(articles, 4)

    page_number = request.GET.get("page")

    articles = paginator.get_page(page_number)

    return render(request, "articles/article_list.html", {
        "articles": articles,
        "categories": categories,
        "categorie_active": categorie_id
    })
    