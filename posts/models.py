from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    categorie_nom = models.CharField(max_length=100, editable=False)

    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    auteur_nom = models.CharField(max_length=100, editable=False)

    def save(self, *args, **kwargs):
        if self.categorie and not self.categorie_nom:
            self.categorie_nom = self.categorie.nom

        if self.auteur and not self.auteur_nom:
            self.auteur_nom = self.auteur.username

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    contenu = models.TextField()

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="commentaires"
    )

    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    auteur_nom = models.CharField(max_length=100, editable=False)

    def save(self, *args, **kwargs):
        if self.auteur and not self.auteur_nom:
            self.auteur_nom = self.auteur.username

        super().save(*args, **kwargs)

    def __str__(self):
        return self.contenu[:50]