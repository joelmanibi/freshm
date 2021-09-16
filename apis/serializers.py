from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
from main import models

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

class ClientSerializer(serializers.ModelSerializer):
    model = models.Client
    class Meta:
        fields = (
            'user',
            'Tel',
            'ville',
            'statut',
            'image',
        )

class AgentSerializer(serializers.ModelSerializer):
    model = models.Agent
    class Meta:
        fields = (
            'user',
            'Tel')

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'Nom',
            'prix',
            'description',
            'lieu',
            'image_produit',
            'agent',
        )
        model = models.Produit

class CommandeSerializer(serializers.ModelSerializer):
    model = models.Commande
    class Meta:
        fields = (
            'id',
            'client',
            'produit',
            'quantite',
            'Lieu_livraison',
            'date_commande',
            'ETAT',
            'date_livraison',
            'statut',
                )