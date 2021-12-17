from django.urls import path
from .views import UserRecordView,ListProduit,ListProduitAgent,ListCommandeAgent, DetailProduit,ListAgent, DetailAgent,CustomAuthToken


urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('list-produit', ListProduit.as_view()),
    path('list-produit-agent', ListProduitAgent.as_view()),
    path('list-commande-agent', ListCommandeAgent.as_view()),
    path('list-produit/<int:pk>/', DetailProduit.as_view()),
    path('list-agent', ListAgent.as_view()),
    path('list-agent/<int:pk>/', DetailAgent.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
]


