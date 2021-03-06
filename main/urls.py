from django.urls import path
from . import views
from .views import (
    menuDetail,
    ajouter_au_panier,
    get_panier_produits,
    commande_produit,
    CartDeleteView,
    commande_details,
    ajouter_produit,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('agent', views.agent, name='agent'),
    path('detail/<int:pk>', views.menuDetail, name='detail'),
    path('ajouter-au-panier/<int:pk>/', views.ajouter_au_panier, name='ajouter-au-panier'),
    path('ajouter-produit', views.ajouter_produit, name='ajouter-produit'),
    path('panier/', views.get_panier_produits, name='panier'),
    path('supprimé-du-panier/<int:pk>/', CartDeleteView.as_view(), name='supprimé-du-panier'),
    path('commande/', views.commande_produit, name='commande'),
    path('commande_details/', views.commande_details, name='commande_details'),
    path('signupclient', views.signup_client, name="signupclient"),
    path('signinclient', views.signin_client, name="signinclient"),
    path('logoutclient', views.logout_client, name="logoutclient"),
    path('signinagent', views.signin_agent, name="signinagent"),
]