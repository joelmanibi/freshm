from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from main import models
from .serializers import ProduitSerializer
from rest_framework import generics


class UserRecordView(APIView):
    """
    API View pour créer ou obtenir une liste de tous les inscrits
    utilisateurs. La requête GET renvoie les utilisateurs enregistrés alors que
    une requête POST permet de créer un nouvel utilisateur.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class ProduitRecordView(APIView):
    """
    API View pour créer ou obtenir une liste de tous les inscrits
    utilisateurs. La requête GET renvoie les utilisateurs enregistrés alors que
    une requête POST permet de créer un nouvel utilisateur.
    """
    

    def get(self, format=None):
        produits = Produit.objects.all()
        serializer = ProduitSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )



class ListProduit(generics.ListCreateAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = ProduitSerializer


class DetailProduit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = ProduitSerializer