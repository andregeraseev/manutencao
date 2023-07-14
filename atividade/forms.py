from django import forms
from .models import  Atividade, Item
from empresa.models import Empresa,Manutencao
from django import forms
from empresa.models import Manutencao

# forms.py
from django import forms
from atividade.models import Atividade, Item


# forms.py
from django import forms
from atividade.models import Atividade, Item

from django import forms
from django.forms import inlineformset_factory
from .models import Atividade, Item

# forms.py
from django import forms
from django.forms import inlineformset_factory
from atividade.models import Atividade, Item

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['area', 'status']

ItemFormSet = inlineformset_factory(Atividade, Item, fields=('descricao',), extra=1, can_delete=False)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao']


class AlterarDataManutencaoForm(forms.Form):
    manutencao_id = forms.IntegerField(widget=forms.HiddenInput())
    data_manutencao = forms.DateField(label='Nova Data da Manutenção')

    def clean_data_manutencao(self):
        data_manutencao = self.cleaned_data['data_manutencao']
        # Adicione aqui as validações adicionais que você deseja para a nova data da manutenção
        return data_manutencao


class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ('empresa', 'data_manutencao')
        widgets = {
            'data_manutencao': forms.DateInput(attrs={'type': 'date'})
        }


