from django.contrib import admin

# Register your models here.
from .models import Produit,Commande,Agent
admin.site.register(Commande)
admin.site.register(Produit)
admin.site.register(Agent)