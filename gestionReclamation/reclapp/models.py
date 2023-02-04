from django.db import models


# Create your models here.

class Entreprise(models.Model):
    nom=models.CharField(max_length=40)
    domaine=models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nom}"




class Client(models.Model):
    nom=models.CharField(max_length=20)
    email=models.CharField(max_length=30)

    entrerpise = models.ForeignKey(
        Entreprise,
        related_name='entreprises',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    entrerpise = models.ManyToManyField(
        Entreprise,
        related_name='entreprises',
        null=True,
        blank=True,
        
    )

    def __str__(self) -> str:
        return f"{self.nom}"




class Reclamation(models.Model):
    description=models.TextField(null=True, blank=True)
    date_de_creation=models.DateField(auto_now_add=True)

    client = models.OneToOneField(
        Client,
        related_name='entreprises',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    
    client = models.ForeignKey(
        Client,
        related_name='entreprises',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


    def __str__(self) -> str:
        return f"{self.description}"    



