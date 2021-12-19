from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth import login
from main import models
from .serializers import ProduitSerializer,AgentSerializer,CommandeSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


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

class ListProduit(generics.ListCreateAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = ProduitSerializer

class ListProduitAgent(generics.ListCreateAPIView):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        """
        Cette vue doit renvoyer une liste de tous les produits
        pour l'utilisateur actuellement authentifié.
        """
        user = self.request.user
        return models.Produit.objects.filter(agent=user)

class ListCommandeAgent(generics.ListCreateAPIView):
    serializer_class = CommandeSerializer

    def get_queryset(self):
        """
        Cette vue doit renvoyer une liste de tous les produits
        pour l'utilisateur actuellement authentifié.
        """
        user = self.request.user
        return models.Commande.objects.filter(produit__id= self.request.user.produit_.all() )

class DetailProduit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = ProduitSerializer

class ListAgent(generics.ListCreateAPIView):
    queryset = models.Agent.objects.all()
    serializer_class = AgentSerializer

class DetailAgent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Agent.objects.all()
    serializer_class = AgentSerializer