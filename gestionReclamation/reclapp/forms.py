from django.forms import ModelForm

from.models import Entreprise, Client, Reclamation

from django.contrib.auth.models import User


class EntrepriseForm(ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__' 

class ReclamationForm(ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__' 
       
class ClientForm(ModelForm):# ModelForm paramètre par défaut de Django
    class Meta:
        model = Client
        fields = '__all__'
       

       
