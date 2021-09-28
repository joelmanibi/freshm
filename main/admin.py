from django.contrib import admin

# Register your models here.
from .models import Produit,Client,Commande,Agent
admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Produit)
admin.site.register(Agent)