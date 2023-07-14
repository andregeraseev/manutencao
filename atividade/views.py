
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from atividade.forms import ManutencaoForm
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Manutencao
from django.shortcuts import get_object_or_404, render
from .models import Manutencao
from django.shortcuts import render, get_object_or_404
from .models import Atividade, Item
from .models import AreaChoise, ItemChoise

def adicionar_manutencao(request):
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            manutencao = form.save()
            return redirect('atividade:adicionar_atividade', manutencao_id=manutencao.id)
    else:
        form = ManutencaoForm()
    return render(request, 'adicionar_manutencao.html', {'form': form})





def adicionar_atividade(request, manutencao_id):
    manutencao = Manutencao.objects.get(id=manutencao_id)
    areas = AreaChoise.objects.all()
    itens = ItemChoise.objects.all()
    atividades = Atividade.objects.filter(manutencao=manutencao)
    if request.method == 'POST':
        area_id = request.POST.get('area')
        area = AreaChoise.objects.get(id=area_id)
        status = request.POST.get('status')
        itens_selecionados = request.POST.getlist('itens[]')

        atividade = Atividade.objects.create(area=area.nome, status=status, manutencao=manutencao)

        for item_id in itens_selecionados:
            item = ItemChoise.objects.get(id=item_id)
            Item.objects.create(atividade=atividade, descricao=item.nome)

        # Verifica se a solicitação veio da página de edição
        referer_url = request.META.get('HTTP_REFERER')
        if 'editar_manutencao' in referer_url:
            return redirect('atividade:editar_manutencao', manutencao_id=manutencao_id)
        else:
            return redirect('atividade:adicionar_atividade', manutencao_id=manutencao_id)

    return render(request, 'adicionar_atividade.html', {'atividades':atividades,'manutencao': manutencao, 'areas': areas, 'itens': itens})






@csrf_exempt
def excluir_atividade(request, area_id):
    if request.method == "POST":
        print("deletando")
        atividade = get_object_or_404(Atividade, pk=area_id)
        atividade.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})


from django.db.models import Q

from django.db.models import Q


def editar_manutencao(request, manutencao_id):
    manutencao = Manutencao.objects.get(id=manutencao_id)
    atividades = Atividade.objects.filter(manutencao=manutencao)
    atividades_descricao = atividades.values_list('area', flat=True)
    area_choises = AreaChoise.objects.filter(nome__in=atividades_descricao)
    itens_choices = ItemChoise.objects.all()
    area_choises_add = AreaChoise.objects.all()

    if request.method == 'POST':
        for atividade in atividades:
            # Primeiro limpamos todos os itens desta atividade
            atividade.item_set.all().delete()

            # Em seguida, adicionamos os novos itens que foram marcados e que pertencem a esta atividade
            item_ids = request.POST.getlist(f'item_{atividade.id}_ids')
            # isto irá criar uma lista de listas, onde cada sublista contém strings de números
            item_ids = [ids.split(',') for ids in item_ids if ids]
            # agora, converta cada string de número em um número inteiro
            item_ids = [int(item_id) for sublist in item_ids for item_id in sublist]

            for item_id in item_ids:
                item = Item(descricao=ItemChoise.objects.get(id=item_id).nome, atividade=atividade)
                item.save()

        return redirect('atividade:editar_manutencao', manutencao_id=manutencao_id)

    return render(request, 'editar_manutencao.html', {
        'manutencao': manutencao,
        'atividades': atividades,
        'itens_choices': itens_choices,
        'area_choises': area_choises,
        'area_choises_add': area_choises_add
    })


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})



def salvar_comentario(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        item.comentario = comentario
        item.save()
    return redirect('atividade:item_detail', item_id=item_id)

def salvar_foto(request, item_id, foto_field):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        foto = request.FILES.get(foto_field)
        if foto:
            setattr(item, foto_field, foto)
            item.save()
    return redirect('atividade:item_detail', item_id=item_id)



def salvar_foto2(request, item_id, foto_field):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        foto = request.FILES.get(foto_field)
        if foto:
            setattr(item, foto_field, foto)
            item.save()
    return redirect('atividade:detalhes_manutencao', manutencao_id=item.atividade.manutencao.id)

def alterar_status_item(request, id):
    print(id)
    atividade = Item.objects.get(id=id)
    atividade.alterar_status()
    return JsonResponse({'status': atividade.status})


def alterar_status(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        atividade.status = status
        atividade.save()
    return redirect('atividade:detalhes_manutencao', manutencao_id=atividade.manutencao.id)

def detalhes_manutencao_view(request, manutencao_id):
    manutencao = get_object_or_404(Manutencao, id=manutencao_id)
    atividades = manutencao.atividade_set.all()  # Acesso às atividades relacionadas à manutenção
    itens = Item.objects.filter(atividade__manutencao=manutencao)  # Acesso aos itens relacionados à manutenção
    for atividade in atividades:

        print(atividade.checka)
    return render(request, 'detalhes_manutencao_2.html', {
        'manutencao': manutencao,
        'atividades': atividades,
        'itens': itens
    })


def acompanhar_manutencao_view(request):
    manutencao_list = Manutencao.objects.all().order_by('-data_manutencao')
    paginator = Paginator(manutencao_list, 10)  # Exibe 10 manutenções por página

    page = request.GET.get('page')
    manutencoes = paginator.get_page(page)

    return render(request, 'lista_acompanhar_manutencao_preventiva.html', {'manutencoes': manutencoes})


def alterar_data_manutencao(request):
    if request.method == 'POST':
        manutencao_id = request.POST.get('manutencaoId')
        print(manutencao_id)
        nova_data = request.POST.get('novaData')
        print(nova_data)
        manutencao = Manutencao.objects.get(id=manutencao_id)
        manutencao.data_manutencao = nova_data
        manutencao.save()
        data = {
            'message': 'Data da manutenção alterada com sucesso!'
        }
        return JsonResponse(data)

    # Se a requisição não for POST ou não for uma requisição AJAX, retorna um erro
    return JsonResponse({'error': 'Método não permitido'}, status=405)



def escolher_manutencao(request):
    manutencao_list = Manutencao.objects.all().order_by('-data_manutencao')
    paginator = Paginator(manutencao_list, 10)  # Exibe 10 manutenções por página

    page = request.GET.get('page')
    try:
        manutencoes = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, entrega a primeira página.
        manutencoes = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo (ex. 9999), entrega a última página de resultados.
        manutencoes = paginator.page(paginator.num_pages)

    manutencao_form = ManutencaoForm(request.POST or None)

    if request.method == 'POST':
        print('aqui')
        manutencao_id = request.POST.get('manutencao_id')
        print('manutencaoid', manutencao_id)
        nova_data = request.POST.get('nova_data')
        print(nova_data)
        manutencao = Manutencao.objects.get(id=manutencao_id)
        print(manutencao)
        manutencao.data_manutencao = nova_data
        manutencao.save()
        return redirect('atividade:escolher_manutencao')

    return render(request, 'escolher_manutencao.html', {'manutencoes': manutencoes, 'manutencao_form': manutencao_form})


#
# def acompanhar_manutencao_view(request):
#     # Lógica para acompanhar as manutenções executadas ou em andamento
#     return render(request, 'acompanhar_manutencao.html')


