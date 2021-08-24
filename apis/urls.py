from django.urls import path
from .views import UserRecordView,ListProduit, DetailProduit

app_name = 'apis'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('', ListProduit.as_view()),
    path('<int:pk>/', DetailProduit.as_view())
]


