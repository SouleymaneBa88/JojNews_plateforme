from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

from .models import Article, Categorie, Commentaire
from .forms import CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = 'liste_article.html'
    context_object_name = 'articles'


class CategorieListView(ListView):
    model = Categorie
    template_name = 'liste_categorie.html'
    context_object_name = 'categories'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail_article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = Commentaire.objects.filter(
            article=self.object
        ).order_by('-date_commentaire')

        context['form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.username = request.user
            commentaire.article = self.object
            commentaire.save()

            return redirect('detail_article', pk=self.object.pk)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Commentaire
    form_class = CommentForm
    template_name = 'update_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.username

    def get_success_url(self):
        return reverse('detail_article', kwargs={'pk': self.object.article.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentaire
    template_name = 'delete_comment.html'

    def get_success_url(self):
        return reverse('detail_article', kwargs={'pk': self.object.article.pk})


class InscriptionView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')