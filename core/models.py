from django.db import models

# Create your models here.

class Lojista(models.Model):
    """
    Define um lojista e suas informações. Um lojista tem
    produtos associados a ele, que também podem estar 
    associados a outros lojistas. Entretanto, o estoque
    é particular a cada um deles.
    """
    nome = models.CharField('Nome', max_length=60)
    endereco_web = models.URLField('Endereço web')
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome