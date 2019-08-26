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
    telefone = models.CharField('Telefone', max_length=15)
    endereco_web = models.URLField('Endereço web')
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    """
    Uma descrição de produto. Itens desta tabela podem estar associados a
    nenhum ou vários lojistas.
    """
    nome = models.CharField('Nome', max_length=60)
    lojistas = models.ManyToManyField(Lojista)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    """
    O estoque referente a cada produto cadastrado. Cada loja tem o seu estoque
    exclusivo de um produto.
    """
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    lojista = models.ForeignKey(Lojista, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    preco_unitario = models.DecimalField('Preço unitário (R$)', max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.produto) + ' do lojista ' + str(self.lojista) + ', com quantidade ' \
            + str(self.quantidade)

    class Meta:
        unique_together = [
            'produto',
            'lojista',
        ]


