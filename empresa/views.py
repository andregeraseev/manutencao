# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpresaForm
from .models import Empresa

def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmpresaForm()
    return render(request, 'cadastro_empresa.html', {'form': form})


def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'editar_empresa.html', {'form': form, 'empresa': empresa})

def listar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'listar_empresas.html', {'empresas': empresas})
