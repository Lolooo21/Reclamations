

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Client, Entreprise, Reclamation

from.forms import ClientForm, ReclamationForm, EntrepriseForm

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'reclapp/pages/home.html', context)

def entreprises(request: HttpRequest) -> HttpResponse:
    entreprises = Entreprise.objects.all().order_by()
    context = { "entreprises": entreprises }
    return render(request, 'reclapp/pages/entreprises.html', context)

def clients(request: HttpRequest) -> HttpResponse:
    clients = Client.objects.all().order_by()
    context = { "clients": clients }
    return render(request, 'reclapp/pages/clients.html', context)    

def reclamations(request: HttpRequest) -> HttpResponse:
    reclamations = Reclamation.objects.all().order_by()
    context = { "reclamations": reclamations }
    return render(request, 'reclapp/pages/reclamations.html', context) 


def client(request: HttpRequest, pk: str) -> HttpResponse:
    client = Client.objects.get(id=pk)
    context = { "client": client }
    return render(request, 'reclapp/pages/client.html', context)


def entreprise(request: HttpRequest, pk: str) -> HttpResponse:
    entreprise = Entreprise.objects.get(id=pk)
    context = { "entreprise": entreprise }
    return render(request, 'reclapp/pages/entreprise.html', context)


def reclamation(request: HttpRequest, pk: str) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    context = { "reclamation": reclamation }
    return render(request, 'reclapp/pages/reclamation.html', context)



def create_client(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClientForm(request.POST) #POST on récupère l'information 
        if form.is_valid:
            form.save()
        return redirect('clients')

    form = ClientForm()
    context = {'form': form, "type":"create"}
    return render(request, 'reclapp/pages/create_client.html',context)


def update_client(request: HttpRequest, pk: str) -> HttpResponse:
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid:
            form.save()
        return redirect('clients')
    context = {'form': form,"type":"update"}
    return render(request, 'reclapp/pages/create_client.html',context)


def delete_client(request: HttpRequest, pk:str) -> HttpResponse:
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect('clients')


def create_entreprise(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EntrepriseForm(request.POST) #POST on récupère l'information 
        if form.is_valid:
            form.save()
        return redirect('entreprises')

    form = EntrepriseForm()
    context = {'form': form, "type":"create"}
    return render(request, 'reclapp/pages/create_entreprise.html',context)


def update_entreprise(request: HttpRequest, pk: str) -> HttpResponse:
    entreprise = Entreprise.objects.get(id=pk)
    form = EntrepriseForm(instance=entreprise)
    if request.method == "POST":
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid:
            form.save()
        return redirect('entreprises')
    context = {'form': form,"type":"update"}
    return render(request, 'reclapp/pages/create_entreprise.html',context)


def delete_entreprise(request: HttpRequest, pk:str) -> HttpResponse:
    entreprise = Entreprise.objects.get(id=pk)
    entreprise.delete()
    return redirect('entreprises')  



def create_reclamation(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ReclamationForm(request.POST) #POST on récupère l'information 
        if form.is_valid:
            form.save()
        return redirect('reclamations')

    form = ReclamationForm()
    context = {'form': form, "type":"create"}
    return render(request, 'reclapp/pages/create_reclamation.html',context)


def update_reclamation(request: HttpRequest, pk: str) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    form = ReclamationForm(instance=reclamation)
    if request.method == "POST":
        form = ReclamationForm(request.POST, instance=reclamation)
        if form.is_valid:
            form.save()
        return redirect('reclamations')
    context = {'form': form,"type":"update"}
    return render(request, 'reclapp/pages/create_reclamation.html',context)


def delete_reclamation(request: HttpRequest, pk:str) -> HttpResponse:
    reclamation = Reclamation.objects.get(id=pk)
    reclamation.delete()
    return redirect('clients')    