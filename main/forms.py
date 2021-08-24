from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Commande,Client


class ClientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        
        widgets = {
        'password': forms.PasswordInput(),
        }
 
        
class ClientForm(forms.ModelForm):
    class Meta:
        model=models.Client
        fields=['Tel','ville','image']


class commandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['quantite','Lieu_livraison']
