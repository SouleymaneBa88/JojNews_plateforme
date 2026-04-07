from django.shortcuts import render
from .models import Categorie,Commentaire,Article
from django.shortcuts import render,get_object_or_404,redirect
from .forms import PosterCommentaire
from django.contrib.auth.decorators import login_required

# Create your views here.
def liste_article(request):
    article_list = Article.objects.all()
    context = {'list': article_list}
    return render(request,'article.html',context)

def detail_traiteur(request, id):
    detail_article = get_object_or_404(Article,id = id)
    context = {
        'traiteur': detail_article
    }

    return render(request,'detail.html',context)

@login_required(login_url='connexion/')
def poste_commentaire(request):
    form = PosterCommentaire()
    if request.method == 'POST':
        if form.is_valid():
            form .save()
            form = Commentaire

            # return redirect()
    context = {
        'form':form
    }
    return render(request,'index.html',context)

@login_required
def modifier_commentaire(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)

    if commentaire.auteur != request.user:
        return redirect('article_list')

    form = PosterCommentaire(request.POST or None, instance=commentaire)

    if form.is_valid():
        form.save()
        return redirect('article_list')

    return render(request, 'modifier.html', {'form': form})

@login_required
def supprimer_commentaire(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)

    if commentaire.auteur != request.user:
        return redirect('article_list')

    commentaire.delete()
    return redirect('article_list')