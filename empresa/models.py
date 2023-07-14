from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=20, unique=True, null=True, blank=True)


    def __str__(self):
        return self.nome

class Manutencao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data_manutencao = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('atividade:atividades_empresa', args=[str(self.empresa.id)])


    def __str__(self):
        return f"Manutenção para {self.empresa.nome}"
