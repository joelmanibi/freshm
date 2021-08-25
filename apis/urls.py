from django.urls import path
from .views import UserRecordView,ListProduit, DetailProduit


urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('produit/', ProduitRecordView.as_view(), name='produits'),
    path('list', ListProduit.as_view()),
    path('<int:pk>/', DetailProduit.as_view())
]


