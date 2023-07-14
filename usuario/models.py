from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(max_length=20, unique=True, null=True, blank=True)

