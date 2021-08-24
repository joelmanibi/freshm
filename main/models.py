from django.db import models

# Create your models here.
class Client(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Tel = PhoneNumberField(blank=True)
    ville = models.CharField(max_length=50,null=False)
    statut = models.BooleanField(default=False) 
    image= models.ImageField(upload_to='image_client',null=True,blank=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Produit(models.Model):

    ETAT = (
        ('Bon', 'Bon'),
        ('Moyen', 'Moyen'),
        ('Epuisé', 'Epuisé')
        )

    Nom=models.CharField(max_length=40)
    prix = models.IntegerField()
    description=models.TextField()
    lieu = models.CharField(max_length=40)
    etat_stock = models.CharField(max_length=15, choices=ETAT, blank=True)
    image_produit= models.ImageField(upload_to='image_produit',null=True,blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.Nom
    
    def get_ajouter_au_panier_url(self):
        return reverse("ajouter-au-panier", kwargs={
            'slug': self.slug
        })



class Commande(models.Model):
    ETAT = (
        ('Livré', 'Livré'),
        ('En cours', 'En cours'),
        ('Annulé', 'Annulé')
        )

    client = models.ForeignKey('Client', on_delete=models.CASCADE,null=True)
    produit=models.ForeignKey('Produit',on_delete=models.CASCADE,null=True)
    quantite = models.PositiveIntegerField(default=1)
    Lieu_livraison = models.CharField(max_length=40)
    date_commande= models.DateField(auto_now_add=True)
    ETAT = models.CharField(max_length=15, choices=ETAT, default='En cours')
    date_livraison = models.DateField(null=True)
    statut = models.BooleanField(default=False)

    def prix_total(self):
        price = self.produit.prix_kg
        quantity = self.quantite
        total = price*quantity
        print(total)
        return total

    def __str__(self):
        return self.produit.Nom