
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from pycpfcnpj import cpfcnpj

class UserProfileForm(UserCreationForm):
    cpf_cnpj = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_cpf_cnpj(self):
        cpf_cnpj = self.cleaned_data['cpf_cnpj']

        # Verificar se o CPF/CNPJ é válido
        if not cpfcnpj.validate(cpf_cnpj):
            raise forms.ValidationError("CPF/CNPJ inválido.")

        return cpf_cnpj

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user_profile = UserProfile(user=user, cpf_cnpj=self.cleaned_data['cpf_cnpj'])

        if commit:
            user.save()
            user_profile.save()

        return user, user_profile


