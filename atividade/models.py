from django.db import models
from empresa.models import Manutencao

class Atividade(models.Model):
    STATUS_CHOICES = (
        ('concluido', 'Concluído'),
        ('em_manutencao', 'Em Manutenção'),
        ('pendente', 'Pendente'),
    )

    area = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    manutencao = models.ForeignKey(Manutencao, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.area

    @property
    def checka(self):
        return self.item_set.filter(checado=True).count()

    @property
    def items_total(self):
        return self.item_set.all().count()


class Item(models.Model):
    STATUS_CHOICES = (
        ('concluido', 'Concluído'),
        ('em_manutencao', 'Em Manutenção'),
        ('pendente', 'Pendente'),
    )
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    comentario = models.TextField(max_length=500, null=True, blank=True )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default= "Pendente")
    foto1 = models.ImageField(upload_to='item_photos', null=True, blank=True)
    foto2 = models.ImageField(upload_to='item_photos', null=True, blank=True)
    foto3 = models.ImageField(upload_to='item_photos', null=True, blank=True)
    checado = models.BooleanField(default=False)

    # Outros campos relevantes aqui

    def __str__(self):
        return self.descricao

    def alterar_status(self):
        if self.status == 'Pendente':
            self.status = 'Concluído'
            self.checado = True
        else:
            self.status = 'Pendente'
            self.checado = False
        self.save()


class AreaChoise(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class ItemChoise(models.Model):
    AreaChoise = models.ForeignKey(AreaChoise, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome
