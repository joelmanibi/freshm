from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Commande,Produit


class ClientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

        widgets = {
        'password': forms.PasswordInput(),
        }
 

class ProduitForm(forms.ModelForm):
    class Meta:
        model=models.Produit
        fields=['Nom','prix','description','lieu','image_produit']

class commandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['quantite','Lieu_livraison']
