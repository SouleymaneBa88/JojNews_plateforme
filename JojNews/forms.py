from django import forms
from .models import Commentaire

class PosterCommentaire(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']