# ============================================================
# IMPORTS
# ============================================================

# post_save :
# signal Django déclenché AUTOMATIQUEMENT
# après qu’un objet soit sauvegardé (save())
#
# Exemple :
# - création d’un objet
# - modification d’un objet
from django.db.models.signals import post_save


# receiver :
# décorateur qui permet de "brancher" une fonction
# à un signal Django
from django.dispatch import receiver


# Import du modèle Commentaire
from .models import Commentaire


# ============================================================
# SIGNAL : notification_commentaire
# ============================================================

# @receiver connecte cette fonction au signal post_save
#
# Donc :
# à chaque fois qu’un Commentaire est sauvegardé,
# cette fonction sera exécutée automatiquement
@receiver(post_save, sender=Commentaire)
def notification_commentaire(sender, instance, created, **kwargs):

    # --------------------------------------------------------
    # PARAMÈTRES IMPORTANTS
    # --------------------------------------------------------
    #
    # sender   : le modèle qui déclenche le signal (Commentaire)
    # instance : l’objet Commentaire qui vient d’être sauvegardé
    # created  : booléen
    #            True  -> nouvel objet créé
    #            False -> objet modifié
    # kwargs   : informations supplémentaires (rarement utilisées)
    #
    # --------------------------------------------------------


    # ========================================================
    # CONDITION : création ou modification ?
    # ========================================================
    #
    # created == True  → nouveau commentaire
    # created == False → commentaire modifié
    #
    # Ici ton code agit uniquement si ce n’est PAS une création
    # donc seulement lors d’une modification
    if created == True:

        # ----------------------------------------------------
        # RÉCUPÉRATION DES DONNÉES
        # ----------------------------------------------------

        # instance.article :
        # on accède à l’article lié au commentaire

        # .titre :
        # champ "titre" de l’article
        titre_article = instance.article.titre


        # instance.username :
        # utilisateur ayant écrit le commentaire
        
        auteur_commentaire = instance.username


        # instance.message :
        # contenu du commentaire
        contenu_commentaire = instance.message


    # ========================================================
    # AFFICHAGE
    # ========================================================
    #
    # print() :
    # affiche dans la console serveur (terminal)
    #
    # Cela sert souvent pour du debug
    # ou vérifier que le signal fonctionne
    #
        print(
                    f"Nouveau commentaire ! "
                    f"Article: {titre_article} | "
                    f"Auteur: {auteur_commentaire} | "
                    f"Message: {contenu_commentaire}"
                )