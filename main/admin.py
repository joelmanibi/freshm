from django.contrib import admin

# Register your models here.
from .models import Produit,client,Commande

admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Produit)