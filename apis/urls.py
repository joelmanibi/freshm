from django.urls import path
from .views import UserRecordView,ListProduit, DetailProduit

app_name = 'apis'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view())
]


