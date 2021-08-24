from django.shortcuts import render,redirect,get_object_or_404,reverse
from . import forms
from django.views.decorators.csrf import csrf_exempt
from .models import Produit,Commande,Client
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.db.models import Sum
from datetime import date
from .forms import commandeForm
# Create your views here.


def signup_client(request):
    userForm=forms.ClientUserForm()
    clientForm=forms.ClientForm()
    mydict={'userForm':userForm,'clientForm':clientForm}
    if request.method=='POST':
        userForm=forms.ClientUserForm(request.POST)
        clientForm=forms.ClientForm(request.POST,request.FILES)
        if userForm.is_valid() and clientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            client=clientForm.save(commit=False)
            client.user=user
            client.save()
        return HttpResponseRedirect("/")
    return render(request,'main/signupclient.html',context=mydict)

@csrf_exempt
def signin_client(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, 'main/signinclient.html',{'form':form})

def logout_client(request):
    if request.method == 'POST':
        logout(request)
    return redirect("signinclient")

def signup_agent(request):
    userForm=forms.AgentUserForm()
    agentForm=forms.AgentForm()
    dicti={'userForm':userForm,'agentForm':agentForm}
    if request.method=='POST':
        userForm=forms.AgentUserForm(request.POST)
        agentForm=forms.AgentForm(request.POST,request.FILES)
        if userForm.is_valid() and agentForm.is_valid():
            g = Group.objects.get(name='Agents')
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            agent=agentForm.save(commit=False)
            agent.user=user
            agent.save()
            g.user_set.add(agent)
        return HttpResponseRedirect('dashboardclient')
    return render(request,'main/signupagent.html',context=dicti)

@login_required(login_url='adminlogin')
def signin_agent(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
    else:
        form = AuthenticationForm()
    return render(request, 'main/signinagent.html',{'form':form})

@login_required(login_url='signinclient')
def index(request):
    users = User.objects.all()
    panier_produits = Commande.objects.filter(statut:=False)
    taille= len(panier_produits)
    query = request.GET.get('query')
    if query:
        produits = Produit.objects.filter(Nom__icontains=query)

    else:
        produits = Produit.objects.all()
    context = {
            'panier_produits':panier_produits,
            'taille':taille,
            'produits':produits,
            'users':users
    }
    return render(request, 'main/index.html',context)

@login_required(login_url='signinclient')
def menuDetail(request, slug):

    if request.user.client:
        produit = Produit.objects.filter(slug=slug).first()
        panier_produits = Commande.objects.filter(client=request.user.client,statut
        m!=False)
        taille= len(panier_produits)
        context = {
            'produit' : produit,
            'taille':taille,
        }
        return render(request, 'main/detail.html', context)
    else:
        return redirect("signinclient")

@login_required(login_url='signinclient')
def ajouter_au_panier(request, slug):
    if request.method == 'POST':
        produit = get_object_or_404(Produit, slug=slug)
        quantite=request.POST.get('quantite')
        Lieu_livraison = request.POST.get('Lieu_livraison')
        commande = Commande.objects.create(
        produit=produit,
        client=request.user.client,
        commandé=False,
        quantite=quantite,
        Lieu_livraison=Lieu_livraison
    )
    messages.info(request, "ajouté au panier avec succes!! Continuer vos achat")
    return redirect("panier")

@login_required(login_url='signinclient')
def get_panier_produits(request):

    panier_produits = Commande.objects.filter(client=request.user.client,statut=False)
    prix = panier_produits.aggregate(Sum('produit__prix_kg'))
    qte = panier_produits.aggregate(Sum('quantite'))
    total = prix.get("produit__prix_kg__sum")
    count = qte.get("quantite__sum")
    taille= len(panier_produits)
    context = {
            
            'panier_produits':panier_produits,
            'total': total,
            'count': count,
            'taille':taille,
         }
    return render(request, 'main/panier.html', context)

class CartDeleteView(DeleteView):
    model = Commande
    success_url = '/panier/'

    def test_func(self):
        panier = self.get_object()
        if self.request.client == panier.client:
            return True
        return False

def commande_produit(request):
    panier_produits = Commande.objects.filter(client=request.user.client,statut=False)
    date_commande=date.today()
    panier_produits.update(statut=True, date_commande=date_commande)
    messages.info(request, "Produit commandé avec succes")
    return redirect("commande_details")

def commande_details(request):
    produits = Commande.objects.filter(client=request.user.client, statut=True,statut="En cours").order_by('-date_commande')
    panier_produits = Commande.objects.filter(client=request.user.client, statut=True,statut="Livré").order_by('-date_commande')
    prix = produits.aggregate(Sum('produit__prix_kg'))
    number = produits.aggregate(Sum('quantite'))
    total = prix.get("produit__prix_kg__sum")
    count = number.get("quantite__sum")
    context = {
        'produits':produits,
        'panier_produits':panier_produits,
        'total': total,
        'count': count,
    }
    return render(request, 'main/commande_details.html', context)